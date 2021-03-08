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
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class MainMenu:
    def __init__(self, username, user, screen, display_surface):
        self.logout = False
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen

        # Text1 is to display page title
        # Text2 is to display username and user type
        # Background1 is for the header
        # Background2 is for the border
        # Popup is for the logout confirmation
        # Buttons 1-6 are function buttons
        # Button 7 is logout button
        # Button 8 is popup cancel button
        # Button 9 is popup yes button
        # Button 10 is popup no button
        # Button 11 is for Query button
        #Texts
        self.text1 = None
        self.text1_position = None
        self.text2 = None
        self.text2_position = None
        #Background
        self.background1_image = None
        self.background1_position = None
        self.background2_image = None
        self.background2_position = None
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
        # Text
        self.text1 = pygame.font.SysFont('Broadway', 75).render("Main Menu", True, (0, 0, 0))
        self.text2 = pygame.font.SysFont('Broadway', 19).render('Welcome, ' + self.username +"("+ self.user +")", True, (0, 0, 0))

        # Test Positions
        self.text1_position = [394,8]
        self.text2_position = [353,255]

        # Graphics
        self.background1_image = pygame.image.load("images\w1.png")
        self.background2_image = pygame.image.load("images\w19.png")
        self.popup_image = pygame.image.load("images\w9.png")
        
        if self.user == "Student":
            self.button1_image = pygame.image.load("images\w2.png")
            self.button2_image = pygame.image.load("images\w3.png")
            self.button3_image = pygame.image.load("images\w4.png")
            self.button4_image = pygame.image.load("images\w5.png")
            self.button5_image = pygame.image.load("images\w6.png")
            self.button6_image = pygame.image.load("images\w7.png")
        elif self.user == "Teacher":
            self.button1_image = pygame.image.load("images\w13.png")
            self.button2_image = pygame.image.load("images\w14.png")
            self.button3_image = pygame.image.load("images\w15.png")
            self.button4_image = pygame.image.load("images\w16.png")
            self.button5_image = pygame.image.load("images\w17.png")
        self.button7_image = pygame.image.load("images\w8.png")
        self.button8_image = pygame.image.load("images\w12.png")
        self.button9_image = pygame.image.load("images\w10.png")
        self.button10_image = pygame.image.load("images\w11.png")
        self.button11_image = pygame.image.load("images\w20.png")

        # Graphic Positions
        self.background1_position = [0,0]
        self.background2_position = [262,251]
        self.popup_position = [403,326]
     
        self.button1_position = self.button1_image.get_rect().move(360, 324)
        self.button2_position = self.button2_image.get_rect().move(569, 324)
        self.button3_position = self.button3_image.get_rect().move(770, 324)
        self.button4_position = self.button4_image.get_rect().move(360, 497)
        self.button5_position = self.button5_image.get_rect().move(569, 497)
        if self.user == "Student":
            self.button6_position = self.button6_image.get_rect().move(770, 497)
        self.button7_position = self.button7_image.get_rect().move(818, 255)
        self.button8_position = self.button8_image.get_rect().move(812, 332)
        self.button9_position = self.button9_image.get_rect().move(491, 514)
        self.button10_position = self.button10_image.get_rect().move(691, 514)
        self.button11_position = self.button11_image.get_rect().move(1112, 13)

    # Main Menu Display
    def display(self):
        # Copy of background image
        self.display_surface.blit(self.background1_image, self.background1_position)
        self.display_surface.blit(self.background2_image, self.background2_position)

        #Copy text
        self.screen.blit(self.text1, self.text1_position)
        self.screen.blit(self.text2, self.text2_position)
        
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
        self.display_surface.blit(self.button11_image, self.button11_position)
        # Mouseover Animation
        if self.logout == False:
            mouseover(self.button1_image, self.button1_position)
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
                    print("Create Custom Quiz Button Pressed!")
                    clicksound()
                    return 0
                elif self.user == "Teacher":
                    print("Modify Quiz Button Pressed!")
                    clicksound()
                    return 0
            elif self.button3_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("View Profile Button Pressed!")
                    clicksound()
                    return 0
                elif self.user == "Teacher":
                    print("Remove Quiz Button Pressed!")
                    clicksound()
                    return 0
            elif self.button4_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("View Leaderboard Button Pressed!")
                    clicksound()
                    return 0
                elif self.user == "Teacher":
                    print("Review Quiz Button Pressed!")
                    clicksound()
                    return 0
            elif self.button5_position.collidepoint(pygame.mouse.get_pos()):
                if self.user == "Student":
                    print("Issue Challenge Button Pressed!")
                    clicksound()
                    return 0
                elif self.user == "Teacher":
                    print("Upload Assignment Button Pressed!")
                    clicksound()
                    return 0
            elif self.user == "Student" and self.button6_position.collidepoint(pygame.mouse.get_pos()):
                print("Friend List Button Pressed!")
                clicksound()
                return 0
            elif self.button7_position.collidepoint(pygame.mouse.get_pos()):
                print("Log Out Button Pressed!")
                clicksound()
                self.logout = True
                return 0
            elif self.button11_position.collidepoint(pygame.mouse.get_pos()):
                print("Query Button Pressed!")
                clicksound()
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
                return -1
            elif self.button10_position.collidepoint(pygame.mouse.get_pos()):
                print("No Button on Pop Up Pressed!")
                clicksound()
                self.logout = False
                return 0
            else:
                return 0
