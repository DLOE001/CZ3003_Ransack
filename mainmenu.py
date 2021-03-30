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

        #Set logout popup confirmation for teacher
        self.logoutpopup_image = pygame.image.load("images/w9.png")
        self.button9_image = pygame.image.load("images/w10.png")
        self.button10_image = pygame.image.load("images/w11.png")
        self.button8_image = pygame.image.load("images/w12.png")

        self.logoutpopup_position = [403,326]
        self.button8_position = self.button8_image.get_rect().move(812, 332)
        self.button9_position = self.button9_image.get_rect().move(491, 514)
        self.button10_position = self.button10_image.get_rect().move(691, 514)
        
        # Set main menu for student and teacher respectively
        if self.user == "Student":
            #Set background for student
            self.background1_image = pygame.image.load("images/student_mainmenu.jpg")
            self.background1_position = [0,0]

            # Set World Select Button
            self.button1_position = pygame.Rect(208, 236, 275, 312)
            
            # Set Friends Button
            self.button2_position = pygame.Rect(509, 234, 273, 301)
            
            # Set Leaderboard Button
            self.button3_position = pygame.Rect(795, 250, 189, 200)
            
            # Set Profile Button
            self.button4_position = pygame.Rect(241, 616, 243, 144)
            
            # Set Custom Quiz Button
            self.button5_position = pygame.Rect(534, 568, 272, 210)
            
            # Problem Community Button
            self.button6_position = pygame.Rect(811, 541, 203, 248)
            
            # Set mailbox button
            self.button11_position = pygame.Rect(1049, 23, 140, 153)
            
            # Set Username Text
            self.studentUsername = pygame.font.SysFont('Courier New', 40).render(self.username, True, (0, 0, 0))
            self.studentUsername_position = [835,95]
        
            #Set logout button for student
            self.logoutbutton7_position = pygame.Rect(763, 76, 269, 130)

            self.gotofriends = False

        elif self.user == "Teacher":
            #Set background for teacher
            self.background1_image = pygame.image.load("images/teacher_mainmenu.jpg")
            self.background1_position = [0,0]
            
            # Set upload assignment button
            self.uploadAssignment_rect = pygame.Rect(387, 304, 450, 82)
        
            # Set custom quiz managemnet button
            self.customQuizManagement_rect = pygame.Rect(387, 434, 450, 82)

            # Set summary report button
            self.generateSummaryReport_rect = pygame.Rect(387, 690, 450, 82)

            # Set class management button
            self.classManagement_rect = pygame.Rect(387, 565, 450, 82)
            
            # Set Username Text
            self.teacherUsername = pygame.font.SysFont('Courier New', 40).render(self.username, True, (0, 0, 0))
            self.teacherUsername_position = [835,95]

            #Set logout button for teacher
            self.logoutbutton7_position = pygame.Rect(716, 168, 392, 61)
            
    # Display main menu for student and teacher respectively
    def display(self):

        #Main Menu Display for Student
        if self.user == "Student":
            #Display background for student
            self.display_surface.blit(self.background1_image, self.background1_position)
            
            # Display Student Username
            self.screen.blit(self.studentUsername, self.studentUsername_position)
            
        #Main Menu Display for Teacher
        elif self.user == "Teacher":
            #Display background for teacher
            self.display_surface.blit(self.background1_image, self.background1_position)
            
            # Display Teacher Username
            self.screen.blit(self.teacherUsername, self.teacherUsername_position)

        #Display logout popup confirmation
        if self.logout:
            self.display_surface.blit(self.logoutpopup_image, self.logoutpopup_position)
            self.display_surface.blit(self.button8_image, self.button8_position)
            self.display_surface.blit(self.button9_image, self.button9_position)
            self.display_surface.blit(self.button10_image, self.button10_position)
            
    # Main Menu Actions
    def action(self):
        if self.logout == False:
            if self.logoutbutton7_position.collidepoint(pygame.mouse.get_pos()):
                print("Log Out Button Pressed!")
                clicksound()
                self.logout = True
                return 0
            elif self.user == "Student":
                if self.button1_position.collidepoint(pygame.mouse.get_pos()):
                    print("World Select Button Pressed!")
                    clicksound()
                    return 1
                elif self.button2_position.collidepoint(pygame.mouse.get_pos()):
                    print("Friends Pressed!")
                    clicksound()
                    return 5
                elif self.button3_position.collidepoint(pygame.mouse.get_pos()):
                    print("View Leaderboard Pressed!")
                    clicksound()
                    return 4
                elif self.button4_position.collidepoint(pygame.mouse.get_pos()):
                    print("View Profile Button Pressed!")
                    clicksound()
                    return 13
                elif self.button5_position.collidepoint(pygame.mouse.get_pos()):
                    print("Custom Quiz Button Pressed!")
                    clicksound()
                    return 8
                elif self.button6_position.collidepoint(pygame.mouse.get_pos()):
                    print("Problem Community Pressed!")
                    clicksound()
                    return 0
                elif self.button11_position.collidepoint(pygame.mouse.get_pos()):
                        print("Mailbox pressed")
                        clicksound()
                        return 0
            elif self.user == "Teacher":
                if self.uploadAssignment_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Upload Assigment Pressed!")
                    clicksound()
                    return 7
                elif  self.customQuizManagement_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Custom Quiz management Pressed!")
                    clicksound()
                    return 10
                elif  self.generateSummaryReport_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Generate Summary Report Pressed!")
                    clicksound()
                    return 11
                elif  self.classManagement_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Class Management Pressed!")
                    clicksound()
                    return 12
                else:
                    return 0
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
