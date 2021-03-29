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

class TeacherClassManagement:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        
        # Set background
        self.background1_image = pygame.image.load("images/teacher_class_management.jpg")
        self.background1_position = [0,0]

        # Set back button rectangle 
        self.backbutton1_rect = pygame.Rect(40, 38, 100, 60)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.backbutton1_rect)

        # Table Header
        # Name
        self.nameHeader = pygame.font.SysFont('Courier New', 30, True).render("Name", True, (0, 0, 0))
        self.nameHeader_rect = self.nameHeader.get_rect().move(0,315)
        self.nameHeader_rect.centerx = 281

        # Worlds Cleared
        self.worldHeader = pygame.font.SysFont('Courier New', 30, True).render("Worlds Cleared", True, (0, 0, 0))
        self.worldHeader_rect = self.worldHeader.get_rect().move(0,315)
        self.worldHeader_rect.centerx = 586

        # Overall Score
        self.scoreHeader = pygame.font.SysFont('Courier New', 30, True).render("Overall Score", True, (0, 0, 0))
        self.scoreHeader_rect = self.scoreHeader.get_rect().move(0,315)
        self.scoreHeader_rect.centerx = 900
                
    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)

        #Display Texts
        self.display_surface.blit(self.nameHeader, self.nameHeader_rect)
        self.display_surface.blit(self.worldHeader, self.worldHeader_rect)
        self.display_surface.blit(self.scoreHeader, self.scoreHeader_rect)
        
        self.students = mysqlConnection.retrieveStudentAccountData()
        if len(self.students) > 0:
            count = 0
            for i in self.students:
                y_axis = count*45+360
                nameText = pygame.font.SysFont('Courier New', 30).render(i[0], True, (0, 0, 0))
                nameRect = nameText.get_rect().move(0,y_axis)
                nameRect.centerx = 281
                worldText = pygame.font.SysFont('Courier New', 30).render(i[4], True, (0, 0, 0))
                worldRect = worldText.get_rect().move(0,y_axis)
                worldRect.centerx = 586
                score = mysqlConnection.retrieveOverallUserQuizScore(i[0])
                scoreText = pygame.font.SysFont('Courier New', 30).render(str(score), True, (0, 0, 0))
                scoreRect = scoreText.get_rect().move(0,y_axis)
                scoreRect.centerx = 900
                self.display_surface.blit(nameText, nameRect)
                self.display_surface.blit(worldText, worldRect)
                self.display_surface.blit(scoreText, scoreRect)
                count+=1
    
    # On click actions of UI components in the leaderboard page         
    def action(self):
        if self.backbutton1_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        else:
            return 12
