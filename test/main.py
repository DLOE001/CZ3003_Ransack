from pygame.locals import *
from tiles import *
from spritesheet import Spritesheet
from player import Player
from monster import Monster
from quiz import Quiz
################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
pygame.display.set_caption("EyeLearnSE")
DISPLAY_W, DISPLAY_H = 1200, 900
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
TARGET_FPS = 60
################################# LOAD SPRITESHEET PLAYER, MONSTERS AND QUIZ ###################################
level1spritesheet = Spritesheet('level1spritesheet.png')
player = Player()
quiz1 = Quiz("What does ESD mean in Critical Path Analysis?", "Earliest Start Date", "Ernies Super Duck", "Elmo So Dead", "I dont't know")
monster1 = Monster(750, 300, quiz1)
quiz2 = Quiz("What does Backward pass in Critical Path Analysis determine?", "Slack Time", "I don't know", "Longest duration", "Start and End time")
monster2 = Monster(225, 300, quiz2)
quiz3 = Quiz("Which of the below is used commonly used for scheduling?", "Gantt Chart", "Notepad", "Paper", "Word of mouth")
monster3 = Monster(375, 75, quiz3)
monsters = []
monsters.append(monster1)
monsters.append(monster2)
monsters.append(monster3)
#################################### LOAD THE LEVEL #######################################
background1_image = pygame.image.load('single_background.png')
map = TileMap('level1.csv', level1spritesheet)
doorchanged = False
#monsters = TileMap('monster.csv', monsterspritesheet)
player.position.x, player.position.y = 0, 800
################################# GAME LOOP ##########################
while running:
    dt = clock.tick(60) * .001 * TARGET_FPS
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
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

    ################################# UPDATE/ Animate SPRITE #################################
    player.update(dt, map.tiles, monsters)
    ################################# UPDATE WINDOW AND DISPLAY #################################
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
    window.blit(canvas, (0,0))
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
quit()
