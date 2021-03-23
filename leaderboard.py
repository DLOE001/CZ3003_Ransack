# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

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

class Leaderboard:
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
        self.background1_image = pygame.image.load("images/leaderboard.jpg")
        self.background1_position = [0,0]

        #Set back button 
        self.backbutton1_image = pygame.image.load("images/w2.png")
        self.backbutton1_position = self.backbutton1_image.get_rect().move(23, 23)

        # Set Rank Text
        self.ranktext1 = pygame.font.SysFont('Broadway', 40).render("Rank", True, (0, 0, 0))
        self.ranktext1_position = [210,350]

        # Set Username Text
        self.usernametext2 = pygame.font.SysFont('Broadway', 40).render("Username", True, (0, 0, 0))
        self.usernametext2_position = [380,350]

        # Set Score Text
        self.scoretext3 = pygame.font.SysFont('Broadway', 40).render("Total Score", True, (0, 0, 0))
        self.scoretext3_position = [684,350]

        # Set Row 1 data
        self.row1Rank = pygame.font.SysFont('Broadway', 40).render("1", True, (0, 0, 0))
        self.row1Rank_position = [210,415]

        self.row1Username = pygame.font.SysFont('Broadway', 40).render("Aaaaa", True, (0, 0, 0))
        self.row1Username_position = [380,415]

        self.row1Score = pygame.font.SysFont('Broadway', 40).render("999", True, (0, 0, 0))
        self.row1Score_position = [684,415]
        
        # Set Row 2 data
        self.row2Rank = pygame.font.SysFont('Broadway', 40).render("2", True, (0, 0, 0))
        self.row2Rank_position = [210,480]

        self.row2Username = pygame.font.SysFont('Broadway', 40).render("Bbbbb", True, (0, 0, 0))
        self.row2Username_position = [380,480]

        self.row2Score = pygame.font.SysFont('Broadway', 40).render("888", True, (0, 0, 0))
        self.row2Score_position = [684,480]

        # Set Row 3 data
        self.row3Rank = pygame.font.SysFont('Broadway', 40).render("3", True, (0, 0, 0))
        self.row3Rank_position = [210,542]

        self.row3Username = pygame.font.SysFont('Broadway', 40).render("Ccccc", True, (0, 0, 0))
        self.row3Username_position = [380,542]

        self.row3Score = pygame.font.SysFont('Broadway', 40).render("777", True, (0, 0, 0))
        self.row3Score_position = [684,542]

        # Set Row 4 data
        self.row4Rank = pygame.font.SysFont('Broadway', 40).render("4", True, (0, 0, 0))
        self.row4Rank_position = [210,597]

        self.row4Username = pygame.font.SysFont('Broadway', 40).render("Ddddd", True, (0, 0, 0))
        self.row4Username_position = [380,597]

        self.row4Score = pygame.font.SysFont('Broadway', 40).render("420", True, (0, 0, 0))
        self.row4Score_position = [684,597]

        # Set Row 5 data
        self.row5Rank = pygame.font.SysFont('Broadway', 40).render("5", True, (0, 0, 0))
        self.row5Rank_position = [210,660]

        self.row5Username = pygame.font.SysFont('Broadway', 40).render("Eeeee", True, (0, 0, 0))
        self.row5Username_position = [380,660]

        self.row5Score = pygame.font.SysFont('Broadway', 40).render("69", True, (0, 0, 0))
        self.row5Score_position = [684,660]
        
    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)
        
        # Display back button 
        self.display_surface.blit(self.backbutton1_image, self.backbutton1_position)

        # Hide all buttons 
        self.backbutton1_image.set_alpha(0)

        # Display Rank Text
        self.screen.blit(self.ranktext1, self.ranktext1_position)

        # Display Username Text
        self.screen.blit(self.usernametext2, self.usernametext2_position)

        # Display Score Text
        self.screen.blit(self.scoretext3, self.scoretext3_position)

        # Display Row 1 Data
        self.screen.blit(self.row1Rank, self.row1Rank_position)
        self.screen.blit(self.row1Username, self.row1Username_position)
        self.screen.blit(self.row1Score, self.row1Score_position)

        # Display Row 2 Data
        self.screen.blit(self.row2Rank, self.row2Rank_position)
        self.screen.blit(self.row2Username, self.row2Username_position)
        self.screen.blit(self.row2Score, self.row2Score_position)

        # Display Row 3 Data
        self.screen.blit(self.row3Rank, self.row3Rank_position)
        self.screen.blit(self.row3Username, self.row3Username_position)
        self.screen.blit(self.row3Score, self.row3Score_position)

        # Display Row 4 Data
        self.screen.blit(self.row4Rank, self.row4Rank_position)
        self.screen.blit(self.row4Username, self.row4Username_position)
        self.screen.blit(self.row4Score, self.row4Score_position)

        # Display Row 5 Data
        self.screen.blit(self.row5Rank, self.row5Rank_position)
        self.screen.blit(self.row5Username, self.row5Username_position)
        self.screen.blit(self.row5Score, self.row5Score_position)

    def action(self):
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        else:
            return 4