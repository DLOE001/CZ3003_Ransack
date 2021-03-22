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

# Leadeboard  Class
import friends

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
username = "Daniel Loe"
user = "Student"
loggedIn = False

# Create Login Object
login = loginPage.Login(username, user, screen, display_surface)
login.loadAssets()

# Create Login Object
register = registerPage.Register(username, user, screen, display_surface)
register.loadAssets()

# Create Main Menu Object
menu = mainmenu.MainMenu(username, user, screen, display_surface)
menu.loadAssets()

#Create World Select Object
worldSelect = worldselect.WorldSelect(username, user, screen, display_surface)
worldSelect.loadAssets()

#Create Leaderboard Object
leaderboard = leaderboard.Leaderboard(username, user, screen, display_surface)
leaderboard.loadAssets()

#Create Friends Object
friends = friends.Friends(username, user, screen, display_surface)
friends.loadAssets()

#Create World Select Object
quizLevel = quizLevel.QuizLevel()

# Run until the user asks to quit
while running:
    # Display the different menus according to state.
    if state == 0:
        menu.display()
    elif state == 1:
        worldSelect.display()
    elif state == 2:
        login.display()
        if (getattr(login, 'done') and getattr(login, 'success')):
            state = 0
            #loggedIn = True
    elif state == 3:
        if quizLevel.display(username, getattr(worldSelect, 'worldSelected'), getattr(worldSelect, 'levelSelected')):
            state = 1
    elif state == 4:
        leaderboard.display()
    elif state == 5:
        friends.display()
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
                state = leaderboard.action()
            elif state == 5:
                state = friends.action() 
            #elif state == 2:
                #state = login.action()
                
        # Draws the surface object to the screen.   
        pygame.display.update()

    # Fills the screen with colour
    screen.fill(white)

# Done! Time to quit.
pygame.quit()
quit()

