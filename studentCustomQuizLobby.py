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

# Import Custom Quiz Object Asset
import customQuizPendingObjAsset

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
        self.displayPending = False
        self.reload = True

    def loadAssets(self):
        # Set background
        self.background1_image = pygame.image.load("images/student_custom_quiz_lobby.jpg")
        self.background1_position = [0,0]

        #Set back button 
        self.backbutton1_position = pygame.Rect(28, 28, 61, 53)
        
        #Set back button 2
        self.backbutton2_image = pygame.image.load("images/custom_quiz_lobby_back.jpg")
        self.backbutton2_rect = self.backbutton2_image.get_rect().move(193, 177)

        # Set create custom quiz button
        self.createCustomQuiz_rect = pygame.Rect(26, 410, 144, 100)
        pygame.draw.rect(self.screen, (255, 255, 255), self.createCustomQuiz_rect)
        
        # Set pending custom quiz button
        self.pendingCustomQuiz_rect = pygame.Rect(32, 518, 139, 98)
        pygame.draw.rect(self.screen, (255, 255, 255), self.pendingCustomQuiz_rect)

        # Set header text
        self.headerText = pygame.font.SysFont('Courier New', 45, True).render("Custom Quiz", True, (247, 230, 82))
        self.headerText_rect = self.headerText.get_rect().move(0, 70)
        self.headerText_rect.centerx = 596

    def changeHeader(self):
        if self.displayPending:
            self.headerText = pygame.font.SysFont('Courier New', 45, True).render("Pending Custom Quiz", True, (247, 230, 82))
        else:
            self.headerText = pygame.font.SysFont('Courier New', 45, True).render("Custom Quiz", True, (247, 230, 82))
        self.headerText_rect = self.headerText.get_rect().move(0, 70)
        self.headerText_rect.centerx = 596
    
    # Student Custom Quiz Lobby
    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)

        # Display header text
        self.display_surface.blit(self.headerText, self.headerText_rect)
    
        if self.displayPending == False:
            if (self.reload == True):
                self.customQuizObjList = []
                self.customQuiz = mysqlConnection.retrieveApprovedCustomQuiz()
                
                # Create the Custom Quiz Objects here
                if (len(self.customQuiz) <=0):
                    pass
                else:
                    for i in range(len(self.customQuiz)):
                        self.customQuizObjList.append(customQuizObjAsset.CustomQuizObjAsset(self.user, self.username, self.customQuiz[i][2], self.customQuiz[i][8], i, self.display_surface))    
                self.reload = False
                
            if (len(self.customQuizObjList) > 0):
                for j in self.customQuizObjList:
                    j.display()
        else:
            # Display Back Button
            self.display_surface.blit(self.backbutton2_image, self.backbutton2_rect)
            
            if (self.reload == True):
                self.customQuizPendingObjList = []
                self.customQuiz = mysqlConnection.retrievePendingCustomQuiz(self.username)
                # Create the Custom Quiz Objects here
                if (len(self.customQuiz) <=0):
                    pass
                else:
                    for i in range(len(self.customQuiz)):
                        self.customQuizPendingObjList.append(customQuizPendingObjAsset.CustomQuizPendingObjAsset(self.user, self.username, self.customQuiz[i][2], self.customQuiz[i][8], i, self.display_surface))    
                self.reload = False
                
            if (len(self.customQuizPendingObjList) > 0):
                for j in self.customQuizPendingObjList:
                    j.display()
    def action(self):
        if( self.displayPending == False):
            for i in self.customQuizObjList:
                i.action()
                if(getattr(i, 'stopRunning')):
                    return 8
        else:
            for i in self.customQuizPendingObjList:
                i.action()
                if(getattr(i, 'stopRunning')):
                    return 8
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            self.displayPending = False
            self.changeHeader()
            return 0
        if self.backbutton2_rect.collidepoint(pygame.mouse.get_pos()) and self.displayPending:
            clicksound()
            self.displayPending = False
            self.changeHeader()
        if self.pendingCustomQuiz_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            self.displayPending = True
            self.changeHeader()
        if self.createCustomQuiz_rect.collidepoint(pygame.mouse.get_pos()):
            self.displayPending = False
            self.changeHeader()
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
    
