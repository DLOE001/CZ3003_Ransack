# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Import SQL Connection 
import mysqlConnection

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class Profile:
    def __init__(self, username, user, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        
        # Set background
        self.background1_image = pygame.image.load("images/profile.jpg")
        self.background1_position = [0,0]

        # Set back button rectangle 
        self.backbutton1_rect = pygame.Rect(28, 28, 61, 53)
                
    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)

        # Retrieve profile data
        self.profileData = mysqlConnection.retrieveProfileData(self.username)
        
        if len(self.profileData)>0:
            # Draw Texts
            # Name
            self.nameText = pygame.font.SysFont('Courier New', 25, True).render(self.username, True, (0, 0, 0))
            self.nameText_position = [240, 268]

            # Email
            self.emailText = pygame.font.SysFont('Courier New', 25).render(self.profileData[0], True, (0, 0, 0))
            self.emailText_position = [255, 343]

            # Title
            self.titleText = pygame.font.SysFont('Courier New', 25).render(self.profileData[1], True, (0, 0, 0))
            self.titleText_position = [255, 417]

            # Worlds Cleared
            self.worldText = pygame.font.SysFont('Courier New', 25).render(str(self.profileData[2])+"/6", True, (0, 0, 0))
            self.worldText_position = [395, 484]
            
            #Display Texts
            self.display_surface.blit(self.nameText, self.nameText_position)
            self.display_surface.blit(self.emailText, self.emailText_position)
            self.display_surface.blit(self.titleText, self.titleText_position)
            self.display_surface.blit(self.worldText, self.worldText_position)
    
    # On click actions of UI components in the leaderboard page         
    def action(self):
        if self.backbutton1_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        else:
            return 13
