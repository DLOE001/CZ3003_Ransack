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

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class Login:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen

        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button
    
    # Set login 
    def loadAssets(self):
        
        # Set background
        self.background1_image = pygame.image.load("images\login.jpg")
        self.background1_position = [0,0]

        # Set login button
        self.login_rect = pygame.Rect(460, 714, 309, 64)
        pygame.draw.rect(self.screen, (255, 255, 255), self.login_rect)

        self.login_rect_position = [0,0]

        # Set register button
        self.register_rect = pygame.Rect(517, 639, 69, 25)
        pygame.draw.rect(self.screen, (255, 255, 255), self.login_rect)
        self.register_rect_position = [0,0]

        #Set user and password input
        self.input_rect = pygame.Rect(566, 480, 309, 179)
        self.input_box1 = InputBox(568, 397, 309, 66)
        self.input_box2 = InputBox(567, 497, 309, 66)
        self.done = False
        self.success = False
        self.input_boxes = [self.input_box1, self.input_box2]
        

    # Login Display
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
                    
            #for box in self.input_boxes:
                #box.update()
            
            # Display background
            self.display_surface.blit(self.background1_image, self.background1_position)

            # Display user and password input
            self.input_box1.draw(self.screen)
            self.input_box2.draw(self.screen)
            
            # Copy of username rectangle
            #pygame.draw.rect(self.screen, (255, 255, 255), self.login_rect)
        

            pygame.display.update()
            clock.tick(30)
            
    # Login Page Actions
    def action(self):
        if self.login_rect.collidepoint(pygame.mouse.get_pos()):
            #self.input_box1.draw(self.screen)
            #self.input_box2.draw(self.screen)
            if(self.authenticate(self.input_box1.retrieveBoxValues(), self.input_box2.retrieveBoxValues())):
                return True
            else:
                self.input_box1.resetText()
                self.input_box2.resetText()
                return False

        if self.register_rect.collidepoint(pygame.mouse.get_pos()):
            print("Register Button Pressed!")
            clicksound()
            return True
    """
    def onClickLogin(self):
        if self.login_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print(self.input_box1.retrieveBoxValues())
            print(self.input_box2.retrieveBoxValues())
            self.authenticate(self.input_box1.retrieveBoxValues(), self.input_box2.retrieveBoxValues())
            self.input_box1.resetText()
            self.input_box2.resetText()
    """       
       
    def authenticate(self, username, password):
        user = ""
        foundStudent = False
        
        allStudents = mysqlConnection.retrieveStudentAccountData()
        allTeachers = mysqlConnection.retrieveTeacherAccountData()
        
        for i in allStudents:
            if((username == i[0]) and (password == i[1])):
                foundStudent = True 
                user = "Student"
                self.success = True
                break
        
        if (foundStudent):
            pass
        else:
            for i in allTeachers:
                if((username == i[0]) and (password == i[1])):
                    user = "Teacher"
                    self.success = True
                    break
           
        if (self.success):
            print("Success Login. Welcome : " + user + " " + username + "\n")
            return True
        else:
            print("Failed to login, Incorrect ID/Password \n")
            return False