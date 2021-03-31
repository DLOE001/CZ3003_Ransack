# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Import Spritesheet Class
from spritesheet import Spritesheet

# Import SQL Connection 
import mysqlConnection

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheet('level1spritesheet.png').parse_sprite('sprite41')
        self.rect = self.image.get_rect()
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .35, -.12
        self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        self.monster = None
        self.hearts = 3
        self.score = 0
        self.finished = False
        #Graphics
        self.heartImage = pygame.image.load("images/heart.png")
        self.victoryImage = pygame.image.load("images/victory.png")
        self.starImage = pygame.image.load("images/star.png")
        self.nostarImage = pygame.image.load("images/nostar.png")
        self.okButton = pygame.image.load("images/ok.png")
        #Graphics position(For static graphics)
        self.victoryImage_position = (0,0)
        self.okButton_rect = self.okButton.get_rect().move(572, 584)

    #Draws player and player stats on the screen
    def draw(self, display):
        #Update score label
        self.scoreLabel = pygame.font.SysFont('Arial', 50, True).render("Score: " + str(self.score), True, (0, 0, 0))
        self.scoreLabel_position = (15, 65)
        #Update remaining hearts
        for i in range(self.hearts):
            self.heartImage_position = (i*50+15, 15)
            display.blit(self.heartImage, self.heartImage_position)
        #Display score and hearts
        display.blit(self.scoreLabel, self.scoreLabel_position)
        display.blit(self.image, (self.rect.x, self.rect.y))

    #Display victory popup
    def victoryDisplay(self, display):
        #Mouseover animation
        mouseover(self.okButton, self.okButton_rect)
        #Display popup objects
        #victoryImage = Background
        #okButton = Button
        #finalScore = Text
        #starImage = Image
        #nostarImage = Image
        display.blit(self.victoryImage, self.victoryImage_position)
        display.blit(self.okButton, self.okButton_rect)
        self.finalScore = pygame.font.SysFont('Arial', 50, True).render("Score: " + str(self.score), True, (0, 0, 0))
        self.finalScore_position = (495, 265)
        display.blit(self.finalScore, self.finalScore_position)
        if self.score == 300:
            for i in range(3):
                self.starImage_position = (i*256+276, 390)
                display.blit(self.starImage, self.starImage_position)
        elif self.score == 275:
            for i in range(2):
                self.starImage_position = (i*256+276, 390)
                display.blit(self.starImage, self.starImage_position)
            self.nostarImage_position = (2*256+276, 390)
            display.blit(self.nostarImage, self.nostarImage_position)
        elif self.score == 250:
            self.starImage_position = (276, 390)
            display.blit(self.starImage, self.starImage_position)
            for i in range(2):
                self.nostarImage_position = ((i+1)*256+276, 390)
                display.blit(self.nostarImage, self.nostarImage_position)
        
    #Handle victory popup
    def victoryAction(self, username, level):
        #Check if OK button is clicked
        if self.okButton_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            score = mysqlConnection.retrieveUserQuizScore(username, level)
            if len(score) > 0:
                if score[0][0] < self.score:
                    mysqlConnection.updateUserQuizScore(username, level, self.score)
            elif len(score) == 0:
                mysqlConnection.insertUserQuizScore(username, level, self.score)
            return True


    #Handles player movements and collisions
    def update(self, dt, tiles, monsters):
        self.heartsChecker(monsters)
        self.horizontal_movement(dt)
        self.checkCollisionsx(tiles)
        self.vertical_movement(dt)
        self.checkCollisionsy(tiles)
        self.checkMonsterCollision(monsters)

    #Handle player horizontal movement
    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .3
        elif self.RIGHT_KEY:
            self.acceleration.x += .3
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x

    #Handle player vertical movement
    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        self.rect.bottom = self.position.y

    #Limits the velocity of the player
    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0 

    #Allows player to jump
    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 9
            self.on_ground = False

    #Check for tile collisions with player
    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    #Handle tile collisions against player x axis
    def checkCollisionsx(self, tiles):
        if self.position.x < 0 or self.position.x > 1200 - self.rect.w:
            if self.velocity.x > 0:  # Hit wall moving right
                self.position.x = 1200 - self.rect.w
                self.rect.x = self.position.x
            elif self.velocity.x < 0:  # Hit wall moving left
                self.position.x = 0
                self.rect.x = self.position.x
        else:
            collisions = self.get_hits(tiles)
            for tile in collisions:
                if tile.finish:
                    self.acceleration = pygame.math.Vector2(0, 0)
                    self.freezePlayer()
                    self.finished = True
                elif tile.cancollide:
                    if tile.hazard:
                        self.hearts -= 1
                        if tile.tileid == '100':
                            self.playerRespawn2()
                        elif tile.tileid == '93':
                            self.playerRespawn3()
                        break
                    elif tile.finish:
                        self.freezePlayer()
                        self.finished = True
                    else:
                        if self.velocity.x > 0:  # Hit tile moving right
                            self.position.x = tile.rect.left - self.rect.w
                            self.rect.x = self.position.x
                        elif self.velocity.x < 0:  # Hit tile moving left
                            self.position.x = tile.rect.right
                            self.rect.x = self.position.x

    #Handle tile collisions against player y axis
    def checkCollisionsy(self, tiles):
        self.on_ground = False
        self.rect.bottom += 1
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if tile.finish:
                self.acceleration = pygame.math.Vector2(0, 0)
                self.freezePlayer()
                self.finished = True
            elif tile.cancollide:
                if tile.hazard:
                    self.hearts -= 1
                    if tile.tileid == '100':
                        self.playerRespawn2()
                    elif tile.tileid == '93':
                        self.playerRespawn3()
                    break
                else:
                    if self.velocity.y > 0:  # Hit tile from the top
                        self.on_ground = True
                        self.is_jumping = False
                        self.velocity.y = 0
                        self.position.y = tile.rect.top
                        self.rect.bottom = self.position.y
                    elif self.velocity.y < 0:  # Hit tile from the bottom
                        self.velocity.y = 0
                        self.position.y = tile.rect.bottom + self.rect.h
                        self.rect.bottom = self.position.y

    #Check if player collided with a monster
    def checkMonsterCollision(self, monsters):
        collisions = self.get_hits(monsters)
        for monster in collisions:
            if monster.dead == False:
                self.monster = monster
                self.freezePlayer()

    #Check if player is dead and handles on-death actions
    def heartsChecker(self, monsters):
        if self.hearts <= 0:
            self.playerRespawn1()
            self.score = 0
            self.hearts = 3
            for monster in monsters:
                monster.dead = False
            print("YOU DIED")
        

    #LEVEL 1 SPAWN POINTS
    #Origin spawn point
    def playerRespawn1(self):
        self.freezePlayer()
        self.position.x = 0
        self.rect.x = self.position.x
        self.position.y = 825
        self.rect.y = self.position.y

    #When player dies to spike
    def playerRespawn2(self):
        self.freezePlayer()
        self.position.x = 375
        self.rect.x = self.position.x
        self.position.y = 525
        self.rect.y = self.position.y

    #When player dies to water
    def playerRespawn3(self):
        self.freezePlayer()
        self.position.x = 675
        self.rect.x = self.position.x
        self.position.y = 525
        self.rect.y = self.position.y

    #Stop all player movements
    def freezePlayer(self):
        self.velocity = pygame.math.Vector2(0, 0)
        self.LEFT_KEY, self.RIGHT_KEY = False, False
