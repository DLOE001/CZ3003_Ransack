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

        #Background
        self.background1_image = None
        self.background1_position = None

        #popup
        self.popup_image = None
        self.popup_position = None

        #Buttons
        self.button1_image = None
        self.button1_position = None
        self.button2_image = None
        self.button2_position = None
        self.button3_image = None
        self.button3_position = None
        self.button4_image = None
        self.button4_position = None
        self.button5_image = None
        self.button5_position = None
        self.button6_image = None
        self.button6_position = None

        self.button7_image = None
        self.button7_position = None
        self.button8_image = None
        self.button8_position = None
        self.button9_image = None
        self.button9_position = None
        self.button10_image = None
        self.button10_position = None
        self.button11_image = None
        self.button11_position = None
    
    def loadAssets(self):

        # Graphics
        self.background1_image = pygame.image.load("images/student_mainmenu.jpg")

        self.button7_image = pygame.image.load("images/w8.png")

        #logout comfirmation
        self.popup_image = pygame.image.load("images/w9.png")
        self.button9_image = pygame.image.load("images/w10.png")
        self.button10_image = pygame.image.load("images/w11.png")
        self.button8_image = pygame.image.load("images/w12.png")

        if self.user == "Student":
            tempimage = pygame.image.load("images/w2.png")
            self.button1_image = tempimage
            self.button2_image = tempimage
            self.button3_image = tempimage
            self.button4_image = tempimage
            self.button5_image = tempimage
            self.button6_image = tempimage

        elif self.user == "Teacher":
            self.button1_image = pygame.image.load("images/w13.png")
            self.button2_image = pygame.image.load("images/w14.png")
            self.button3_image = pygame.image.load("images/w15.png")
            self.button4_image = pygame.image.load("images/w16.png")
            self.button5_image = pygame.image.load("images/w17.png")

        # Graphic Positions
        self.background1_position = [0,0]

        self.popup_position = [403,326]

        self.button1_position = self.button1_image.get_rect().move(271, 293)
        self.button2_position = self.button2_image.get_rect().move(581, 351)
        self.button3_position = self.button3_image.get_rect().move(842 , 305)
        self.button4_position = self.button4_image.get_rect().move(290, 636)
        self.button5_position = self.button5_image.get_rect().move(611, 616)
        if self.user == "Student":
            self.button6_position = self.button6_image.get_rect().move(843, 611)
        self.button7_position = self.button7_image.get_rect().move(940, 237)
        self.button8_position = self.button8_image.get_rect().move(812, 332)
        self.button9_position = self.button9_image.get_rect().move(491, 514)
        self.button10_position = self.button10_image.get_rect().move(691, 514)

    # Main Menu Display
    def display(self):
        # Copy of background image
        self.display_surface.blit(self.background1_image, self.background1_position)

        
        # Copy of menu buttons
        self.display_surface.blit(self.button1_image, self.button1_position)
        self.display_surface.blit(self.button2_image, self.button2_position)
        self.display_surface.blit(self.button3_image, self.button3_position)
        self.display_surface.blit(self.button4_image, self.button4_position)
        self.display_surface.blit(self.button5_image, self.button5_position)
        if self.user == "Student":
            self.display_surface.blit(self.button6_image, self.button6_position)
        self.display_surface.blit(self.button7_image, self.button7_position)
        if self.logout:
            self.display_surface.blit(self.popup_image, self.popup_position)
            self.display_surface.blit(self.button8_image, self.button8_position)
            self.display_surface.blit(self.button9_image, self.button9_position)
            self.display_surface.blit(self.button10_image, self.button10_position)

        # Hide all buttons 
        self.button1_image.set_alpha(0)
        self.button2_image.set_alpha(0)
        self.button3_image.set_alpha(0)
        self.button4_image.set_alpha(0)
        self.button5_image.set_alpha(0)
        self.button6_image.set_alpha(0)

     
    '''
        # Mouseover Animation
        if self.logout == False:
            #mouseover(self.button1_image, self.button1_position)
            mouseover(self.button2_image, self.button2_position)
            mouseover(self.button3_image, self.button3_position)
            mouseover(self.button4_image, self.button4_position)
            mouseover(self.button5_image, self.button5_position)
            if self.user == "Student":
                mouseover(self.button6_image, self.button6_position)
            mouseover(self.button7_image, self.button7_position)
        elif self.logout:
            mouseover(self.button8_image, self.button8_position)
            mouseover(self.button9_image, self.button9_position)
            mouseover(self.button10_image, self.button10_position)
        mouseover(self.button11_image, self.button11_position)
    '''

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
                    return 0
                elif self.user == "Teacher":
                    print("Modify Quiz Button Pressed!")
                    clicksound()
                    return 0
            elif self.button3_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("View Leaderboard Pressed!")
                    clicksound()
                    return 0
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
                    print("Issue Challenges Button Pressed!")
                    clicksound()
                    return 0
                elif self.user == "Teacher":
                    print("Upload Assignment Button Pressed!")
                    clicksound()
                    return 0
            elif self.user == "Student" and self.button6_position.collidepoint(pygame.mouse.get_pos()):
                print("Problem Community Pressed!")
                clicksound()
                return 0
            elif self.button7_position.collidepoint(pygame.mouse.get_pos()):
                print("Log Out Button Pressed!")
                clicksound()
                self.logout = True
                return 
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
                return -1
            elif self.button10_position.collidepoint(pygame.mouse.get_pos()):
                print("No Button on Pop Up Pressed!")
                clicksound()
                self.logout = False
                return 0
            else:
                return 0
