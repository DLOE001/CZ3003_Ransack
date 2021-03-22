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

class Friends:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen

        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        # Set background
        self.background1_image = pygame.image.load("images/friends.jpg")
        self.background1_position = [0,0]

        #Set back button 
        self.backbutton1_image = pygame.image.load("images/w2.png")
        self.backbutton1_position = self.backbutton1_image.get_rect().move(109, 78)

    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)
        
        # Display back button 
        self.display_surface.blit(self.backbutton1_image, self.backbutton1_position)

        # Hide all buttons 
        self.backbutton1_image.set_alpha(0)

    def action(self):
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0