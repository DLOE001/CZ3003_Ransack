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
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class Recover:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.popup= popup.PopUp(display_surface)
        self.successfulRecover = False
        self.emptyFields = False
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        self.backToLogin = False

        # Set background
        self.background1_image = pygame.image.load("images/recover.jpg")
        self.background1_position = [0,0]
        
        # Set back button
        self.backbutton3_position = pygame.Rect(320, 302, 67, 58)
        
        # Set recover button
        self.recover_rect = pygame.Rect(464, 723, 309, 63)
        self.recover_rect_position = [0,0]
        
        # Set the fields for user to key in
        self.username_box1 = InputBox(569, 382, 309, 64)
        self.email_box2 = InputBox(569, 495, 309, 66)

        self.done = False
        self.errorMessage = ""
        self.successMessage = ""
        self.input_boxes = [self.username_box1, self.email_box2]

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

            # Display user, email and password input
            for box in self.input_boxes:
                box.draw(self.screen)
        
            # Refresh Register Page on key press
            pygame.display.update()
            clock.tick(30)
            
    # Register Page Actions
    def action(self):
        # Recover button is selected
        if self.recover_rect.collidepoint(pygame.mouse.get_pos()):
            username = self.username_box1.retrieveBoxValues()
            email = self.email_box2.retrieveBoxValues()
            if(self.checkInputFields(username, email)):
                self.successfulRecover = True
                self.popup.success(self.successMessage)
                for box in self.input_boxes:
                    box.resetText()
                return True
            else:
                self.popup.fail(self.errorMessage)
                if self.emptyFields == False:
                    for box in self.input_boxes:
                        box.resetText()
                return False
         
        # Back button is selected
        if self.backbutton3_position.collidepoint(pygame.mouse.get_pos()):
            self.backToLogin = True
            for box in self.input_boxes:
                box.resetText()
            print("Back Button Pressed!")
            clicksound()
            return True
    
    # Method to check whether input fields have been properly filled 
    def checkInputFields(self, username, email):
        passCheck = False
        self.emptyFields = False
        self.errorMessage = ""
        # Check if username or email field is empty
        if(len(username) <= 0 or len(email) <=0):
            if(len(username) <= 0 and len(email) <=0):
                self.errorMessage = "Both username and email fields not filled"
            elif(len(username) <= 0):
                    self.errorMessage = "Username field not filled"
            elif(len(email) <= 0):
                    self.errorMessage = "Email field not filled"
            self.emptyFields = True
        else:
            # Check if username exists
            inputMatch = False
            allStudents = mysqlConnection.retrieveStudentAccountData()
            allTeachers = mysqlConnection.retrieveTeacherAccountData()
            
            for i in allStudents:
                if username == i[0]:
                    if email == i[2]:
                        inputMatch = True
                        break
                    
            if inputMatch == False:
                for i in allTeachers:
                    if username == i[0]:
                        if email == i[2]:
                            inputMatch = True
                            break

            if inputMatch == False:
                self.errorMessage = "Invalid Username or Email"
            else:
                self.successMessage = "Recovery Email has been sent to: " + email
                passCheck = True
        return passCheck
        
        
        
