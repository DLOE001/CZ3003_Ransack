from pygame.locals import *

# Import Game Assets
from tiles import *
from spritesheet import Spritesheet
from player import Player
from monster import Monster
from quiz import Quiz

# Import SQL Connection 
import mysqlConnection

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
pygame.display.set_caption("EyeLearnSE")

class QuizLevel:
    def display(self, worldSelected, levelSelected):
        DISPLAY_W, DISPLAY_H = 1200, 900
        canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
        window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
        running = True
        clock = pygame.time.Clock()
        TARGET_FPS = 60
        ################################# LOAD SPRITESHEET PLAYER, MONSTERS AND QUIZ ###################################
        level1spritesheet = Spritesheet('level1spritesheet.png')
        player = Player()
        
        levelQuestions = mysqlConnection.retrieveQuizLevelData(worldSelected, levelSelected)
        
        quiz1 = Quiz(levelQuestions[0][2], levelQuestions[0][3], levelQuestions[0][4], levelQuestions[0][5], levelQuestions[0][6])
        monster1 = Monster(750, 300, quiz1)
        quiz2 = Quiz(levelQuestions[1][2], levelQuestions[1][3], levelQuestions[1][4], levelQuestions[1][5], levelQuestions[1][6])
        monster2 = Monster(225, 300, quiz2)
        quiz3 = Quiz(levelQuestions[2][2], levelQuestions[2][3], levelQuestions[2][4], levelQuestions[2][5], levelQuestions[2][6])
        monster3 = Monster(375, 75, quiz3)
        monsters = []
        monsters.append(monster1)
        monsters.append(monster2)
        monsters.append(monster3)
        #################################### LOAD THE LEVEL #######################################
        background1_image = pygame.image.load('images/single_background.png')
        map = TileMap('level1.csv', level1spritesheet)
        doorchanged = False
        player.position.x, player.position.y = 0, 800
        ################################# GAME LOOP ##########################
        while running:
            windowmoved = False
            dt = clock.tick(60) * .001 * TARGET_FPS
            ################################# CHECK PLAYER INPUT #################################
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.VIDEOEXPOSE:
                    player.acceleration = pygame.math.Vector2(0, 0)
                    windowmoved = True
                elif event.type == pygame.KEYDOWN:
                    if player.monster == None:
                        if event.key == pygame.K_LEFT:
                            player.LEFT_KEY = True
                        elif event.key == pygame.K_RIGHT:
                            player.RIGHT_KEY = True
                        elif event.key == pygame.K_SPACE:
                            player.jump()
        
        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.LEFT_KEY = False
                    elif event.key == pygame.K_RIGHT:
                        player.RIGHT_KEY = False
                    elif event.key == pygame.K_SPACE:
                        if player.is_jumping:
                            player.velocity.y *= .25
                            player.is_jumping = False
        
                if event.type == MOUSEBUTTONDOWN:
                    if player.monster != None:
                        player.monster.quiz.attempt(player)
                    elif player.finished:
                        player.victoryAction()
        
            ################################# UPDATE/ Animate SPRITE #################################
            player.update(dt, map.tiles, monsters)
            # Set back Y axis acceleration when game window is is not moving
            if windowmoved == False:
                player.acceleration.y = player.gravity
            ################################# DRAW SURFACE OBJECTS #################################
            canvas.blit(background1_image, [0,0])
            map.draw_map(canvas)
            player.draw(canvas)
            allmonstersdead = True
            for monster in monsters:
                if monster.dead == False:
                    allmonstersdead = False
                monster.draw(canvas)
            if allmonstersdead and doorchanged == False:
                for tile in map.tiles:
                    if tile.finish:
                        tile.image = Spritesheet('level1spritesheet.png').parse_sprite('sprite32')
                        map.load_map()
                doorchanged = True
            if player.monster != None:
                player.monster.quiz.draw(canvas)
            elif player.finished:
                player.victoryDisplay(canvas)
            ############################ UPDATE WINDOW AND DISPLAY ###############################
            window.blit(canvas, (0,0))
            pygame.display.update()
        
        # Done! Time to quit.
        pygame.quit()
        quit()
