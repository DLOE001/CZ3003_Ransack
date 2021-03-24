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
        self.retrievedLeaderboard = False
        self.leaderboardList = []
        self.storeRowTitleText = []
        self.storeRowUsernameText = []
        self.storeRowScoreText = []
        self.storeRowTitlePositions = []
        self.storeRowUsernamePositions = []
        self.storeRowScorePositions = []
        self.counter = 0
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        
        self.leaderboardList = mysqlConnection.retrieveLeaderboard();
        
        # Set background
        self.background1_image = pygame.image.load("images/leaderboard.jpg")
        self.background1_position = [0,0]

        #Set back button 
        self.backbutton1_image = pygame.image.load("images/w2.png")
        self.backbutton1_position = self.backbutton1_image.get_rect().move(23, 23)

        # Set Rank Text
        self.ranktext1 = pygame.font.SysFont('Broadway', 30).render("Rank", True, (0, 0, 0))
        self.ranktext1_position = [217,325]
        
        # Set Title Text
        self.titletext1 = pygame.font.SysFont('Broadway', 30).render("Title", True, (0, 0, 0))
        self.titletext1_position = [390,325]

        # Set Username Text
        self.usernametext2 = pygame.font.SysFont('Broadway', 30).render("Username", True, (0, 0, 0))
        self.usernametext2_position = [550,325]

        # Set Score Text
        self.scoretext3 = pygame.font.SysFont('Broadway', 30).render("Overall Score", True, (0, 0, 0))
        self.scoretext3_position = [745,325]

        # Set Row 1 data
        self.row1Rank = pygame.font.SysFont('Courier New', 30).render("1", True, (0, 0, 0))
        self.row1Rank_position = [260,380]

        self.row1Title = None
        self.storeRowTitleText.append(self.row1Title)
        self.row1Title_position = [340,380]
        self.storeRowTitlePositions.append(self.row1Title_position)
        
        self.row1Username = None
        self.storeRowUsernameText.append(self.row1Username)
        self.row1Username_position = [550,380]
        self.storeRowUsernamePositions.append(self.row1Username_position)
        
        self.row1Score = None
        self.storeRowScoreText.append(self.row1Score)
        self.row1Score_position = [745,380]
        self.storeRowScorePositions.append(self.row1Score_position)
        
        # Set Row 2 data
        self.row2Rank = pygame.font.SysFont('Courier New', 30).render("2", True, (0, 0, 0))
        self.row2Rank_position = [260,440]
        
        self.row2Title = None
        self.storeRowTitleText.append(self.row2Title)
        self.row2Title_position = [340,440]
        self.storeRowTitlePositions.append(self.row2Title_position)

        self.row2Username = None
        self.storeRowUsernameText.append(self.row2Username)
        self.row2Username_position = [550,440]
        self.storeRowUsernamePositions.append(self.row2Username_position)
        
        self.row2Score = None
        self.storeRowScoreText.append(self.row2Score)
        self.row2Score_position = [745,440]
        self.storeRowScorePositions.append(self.row2Score_position)
        
        # Set Row 3 data
        self.row3Rank = pygame.font.SysFont('Courier New', 30).render("3", True, (0, 0, 0))
        self.row3Rank_position = [260,503]

        self.row3Title = None
        self.storeRowTitleText.append(self.row3Title)
        self.row3Title_position = [340,503]
        self.storeRowTitlePositions.append(self.row3Title_position)
        
        self.row3Username = None
        self.storeRowUsernameText.append(self.row3Username)
        self.row3Username_position = [550,503]
        self.storeRowUsernamePositions.append(self.row3Username_position)
        
        self.row3Score = None
        self.storeRowScoreText.append(self.row3Score)
        self.row3Score_position = [745,503]
        self.storeRowScorePositions.append(self.row3Score_position)
        
        # Set Row 4 data
        self.row4Rank = pygame.font.SysFont('Courier New', 30).render("4", True, (0, 0, 0))
        self.row4Rank_position = [260,557]

        self.row4Title = None
        self.storeRowTitleText.append(self.row4Title)
        self.row4Title_position = [340,557]
        self.storeRowTitlePositions.append(self.row4Title_position)
        
        self.row4Username = None
        self.storeRowUsernameText.append(self.row4Username)
        self.row4Username_position = [550,557]
        self.storeRowUsernamePositions.append(self.row4Username_position)
        
        self.row4Score = None
        self.storeRowScoreText.append(self.row4Score)
        self.row4Score_position = [745,557]
        self.storeRowScorePositions.append(self.row4Score_position)
        
        # Set Row 5 data
        self.row5Rank = pygame.font.SysFont('Courier New', 30).render("5", True, (0, 0, 0))
        self.row5Rank_position = [260,612]

        self.row5Title = None
        self.storeRowTitleText.append(self.row5Title)
        self.row5Title_position = [340,612]
        self.storeRowTitlePositions.append(self.row5Title_position)
        
        self.row5Username = None
        self.storeRowUsernameText.append(self.row5Username)
        self.row5Username_position = [550,612]
        self.storeRowUsernamePositions.append(self.row5Username_position)
        
        self.row5Score = None
        self.storeRowScoreText.append(self.row5Score)
        self.row5Score_position = [745,612]
        self.storeRowScorePositions.append(self.row5Score_position)
        
        # Set the text for the top 5 overall score personnel in the leaderboard UI
        if(len(self.leaderboardList) > 0):
            for i in range(len(self.leaderboardList)):
                self.storeRowTitleText[i] = pygame.font.SysFont('Courier New', 30).render(self.leaderboardList[i][0], True, (0, 0, 0))
                self.storeRowUsernameText[i] = pygame.font.SysFont('Courier New', 30).render(self.leaderboardList[i][1], True, (0, 0, 0))
                self.storeRowScoreText[i] = pygame.font.SysFont('Courier New', 30).render(str(self.leaderboardList[i][2]), True, (0, 0, 0))
                
    def display(self):
        
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)
        
        # Display back button 
        self.display_surface.blit(self.backbutton1_image, self.backbutton1_position)

        # Hide all buttons 
        self.backbutton1_image.set_alpha(0)

        # Display Ranking
        self.screen.blit(self.row1Rank, self.row1Rank_position)
        self.screen.blit(self.row2Rank, self.row2Rank_position)
        self.screen.blit(self.row3Rank, self.row3Rank_position)
        self.screen.blit(self.row4Rank, self.row4Rank_position)
        self.screen.blit(self.row5Rank, self.row5Rank_position)
        
        # Display Rank Text
        self.screen.blit(self.ranktext1, self.ranktext1_position)

        # Display Title Text
        self.screen.blit(self.titletext1, self.titletext1_position)
        
        # Display Username Text
        self.screen.blit(self.usernametext2, self.usernametext2_position)

        # Display Score Text
        self.screen.blit(self.scoretext3, self.scoretext3_position)

        # Display the top 5 overall score personnel in the leaderboard UI
        if(len(self.leaderboardList) > 0):
            for i in range(len(self.leaderboardList)):
                self.screen.blit(self.storeRowTitleText[i], self.storeRowTitlePositions[i])
                self.screen.blit(self.storeRowUsernameText[i], self.storeRowUsernamePositions[i])
                self.screen.blit(self.storeRowScoreText[i], self.storeRowScorePositions[i])
    
    # On click actions of UI components in the leaderboard page         
    def action(self):
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        else:
            return 4