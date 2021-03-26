# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(0)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class MainMenu:
    def __init__(self, username, user, screen, display_surface):
        self.logout = False
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen

        # Background1 is for the background
        # Popup is for the logout confirmation
        # Buttons 1-6 are function buttons
        # Button 7 is logout button
        # Button 8-10 is popup logout comfirmation button

    # Set main menu for student and teacher respectively
    def loadAssets(self):

        # Set main menu for student and teacher respectively
        if self.user == "Student":
            #Set background for student
            self.background1_image = pygame.image.load("images/student_mainmenu.jpg")
            self.background1_position = [0,0]

            #Set various main menu button for student
            tempimage = pygame.image.load("images/w2.png")
            self.button1_image = tempimage
            self.button2_image = tempimage
            self.button3_image = tempimage
            self.button4_image = tempimage
            self.button5_image = tempimage
            self.button6_image = tempimage

            self.button1_position = self.button1_image.get_rect().move(271, 293)
            self.button2_position = self.button2_image.get_rect().move(581, 351)
            self.button3_position = self.button3_image.get_rect().move(842 , 305)
            self.button4_position = self.button4_image.get_rect().move(290, 636)
            self.button5_position = self.button5_image.get_rect().move(611, 616)
            self.button6_position = self.button6_image.get_rect().move(843, 611)
            
            # Set Username Text
            self.studentUsername = pygame.font.SysFont('Courier New', 40).render(self.username, True, (0, 0, 0))
            self.studentUsername_position = [835,95]
        
            #Set logout button for student
            self.logoutbutton7_image = pygame.image.load("images/w2.png")
            self.logoutbutton7_position = self.logoutbutton7_image.get_rect().move(829, 93)

            #Set logout popup confirmation for student
            self.logoutpopup_image = pygame.image.load("images/w9.png")
            self.button9_image = pygame.image.load("images/w10.png")
            self.button10_image = pygame.image.load("images/w11.png")
            self.button8_image = pygame.image.load("images/w12.png")

            self.logoutpopup_position = [403,326]
            self.button8_position = self.button8_image.get_rect().move(812, 332)
            self.button9_position = self.button9_image.get_rect().move(491, 514)
            self.button10_position = self.button10_image.get_rect().move(691, 514)

            self.gotofriends = False

        elif self.user == "Teacher":
            #Set background for teacher
            self.background1_image = pygame.image.load("images/teacher_mainmenu.jpg")
            self.background1_position = [0,0]

            #Set various main menu button for teacher (needed as actions() checks for these buttons)
            tempimage = pygame.image.load("images/w2.png")
            self.button1_image = tempimage
            self.button2_image = tempimage
            self.button3_image = tempimage
            self.button4_image = tempimage
            self.button5_image = tempimage
            self.button6_image = tempimage

            self.button1_position = self.button1_image.get_rect().move(0, 0)
            self.button2_position = self.button2_image.get_rect().move(0, 0)
            self.button3_position = self.button3_image.get_rect().move(0, 0)
            self.button4_position = self.button4_image.get_rect().move(0, 0)
            self.button5_position = self.button5_image.get_rect().move(0, 0)
            self.button6_position = self.button6_image.get_rect().move(0, 0)
            
            # Set login button
            self.uploadAssignment_rect = pygame.Rect(385, 310, 450, 115)
            pygame.draw.rect(self.screen, (255, 255, 255), self.uploadAssignment_rect)
            self.uploadAssignment_rect_position = [0,0]
        
            # Set Username Text
            self.teacherUsername = pygame.font.SysFont('Courier New', 40).render(self.username, True, (0, 0, 0))
            self.teacherUsername_position = [835,95]

            #Set logout button for teacher
            self.logoutbutton7_image = pygame.image.load("images/teacher_logout.png")
            self.logoutbutton7_position = self.logoutbutton7_image.get_rect().move(715, 168)

            
            #Set logout popup confirmation for teacher
            self.logoutpopup_image = pygame.image.load("images/w9.png")
            self.button9_image = pygame.image.load("images/w10.png")
            self.button10_image = pygame.image.load("images/w11.png")
            self.button8_image = pygame.image.load("images/w12.png")

            self.logoutpopup_position = [403,326]
            self.button8_position = self.button8_image.get_rect().move(812, 332)
            self.button9_position = self.button9_image.get_rect().move(491, 514)
            self.button10_position = self.button10_image.get_rect().move(691, 514)
            
    # Display main menu for student and teacher respectively
    def display(self):

        #Main Menu Display for Student
        if self.user == "Student":
            #Display background for student
            self.display_surface.blit(self.background1_image, self.background1_position)

            #Display various main menu button for student
            self.display_surface.blit(self.button1_image, self.button1_position)
            self.display_surface.blit(self.button2_image, self.button2_position)
            self.display_surface.blit(self.button3_image, self.button3_position)
            self.display_surface.blit(self.button4_image, self.button4_position)
            self.display_surface.blit(self.button5_image, self.button5_position)
            self.display_surface.blit(self.button6_image, self.button6_position)
            
            # Hide above buttons 
            self.button1_image.set_alpha(0)
            self.button2_image.set_alpha(0)
            self.button3_image.set_alpha(0)
            self.button4_image.set_alpha(0)
            self.button5_image.set_alpha(0)
            self.button6_image.set_alpha(0)

            # Display Student Username
            self.screen.blit(self.studentUsername, self.studentUsername_position)
        
            #Display logout button for student
            self.display_surface.blit(self.logoutbutton7_image, self.logoutbutton7_position)
            # Hide logout buttons
            self.logoutbutton7_image.set_alpha(0)

            #Display logout popup confirmation for student
            if self.logout:
                self.display_surface.blit(self.logoutpopup_image, self.logoutpopup_position)
                self.display_surface.blit(self.button8_image, self.button8_position)
                self.display_surface.blit(self.button9_image, self.button9_position)
                self.display_surface.blit(self.button10_image, self.button10_position)
            
        #Main Menu Display for Teacher
        if self.user == "Teacher":
            #Display background for teacher
            self.display_surface.blit(self.background1_image, self.background1_position)

            #Display various main menu button for teacher
            self.display_surface.blit(self.button1_image, self.button1_position)
            self.display_surface.blit(self.button2_image, self.button2_position)
            self.display_surface.blit(self.button3_image, self.button3_position)
            self.display_surface.blit(self.button4_image, self.button4_position)
            self.display_surface.blit(self.button5_image, self.button5_position)
            self.display_surface.blit(self.button6_image, self.button6_position)
            
            # Hide above buttons 
            self.button1_image.set_alpha(0)
            self.button2_image.set_alpha(0)
            self.button3_image.set_alpha(0)
            self.button4_image.set_alpha(0)
            self.button5_image.set_alpha(0)
            self.button6_image.set_alpha(0)
     
            # Display Teacher Username
            self.screen.blit(self.teacherUsername, self.teacherUsername_position)

            #Display logout button for student
            self.display_surface.blit(self.logoutbutton7_image, self.logoutbutton7_position)
            # Hide logout buttons
            self.logoutbutton7_image.set_alpha(0)

            #Display logout popup confirmation for student
            if self.logout:
                self.display_surface.blit(self.logoutpopup_image, self.logoutpopup_position)
                self.display_surface.blit(self.button8_image, self.button8_position)
                self.display_surface.blit(self.button9_image, self.button9_position)
                self.display_surface.blit(self.button10_image, self.button10_position)
            
    # Main Menu Actions
    def action(self):
        if self.logout == False:
            if self.button1_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("World Select Button Pressed!")
                    clicksound()
                    return 1
                elif self.user == "Teacher":
                    print("Data Analytics Button Pressed!")
                    clicksound()
                    return 0
            elif self.button2_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("Friends Pressed!")
                    clicksound()
                    return 5
                elif self.user == "Teacher":
                    print("Modify Quiz Button Pressed!")
                    clicksound()
                    return 0
            elif self.button3_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("View Leaderboard Pressed!")
                    clicksound()
                    return 4
                elif self.user == "Teacher":
                    print("Remove Quiz Button Pressed!")
                    clicksound()
                    return 0
            elif self.button4_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("View Profile Button Pressed!")
                    clicksound()
                    return 0
                elif self.user == "Teacher":
                    print("Review Quiz Button Pressed!")
                    clicksound()
                    return 0
            elif self.button5_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("Custom Quiz Button Pressed!")
                    clicksound()
                    return 8
                elif self.user == "Teacher":
                    print("Upload Assignment Button Pressed!")
                    clicksound()
                    return 0
            elif self.user == "Student" and self.button6_position.collidepoint(pygame.mouse.get_pos()):
                print("Problem Community Pressed!")
                clicksound()
                return 0
            elif self.logoutbutton7_position.collidepoint(pygame.mouse.get_pos()):
                print("Log Out Button Pressed!")
                clicksound()
                self.logout = True
                return 0
            elif self.uploadAssignment_rect.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Teacher":
                    print("Upload assigment Pressed!")
                    clicksound()
                    return 7
            else:
                return 0
        elif self.logout:
            if self.button8_position.collidepoint(pygame.mouse.get_pos()):
                print("Cancel Button on Pop Up Pressed!")
                clicksound()
                self.logout = False
                return 0
            elif self.button9_position.collidepoint(pygame.mouse.get_pos()):
                print("Yes Button on Pop Up Pressed!")
                clicksound()
                return 2
            elif self.button10_position.collidepoint(pygame.mouse.get_pos()):
                print("No Button on Pop Up Pressed!")
                clicksound()
                self.logout = False
                return 0
            else:
                return 0