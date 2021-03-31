# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Imports Text Box
from friendinputBox import InputBox

# Import SQL Connection 
import mysqlConnection

# Import Popup
import popup

# Import Popupyesno
import popupyesno

# Import Taking Custom Quiz UI 
import taking_custom_quiz

# Import SQL Connection 
import mysqlConnection

# Import Random
import random

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class Friends:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.popup= popup.PopUp(display_surface)
        self.popupyesno = popupyesno.PopUpYesNo(display_surface)
        self.typeOfQuiz = "Challenge"
        self.stopRunning = False
        self.usernameSelected = ""
        
    def loadAssets(self):
        
        # Set background
        self.background1_image = pygame.image.load("images/friends.jpg")
        self.background1_position = [0,0]

        # Set back button 
        self.backbutton1_position = pygame.Rect(125, 96, 63, 55)
        
        # Set challenge friend button 
        self.challengeFriend_position = pygame.Rect(1022, 179, 72, 49)
        
        # Set friends input
        self.friendsinput_box1 = InputBox(228, 667, 205, 35)
        self.done = False
        self.success = False
        self.input_boxes = [self.friendsinput_box1]

        # Set add friend button
        self.addfriend_rect = pygame.Rect(143, 735, 285, 46)
        pygame.draw.rect(self.screen, (255, 255, 255), self.addfriend_rect)
        self.addfriend_rect_position = [0,0]

        self.usernameSelected = ""
    def display(self):

        clock = pygame.time.Clock()        
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    self.done = self.action()
                for box in self.input_boxes:
                    box.handle_event(event)
                    
            # Display background
            self.display_surface.blit(self.background1_image, self.background1_position)

            # Display friend input
            self.friendsinput_box1.draw(self.screen)

            # Display current friend list
            self.displayfriendlist()

            # Refresh Page on key press
            pygame.display.update()
            clock.tick(30)

    def action(self):
        if self.challengeFriend_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            hasPendingBattle = mysqlConnection.retrievePendingBattleStatus(self.username, self.usernameSelected)
            ableToBattle = False
            if(len(hasPendingBattle) > 0):
                for i in range(len(hasPendingBattle)):
                    if(hasPendingBattle[i][6] != None and hasPendingBattle[i][7] != None):
                        pass
                    else:
                        if (hasPendingBattle[i][6] == None and hasPendingBattle[i][7] == None):
                            ableToBattle = False
                            break
                    ableToBattle = True
            else:
                ableToBattle = True
            if(ableToBattle == False):
                self.popup.fail("Failed to initiate battle, already have an existing battle with " + self.usernameSelected)
            else:
                if self.popupyesno.confirmation("Quiz have to be taken before challenging the player. Continue?"):
                    self.quizIndexToUse = 0
                    self.storeChallengeQues = mysqlConnection.retrieveChallengeQuizData()
                    if (len(self.storeChallengeQues) > 0):
                        self.quizIndexToUse = random.randint(0, len(self.storeChallengeQues)-1)
                    
                    # Create the challenge quiz UI
                    self.takingQuizUI = taking_custom_quiz.TakingQuizUI(self.user, self.storeChallengeQues[self.quizIndexToUse][1], self.username, self.display_surface, self.typeOfQuiz)
                    self.takingQuizUI.loadAssets()
                    self.takingQuizUI.passSelectedUsername(self.usernameSelected)
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
            return False
        
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            print("Back Button Pressed!")
            clicksound()
            return True

        if self.addfriend_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            friendname = self.friendsinput_box1.retrieveBoxValues()
            # Check if friendname is empty 
            if not friendname:
                self.popup.fail("Friend name is empty!")
                print("Empty")
            else:
                # Retrieve current friend list
                newfriendlist = mysqlConnection.retrieveFriendList(self.username)

                # Add new friendname
                newfriendlist.append(friendname)

                # Convert list to string so that SQL can accept
                newfriendstring = ''
                for i in newfriendlist:
                    newfriendstring = newfriendstring + i + ', '

                # Remove last two index of string as not needed
                newfriendstring = newfriendstring[:-2]

                print(newfriendstring)

                # Proceed to update which will be reflect in SQL and system
                mysqlConnection.updateFriendList(self.username, newfriendstring)

                self.popup.success("Friend added!")


    def displayfriendlist(self):
        friendlist = mysqlConnection.retrieveFriendList(self.username)
        index = 0

        self.usernameSelected = friendlist[0]
        
        # Set name of current chat
        self.chat_text = pygame.font.SysFont('Courier New', 40).render(friendlist[0], True, (0, 0, 0))
        self.chat_text_position = [490 ,193]

        self.screen.blit(self.chat_text, self.chat_text_position)


        for v in friendlist:
            # For each friend, set and display the names accordingly
            self.friend_text1 = pygame.font.SysFont('Courier New', 50).render(v, True, (0, 0, 0))

            # Each names have a interval of y = 112
            self.friend_text1_position = [170 ,214 + index*112]

            self.screen.blit(self.friend_text1, self.friend_text1_position)
            index = index + 1





