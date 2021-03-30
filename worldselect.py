# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class WorldSelect:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen

        # Text1 is to display page title
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

        self.defaultWorld = 1
        self.worldSelected = 0
        self.levelSelected = 0
    
    def loadAssets(self):

        # Set background
        self.background1_image = pygame.image.load("images/student_worldselect.jpg")
        self.background1_position = [0,0]

        # Set world 1 button 
        self.button1_position = pygame.Rect(90, 365, 101, 141)

        # Set world 2 button
        self.button2_position = pygame.Rect(702, 328, 799-702, 460-328)

        # Set back button
        self.backbutton3_position = pygame.Rect(29, 29, 60, 50)

    # Main Menu Display
    def display(self):
        # Display background 
        self.display_surface.blit(self.background1_image, self.background1_position)
    
    # Main Menu Actions
    def action(self):
        if(self.worldSelected == 0):
            self.worldSelected = self.defaultWorld
        
        # World 1 button is selected
        if self.button1_position.collidepoint(pygame.mouse.get_pos()):
            print("World Button 1 Pressed!")
            self.levelSelected = 1
            clicksound()
            return 3

        # World 2 button is selected
        elif self.button2_position.collidepoint(pygame.mouse.get_pos()):
            print("World Button 2 Pressed!")
            self.levelSelected = 2
            clicksound()
            return 3

        # Back button is selected
        elif self.backbutton3_position.collidepoint(pygame.mouse.get_pos()):
            print("Back Button Pressed!")
            clicksound()
            return 0
        else:
            return 1
