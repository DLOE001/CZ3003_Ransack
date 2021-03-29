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

class TeacherSummaryReport:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        
        # Set background
        self.background1_image = pygame.image.load("images/teacher_summary_report.jpg")
        self.background1_position = [0,0]

        #Set back button rectangle 
        self.backbutton1_rect = pygame.Rect(40, 38, 100, 60)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.backbutton1_rect)     
                
    def display(self):
        
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)
    
    # On click actions of UI components in the leaderboard page         
    def action(self):
        if self.backbutton1_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        else:
            return 11
