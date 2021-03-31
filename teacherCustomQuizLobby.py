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

# Import Teacher Review Custom Quiz Object Asset
import teacherReviewCustomQuizObjAsset

# Import Teacher Review Custom Quiz Object Asset
import teacherModifyCustomQuizObjAsset

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class TeacherCustomQuizLobby:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.reload = True
        self.displayReview = False
        self.displayModify = False
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        # Set background
        self.background1_image = pygame.image.load("images/teacher_custom_quiz_lobby.jpg")
        self.background1_position = [0,0]

        #Set back button
        self.backbutton1_position = pygame.Rect(28, 28, 61, 53)
        
        #Set back button 2
        self.backbutton2_image = pygame.image.load("images/custom_quiz_lobby_back.jpg")
        self.backbutton2_rect = self.backbutton2_image.get_rect().move(193, 177)

        # Set review custom quiz button
        self.reviewCustomQuiz_rect = pygame.Rect(26, 410, 144, 100)
        pygame.draw.rect(self.screen, (255, 255, 255), self.reviewCustomQuiz_rect)
        
        # Set modify custom quiz button
        self.modifyCustomQuiz_rect = pygame.Rect(32, 518, 139, 98)
        pygame.draw.rect(self.screen, (255, 255, 255), self.modifyCustomQuiz_rect)

        # Set header text
        self.headerText = pygame.font.SysFont('Courier New', 45, True).render("Manage Custom Quiz", True, (247, 230, 82))
        self.headerText_rect = self.headerText.get_rect().move(0, 70)
        self.headerText_rect.centerx = 596

    def changeHeader(self):
        if self.displayReview:
            self.headerText = pygame.font.SysFont('Courier New', 45, True).render("Review Custom Quiz", True, (247, 230, 82))
        elif self.displayModify:
            self.headerText = pygame.font.SysFont('Courier New', 45, True).render("Remove Custom Quiz", True, (247, 230, 82))
        else:
            self.headerText = pygame.font.SysFont('Courier New', 45, True).render("Manage Custom Quiz", True, (247, 230, 82))
        self.headerText_rect = self.headerText.get_rect().move(0, 70)
        self.headerText_rect.centerx = 596
            
    # Student Custom Quiz Lobby
    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)

        # Display Header Text
        self.display_surface.blit(self.headerText, self.headerText_rect)
    
        if (self.displayModify == False and self.displayReview == False):
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
        elif (self.displayReview == True and self.displayModify == False):
            # Display Back Button
            self.display_surface.blit(self.backbutton2_image, self.backbutton2_rect)
            
            if (self.reload == True):
                self.customQuizObjList = []
                self.customQuiz = mysqlConnection.retrieveAllPendingCustomQuiz()
                
                # Create the review Custom Quiz Objects here
                if (len(self.customQuiz) <=0):
                    pass
                else:
                    for i in range(len(self.customQuiz)):
                        self.customQuizObjList.append(teacherReviewCustomQuizObjAsset.TeacherReviewCustomQuizObjAsset(self.user, self.username, self.customQuiz[i][2], self.customQuiz[i][8], i, self.display_surface))    
                self.reload = False
                
            if (len(self.customQuizObjList) > 0):
                for j in self.customQuizObjList:
                    j.display()
        elif (self.displayReview == False and self.displayModify == True):
            # Display Back Button
            self.display_surface.blit(self.backbutton2_image, self.backbutton2_rect)
            
            if (self.reload == True):
                self.customQuizObjList = []
                self.customQuiz = mysqlConnection.retrieveApprovedCustomQuiz()
                
                # Create the review Custom Quiz Objects here
                if (len(self.customQuiz) <=0):
                    pass
                else:
                    for i in range(len(self.customQuiz)):
                        self.customQuizObjList.append(teacherModifyCustomQuizObjAsset.TeacherModifyCustomQuizObjAsset(self.user, self.username, self.customQuiz[i][2], self.customQuiz[i][8], i, self.display_surface))    
                self.reload = False
                
            if (len(self.customQuizObjList) > 0):
                for j in self.customQuizObjList:
                    j.display()
                    
    def action(self):
        for i in self.customQuizObjList:
            i.action()
            if(getattr(i, 'stopRunning')):
                return 10
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            self.displayReview = False
            self.displayModify = False
            self.changeHeader()
            return 0
        if self.backbutton2_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            self.displayReview = False
            self.displayModify = False
            self.changeHeader()
        if self.reviewCustomQuiz_rect.collidepoint(pygame.mouse.get_pos()):
            self.displayReview = True
            self.displayModify = False
            self.changeHeader()
        if self.modifyCustomQuiz_rect.collidepoint(pygame.mouse.get_pos()):
            self.displayReview = False
            self.displayModify = True
            self.changeHeader()
        if (not self.backbutton1_position.collidepoint(pygame.mouse.get_pos())
            or not self.backbutton2_rect.collidepoint(pygame.mouse.get_pos())
            or not self.reviewCustomQuiz_rect.collidepoint(pygame.mouse.get_pos())
            or not self.modifyCustomQuiz_rect.collidepoint(pygame.mouse.get_pos())):
                return 10
    
