# EyeLearnSE Game by Team Ransack(2021)

# Brings in all the pygame keywords we need
from pygame.locals import *

# Main Menu Class
import mainmenu

# World Select Class
import worldselect

# Import and initialize the pygame library
import pygame
pygame.init()

# Initialise Global Variables
running = True
state = 0

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

# Simulated Console Login
# TODO: To be removed once Login page is done
user = "nil"
while user == "nil":
    print("1: Student, 2: Teacher")
    choice = input()
    if choice == "1":
        user = "Student"
        print("Logged in as Student")
    elif choice == "2":
        user = "Teacher"
        print("Logged in as Teacher")
    else:
        print("Input 1 or 2 only!")

# Create Main Menu Object
menu = mainmenu.MainMenu(username, user, screen, display_surface)
menu.loadAssets()

#Create World Select Object
worldselect = worldselect.WorldSelect(username, user, screen, display_surface)
worldselect.loadAssets()

# Run until the user asks to quit
while running:
    # Display the different menus according to state.
    if state == 0:
        menu.display()
    elif state == 1:
        worldselect.display()
    elif state == -1:
        running = False
    
    # When user clicks the window close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # When user clicks
        if event.type == MOUSEBUTTONDOWN:
            if state == 0:
                state = menu.action()
            elif state == 1:
                state = worldselect.action()
                    
        # Draws the surface object to the screen.   
        pygame.display.update()

    # Fills the screen with colour
    screen.fill(white)


# Done! Time to quit.
pygame.quit()
quit()
