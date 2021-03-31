# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Import SQL Connection 
import mysqlConnection

# Import Mailbox Asset
import mailboxObjAsset

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class Mailbox:
    def __init__(self, username, user, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.reload = True
        # Set background
        self.background1_image = pygame.image.load("images/mailbox.jpg")
        self.background1_position = [0,0]

        # Set back button rectangle 
        self.backbutton1_rect = pygame.Rect(28, 28, 61, 53)
        
        
    def display(self):
        # Display background
        self.display_surface.blit(self.background1_image, self.background1_position)
        self.notificationObjList = []
        self.notification = mysqlConnection.retrieveNotification(self.username)
        
        if (self.reload == True):
            if (len(self.notification) <= 0):
                pass
            else:
                for i in range(len(self.notification)):
                    self.notificationObjList.append(mailboxObjAsset.MailboxObjAsset(self.user, self.username, self.notification[i][0], i, self.display_surface))
            self.reload = False
                
        if (len(self.notificationObjList) > 0):
            for j in self.notificationObjList:
                j.display()
    # On click actions of UI components in the leaderboard page         
    def action(self):
        for i in self.notificationObjList:
            i.action()
            if(getattr(i, 'stopRunning')):
                return 14
        if self.backbutton1_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return 0
        else:
            return 14
