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

class Login:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.popup= popup.PopUp(display_surface)
        self.enterkey = False

    def loadAssets(self):
        # Set background
        self.background1_image = pygame.image.load("images\login.jpg")
        self.background1_position = [0,0]

        # Set login button
        self.login_rect = pygame.Rect(460, 612, 309, 64)
        pygame.draw.rect(self.screen, (255, 255, 255), self.login_rect)
        self.login_rect_position = [0,0]

        # Set register button
        self.register_rect = pygame.Rect(810, 709, 69, 25)
        pygame.draw.rect(self.screen, (255, 255, 255), self.register_rect)
        self.register_rect_position = [0,0]

        # Set recover button
        self.recover_rect = pygame.Rect(810, 761, 69, 25)
        pygame.draw.rect(self.screen, (255, 255, 255), self.recover_rect)
        self.recover_rect_position = [0,0]

        #Set user and password input
        self.input_rect = pygame.Rect(566, 480, 309, 179)
        self.username_box1 = InputBox(568, 397, 310, 66)
        self.password_box2 = InputBox(568, 497, 310, 66)
        self.done = False
        self.success = False
        self.registerClicked = False
        self.recoverClicked = False
        self.input_boxes = [self.username_box1, self.password_box2]
        
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
                elif event.type == pygame.KEYDOWN:
                    # If player press enter key, check all fields
                    if event.key == pygame.K_RETURN:
                        self.enterkey = True
                        self.done = self.action()
                    # If player press tab key, switch between the fields
                    elif event.key == pygame.K_TAB:
                        boxswitched = False
                        for i in range(len(self.input_boxes)):
                            if self.input_boxes[i].active and i == len(self.input_boxes)-1:
                                self.input_boxes[i].active = False
                                self.input_boxes[i].color = pygame.Color('lightskyblue3')
                                boxswitched = True
                                break
                            elif self.input_boxes[i].active:
                                self.input_boxes[i].active = False
                                self.input_boxes[i].color = pygame.Color('lightskyblue3')
                                self.input_boxes[i+1].active = True
                                self.input_boxes[i+1].color = pygame.Color('dodgerblue2')
                                boxswitched = True
                                break
                        if boxswitched == False:
                            self.input_boxes[0].active = True
                            self.input_boxes[0].color = pygame.Color('dodgerblue2')
                for box in self.input_boxes:
                    box.handle_event(event)
            
            # Display background
            self.display_surface.blit(self.background1_image, self.background1_position)

            # Display user and password input
            for box in self.input_boxes:
                box.draw(self.screen)
            
            # Refresh Login Page
            pygame.display.update()
            clock.tick(30)
            
    # Login Page Actions
    def action(self):
        if self.login_rect.collidepoint(pygame.mouse.get_pos()) or self.enterkey:
            self.enterkey = False
            username = self.username_box1.retrieveBoxValues()
            password = self.password_box2.retrieveBoxValues()
            #self.input_box1.draw(self.screen)
            #self.input_box2.draw(self.screen)
            if(self.authenticate(username, password)):
                for box in self.input_boxes:
                    box.resetText()
                return True
            else:
                for box in self.input_boxes:
                    box.resetText()
                return False    
            
        # Transition to Register Page
        if self.register_rect.collidepoint(pygame.mouse.get_pos()):
            self.registerClicked = True
            clicksound()
            return True

        # Transition to Recover Page
        if self.recover_rect.collidepoint(pygame.mouse.get_pos()):
            self.recoverClicked = True
            clicksound()
            return True
            
        
    def authenticate(self, username, password):
        user = ""
        foundStudent = False
        
        allStudents = mysqlConnection.retrieveStudentAccountData()
        allTeachers = mysqlConnection.retrieveTeacherAccountData()
        
        for i in allStudents:
            if((username == i[0]) and (password == i[1])):
                foundStudent = True 
                self.username = i[0]
                self.user = "Student"
                self.success = True
                break
        
        if (foundStudent):
            pass
        else:
            for i in allTeachers:
                if((username == i[0]) and (password == i[1])):
                    self.username = i[0]
                    self.user = "Teacher"
                    self.success = True
                    break
           
        if (self.success):
            self.popup.success("Welcome : " + username)
            return True
        else:
            self.popup.fail("Failed to login, Incorrect ID/Password")
            return False
