# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Import SQL Connection 
import mysqlConnection

# Import Taking Custom Quiz UI 
import taking_custom_quiz

# Import Popup
import popup

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class MailboxObjAsset:
    def __init__(self, user, username, notificationMessage, iteration, display_surface):
        self.user = user
        self.username = username
        self.notificationMessage = notificationMessage
        self.iteration = iteration
        self.display_surface = display_surface
        self.stopRunning = False
        self.popup= popup.PopUp(display_surface)
        self.typeOfQuiz = "Challenge"
        self.y_axis = 236
        y_axis_offset = self.iteration * 50
    
        """
        self.storeNotification_position.append(pygame.Rect(223, 236, 785, 89))
        self.storeNotification_position.append(pygame.Rect(223, 324, 785, 84))
        self.storeNotification_position.append(pygame.Rect(223, 411, 785, 64))
        self.storeNotification_position.append(pygame.Rect(223, 480, 785, 60))
        self.storeNotification_position.append(pygame.Rect(223, 545, 785, 69))
        """
        
        # Set Clickable Notification Area
        self.notification_position = pygame.Rect(pygame.Rect(223, y_axis_offset + self.y_axis, 785, 89))
        
        # Set Notfication Text
        self.notificationtext1 = pygame.font.SysFont('Courier New', 30).render(self.notificationMessage, True, (0, 0, 0))
        self.notificationtext1_position = [250,y_axis_offset + self.y_axis + 20]
        
    # Popup Display
    def display(self):

        # Displays Notification
        self.display_surface.blit(self.notificationtext1, self.notificationtext1_position)

        """
        # Wait for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                
                #self.action()
                pass
        """
    
    # Popup Actions
    def action(self):
        if self.notification_position.collidepoint(pygame.mouse.get_pos()):
            print("Clicked Notification")
            challengerUsername = ""
            battleIDToUse = 0
            for i in self.notificationMessage:
                if(i == " "):
                    break
                else:
                    challengerUsername += i
            
            
            quizNameToUse = mysqlConnection.retrievePendingBattleStatus(challengerUsername, self.username)
            
            if(len(quizNameToUse) > 0):
                for i in range(len(quizNameToUse)):
                    if(quizNameToUse[i][6] != None and quizNameToUse[i][7] != None):
                        pass
                    else:
                        battleIDToUse = quizNameToUse[i][0]
                        break
            self.takingQuizUI = taking_custom_quiz.TakingQuizUI(self.user, quizNameToUse[0][2] , self.username, self.display_surface, self.typeOfQuiz)
            self.takingQuizUI.loadAssets()
            self.takingQuizUI.passChallengerUsername(quizNameToUse[0][3])
            self.takingQuizUI.setReplyChallenge(True)
            self.takingQuizUI.setBattleID(battleIDToUse)
            self.takingQuizUI.setNotificationMsg(self.notificationMessage)
            clicksound()
            self.stopRunning = False
            while not self.stopRunning:  
                self.takingQuizUI.display()
                if(getattr(self.takingQuizUI, 'finished')):
                    self.stopRunning = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == MOUSEBUTTONDOWN:
                        self.takingQuizUI.action()
                    pygame.display.update()
            return 14
            
