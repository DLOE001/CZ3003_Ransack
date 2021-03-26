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

# Import Create Custom Quiz
import createCustomQuiz

# Import Custom Quiz Object Asset
import customQuizObjAsset

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class StudentCustomQuizLobby:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.reload = True
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        # Set background
        self.background1_image = pygame.image.load("images/student_custom_quiz_lobby.jpg")
        self.background1_position = [0,0]

        #Set back button 
        self.backbutton1_image = pygame.image.load("images/w2.png")
        self.backbutton1_position = self.backbutton1_image.get_rect().move(22, 21)

        # Set create custom quiz button
        self.createCustomQuiz_rect = pygame.Rect(26, 410, 144, 100)
        pygame.draw.rect(self.screen, (255, 255, 255), self.createCustomQuiz_rect)
        
    # Student Custom Quiz Lobby
    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)
        
        # Display back button 
        self.display_surface.blit(self.backbutton1_image, self.backbutton1_position)

        # Hide all buttons 
        self.backbutton1_image.set_alpha(0)
    
        if (self.reload == True):
            self.customQuizObjList = []
            self.customQuiz = mysqlConnection.retrieveAllCustomQuiz()
            
            # Create the Custom Quiz Objects here
            if (len(self.customQuiz) <=0):
                pass
            else:
                for i in range(len(self.customQuiz)):
                    self.customQuizObjList.append(customQuizObjAsset.CustomQuizObjAsset(self.customQuiz[i][2], self.customQuiz[i][8], i, self.display_surface))    
            self.reload = False
            
        if (len(self.customQuizObjList) > 0):
            for j in self.customQuizObjList:
                j.display()
    
    def action(self):
        for i in self.customQuizObjList:
            i.action()
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        if self.createCustomQuiz_rect.collidepoint(pygame.mouse.get_pos()):
            # Create create custom quiz Object
            self.createCustomQuizObj = createCustomQuiz.CreateCustomQuiz(self.username, self.user, self.screen, self.display_surface)
            self.createCustomQuizObj.loadAssets()
            clicksound()
            self.stopRunning = False
            while not self.stopRunning:
                self.createCustomQuizObj.display()
                if (getattr(self.createCustomQuizObj, 'done')):
                    self.stopRunning = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    
                    pygame.display.update()
            self.reload = True
            return 8
        else:
            return 8
    