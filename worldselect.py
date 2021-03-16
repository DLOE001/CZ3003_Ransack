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
        #Texts
        self.text1 = None
        self.text1_position = None
        #Background
        self.background1_image = None
        self.background1_position = None
        #Buttons
        self.button1_image = None
        self.button1_position = None
        self.button2_image = None
        self.button2_position = None
    
    def loadAssets(self):
        # Text
        self.text1 = pygame.font.SysFont('Broadway', 75).render("World Select", True, (0, 0, 0))
        
        # Test Positions
        self.text1_position = [364,8]

        # Graphics
        self.background1_image = pygame.image.load("images/student_worldselect.jpg")
        self.button1_image = pygame.image.load("images/w2.png")
        self.button2_image = pygame.image.load("images/w2.png")

        # Graphics Positions
        self.background1_position = [0,0]

        self.button1_position = self.button1_image.get_rect().move(17, 23)
        self.button2_position = self.button2_image.get_rect().move(280, 423)

    # Main Menu Display
    def display(self):
        # Copy of background image
        self.display_surface.blit(self.background1_image, self.background1_position)
        
        #Copy text
        self.screen.blit(self.text1, self.text1_position)

        # Copy of back button
        self.display_surface.blit(self.button1_image, self.button1_position)
        self.display_surface.blit(self.button2_image, self.button2_position)

        '''
        # Mouseover Animation
        mouseover(self.button1_image, self.button1_position)
        mouseover(self.button2_image, self.button2_position)
        '''

        # Hide all buttons 
        self.button1_image.set_alpha(0)
        self.button2_image.set_alpha(0)

    # Main Menu Actions
    def action(self):
        if self.button1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        elif self.button2_position.collidepoint(pygame.mouse.get_pos()):
            print("Query Button Pressed!")
            clicksound()
            return 1
        else:
            return 0
