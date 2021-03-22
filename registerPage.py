# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Imports Text Box
from inputBox import InputBox

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
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class Register:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        self.backToLogin = False

        # Set background
        self.background1_image = pygame.image.load("images/register.jpg")
        self.background1_position = [0,0]
        
        # Set back button
        self.backbutton3_image = pygame.image.load("images/w2.png")
        self.backbutton3_position = self.backbutton3_image.get_rect().move(275, 260)
        
        # Hide Buttons
        self.backbutton3_image.set_alpha(0)
        print("loaded")

    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)

        # Set back button
        self.display_surface.blit(self.backbutton3_image, self.backbutton3_position)

    # Register Page Actions
    def action(self):
        # Back button is selected
        if self.backbutton3_position.collidepoint(pygame.mouse.get_pos()):
            self.backToLogin = True
            print("Back Button Pressed!")
            clicksound()
            return 2
        else:
            return 6
        