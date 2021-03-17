import pygame
from spritesheet import Spritesheet

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

    #Draws player on the screen
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    #Handles player movements and collisions
    def update(self, dt, tiles, monsters):
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
        self.rect.clamp_ip((0, 0), (1200, 900))

    #Handle player vertical movement
    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        self.rect.bottom = self.position.y
        self.rect.clamp_ip((0, 0), (1200, 900))

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
                if tile.cancollide:
                    if tile.hazard:
                        if tile.tileid == '100':
                            self.playerRespawn2()
                        elif tile.tileid == '93':
                            self.playerRespawn3()
                    elif tile.finish:
                        pygame.quit()
                        quit()
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
            if tile.cancollide:
                if tile.hazard:
                    if tile.tileid == '100':
                        self.playerRespawn2()
                    elif tile.tileid == '93':
                        self.playerRespawn3()
                elif tile.finish:
                    pygame.quit()
                    quit()
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
                self.LEFT_KEY, self.RIGHT_KEY = False, False
                self.velocity.x = 0
                self.velocity.y = 0

    #LEVEL 1 SPAWN POINTS
    #Origin spawn point
    def playerRespawn1(self):
        self.position.x = 0
        self.rect.x = self.position.x
        self.position.y = 800
        self.rect.y = self.position.y

    #When player dies to spike
    def playerRespawn2(self):
        self.position.x = 375
        self.rect.x = self.position.x
        self.position.y = 525
        self.rect.y = self.position.y

    #When player dies to water
    def playerRespawn3(self):
        self.position.x = 675
        self.rect.x = self.position.x
        self.position.y = 525
        self.rect.y = self.position.y
