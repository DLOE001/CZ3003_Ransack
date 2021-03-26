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

class Register:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.successfulRegister = False
        self.popup= popup.PopUp(display_surface)
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        self.backToLogin = False

        # Set background
        self.background1_image = pygame.image.load("images/register.jpg")
        self.background1_position = [0,0]
        
        # Set back button
        self.backbutton3_image = pygame.image.load("images/w2.png")
        self.backbutton3_position = self.backbutton3_image.get_rect().move(275, 260)
        
        # Hide Buttons
        self.backbutton3_image.set_alpha(0)
        
        # Set register button
        self.register_rect = pygame.Rect(460, 714, 309, 63)
        pygame.draw.rect(self.screen, (255, 255, 255), self.register_rect)
        self.register_rect_position = [0,0]
        
        # Set the fields for user to key in
        self.username_box1 = InputBox(557, 359, 309, 64)
        self.email_box2 = InputBox(556, 470, 309, 66)
        self.password_box3 = InputBox(556, 585, 309, 65)

        self.done = False
        self.errorMessage = ""
        self.successMessage = "Successfully Registered Account"
        self.input_boxes = [self.username_box1, self.email_box2, self.password_box3]

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

            # Set back button
            self.display_surface.blit(self.backbutton3_image, self.backbutton3_position)

            # Display user, email and password input
            for box in self.input_boxes:
                box.draw(self.screen)
        
            # Refresh Register Page on key press
            pygame.display.update()
            clock.tick(30)
            
    # Register Page Actions
    def action(self):
        # Register button is selected
        if self.register_rect.collidepoint(pygame.mouse.get_pos()):
            username = self.username_box1.retrieveBoxValues()
            email = self.email_box2.retrieveBoxValues()
            password = self.password_box3.retrieveBoxValues()
            if(self.checkInputFields(username, password, email)):
                mysqlConnection.createStudentAccount(username, password, email)
                self.successfulRegister = True
                for box in self.input_boxes:
                    box.resetText()
                self.popup.success(self.successMessage)
                return True
            else:
                self.popup.fail(self.errorMessage)
                for box in self.input_boxes:
                    box.resetText()
                return False
         
        # Back button is selected
        if self.backbutton3_position.collidepoint(pygame.mouse.get_pos()):
            self.backToLogin = True
            print("Back Button Pressed!")
            clicksound()
            return True
    
    # Method to check whether input fields have been properly filled 
    def checkInputFields(self, username, password, email):
        passCheck = False
        self.errorMessage = ""
        if(len(username) <= 0 or len(password) <= 0 or len(email) <=0):
            if(len(username) <= 0):
                if(len(self.errorMessage) <= 0):
                    self.errorMessage = "Username field not filled\n"
                else:
                    self.errorMessage += "Username field not filled\n"
            if(len(password) <= 0):
                if(len(self.errorMessage) <= 0):
                    self.errorMessage = "Password field not filled\n"
                else:
                    self.errorMessage += "Password field not filled\n"
            if(len(email) <= 0):
                if(len(self.errorMessage) <= 0):
                    self.errorMessage = "Email field not filled\n"
                else:
                    self.errorMessage += "Email field not filled\n"
        else:
            # Check for duplicate username
            duplicatedUsername = False
            foundDuplicate = False
            allStudents = mysqlConnection.retrieveStudentAccountData()
            allTeachers = mysqlConnection.retrieveTeacherAccountData()
            
            for i in allStudents:
                if(username == i[0]):
                    duplicatedUsername = True
                    foundDuplicate = True
                    break
            
            if (foundDuplicate):
                pass
            else:
                for i in allTeachers:
                    if(username == i[0]):
                        duplicatedUsername = True
                        break
            if(duplicatedUsername):
                if(len(self.errorMessage) <= 0):
                    self.errorMessage = username + " is already taken\n"
                else:
                    self.errorMessage += username + " is already taken\n" 
            else:
                passCheck = True
        return passCheck
        
        
        