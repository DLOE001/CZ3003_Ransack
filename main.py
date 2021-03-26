# EyeLearnSE Game by Team Ransack(2021)

# Brings in all the pygame keywords we need
from pygame.locals import *

# Main Menu Class
import mainmenu

# World Select Class
import worldselect

# Login Page Class
import loginPage

# Login Register Class
import registerPage

# Quiz Level Page Class
import quizLevel

# Leadeboard  Class
import leaderboard

# Friends  Class
import friends

# Upload Assignment Class
import uploadAssignmentPage

# Import and initialize the pygame library
import pygame
pygame.init()

# Initialise Global Variables
running = True
state = 2

# Name of the game
pygame.display.set_caption("EyeLearnSE")

# Game window resolution
screen_width = 1200
screen_height = 900

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))
  
# Set the display surface 
display_surface = pygame.display.set_mode((screen_width, screen_height))

# Colour Coordinates(RGB)
white = [255, 255, 255]

# Sample User Data
username = ""
user = ""

# Create Login Object
login = loginPage.Login(username, user, screen, display_surface)
login.loadAssets()
    
# Create Login Object
register = registerPage.Register(username, user, screen, display_surface)
register.loadAssets()

# Create Main Menu Object
menu = mainmenu.MainMenu(username, user, screen, display_surface)
menu.loadAssets()
    
# Create World Select Object
worldSelect = worldselect.WorldSelect(username, user, screen, display_surface)
worldSelect.loadAssets()

# Create Leaderboard Object
leaderBoard = leaderboard.Leaderboard(username, user, screen, display_surface)
leaderBoard.loadAssets()

# Create Friends Object
friendMenu = friends.Friends(username, user, screen, display_surface)
friendMenu.loadAssets()

# Create Upload Assignment Object
uploadAssignment = uploadAssignmentPage.UploadAssignment(username, user, screen, display_surface)
uploadAssignment.loadAssets()

# Create Quiz Level Object
level = quizLevel.QuizLevel()

# Recreates the UI Objects passing in the logged in user's username and user type
def recreateUIObj(username, user):
    global login
    global menu
    global worldSelect
    global level
    global leaderBoard
    global friendMenu
    
     # Create Login Object
    login = loginPage.Login(username, user, screen, display_surface)
    login.loadAssets()
                
    # Create Main Menu Object
    menu = mainmenu.MainMenu(username, user, screen, display_surface)
    menu.loadAssets()
                
    #Create World Select Object
    worldSelect = worldselect.WorldSelect(username, user, screen, display_surface)
    worldSelect.loadAssets()
                
    # Create Leaderboard Object
    leaderBoard = leaderboard.Leaderboard(username, user, screen, display_surface)
    leaderBoard.loadAssets()
    
    # Create Friends Object
    friendMenu = friends.Friends(username, user, screen, display_surface)
    friendMenu.loadAssets()
    
    # Create Upload Assignment Object
    uploadAssignment = uploadAssignmentPage.UploadAssignment(username, user, screen, display_surface)
    uploadAssignment.loadAssets()
    
    #Create Quiz Level Object
    level = quizLevel.QuizLevel()

# Run until the user asks to quit
while running:
    # Display the different menus according to state.
    if state == 0:
        # Set done = false so to keep page refreshing 
        setattr(friendMenu, 'done', False)
        setattr(uploadAssignment, 'done', False)
        menu.display()
    elif state == 1:
        worldSelect.display()
    elif state == 2:
        if(getattr(register, 'backToLogin') or getattr(register, 'successfulRegister')):
            setattr(login, 'done', False)
        login.display()
        if (getattr(login, 'done') and getattr(login, 'success')):
            username = getattr(login, 'username')
            user = getattr(login, 'user')
            recreateUIObj(username, user)
            state = 0
        elif (getattr(login, 'done') and getattr(login, 'registerClicked')):
            setattr(register, 'done', False)
            state = 6
    elif state == 3:
        if level.display(username, getattr(worldSelect, 'worldSelected'), getattr(worldSelect, 'levelSelected')):
            leaderBoard.loadAssets()
            state = 1
    elif state == 4:
        leaderBoard.display()
    elif state == 5:
        friendMenu.display()
        if (getattr(friendMenu, 'done')):
            state = 0
    elif state == 6:
        register.display()
        if (getattr(register, 'done')):
            state = 2
    elif state == 7:
        uploadAssignment.display()
        if (getattr(uploadAssignment, 'done')):
            state = 0
            
    elif state == -1:
        running = False
 
    # When user clicks the window close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("CLICKED")
            running = False
        # When user clicks
        if event.type == MOUSEBUTTONDOWN:
            if state == 0:
                state = menu.action()
            elif state == 1:
                state = worldSelect.action()
            elif state == 4:
                state = leaderBoard.action()
            #elif state == 5:
                #state = friendMenu.action()
            #elif state == 6:
                #state = register.action()
            #elif state == 2:
                #state = login.action()
            #elif state == 7:
                #state = uploadAssignment.action()
                
        # Draws the surface object to the screen.   
        pygame.display.update()

    # Fills the screen with colour
    screen.fill(white)

# Done! Time to quit.
pygame.quit()
quit()

