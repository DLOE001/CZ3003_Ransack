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
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class PopUp:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.layer1 = pygame.Surface([1200,900], pygame.SRCALPHA, 32)
        self.displaying = False

        # Header
        self.headerText = None
        self.headerText_rect = [0,0]

        # Message box dimensions
        self.headerBox_left = 324
        self.headerBox_right = 908
        self.headerBox_top = 343
        self.headerBox_bottom = 383
        
        # Message
        self.messageText = None
        self.messageText_rect = [0,0]

        # Message box dimensions
        self.messageBox_rect = pygame.Rect(324, 387, 590, 617)
        self.messageBox_left = 324
        self.messageBox_right = 908
        self.messageBox_top = 387
        self.messageBox_bottom = 617

        # Popup box iamge
        self.popupbox_image = pygame.image.load("images/popup.png")
        self.popupbox_position = [322,340]    

        # Set cross button 
        self.crossbutton_image = pygame.image.load("images/cross.png")
        self.crossbutton_rect = self.crossbutton_image.get_rect().move(867, 347)

        # Set ok button
        self.okbutton_image = pygame.image.load("images/ok2.png")
        self.okbutton_rect = self.okbutton_image.get_rect()
        self.okbutton_rect.center = (((self.messageBox_left+self.messageBox_right)/2), 618)

        self.msg=""
        self.msgsize=0

    # Success Popup
    def success(self, msg="Action was successful!", hdr="Success", msgsize=40, hdrsize=30):
        self.displaying = True
        self.header(hdr, hdrsize)
        self.message(msg, msgsize)
        self.display()

    # Error/Fail Popup
    def fail(self, msg="Action failed!", hdr="Error", msgsize=40, hdrsize=30):
        self.displaying = True
        self.header(hdr, hdrsize)
        self.message(msg, msgsize)
        self.display()

    # Define the popup header
    def header(self, hdr, size=30):
        self.headerText = pygame.font.SysFont('Arial', size, True).render(hdr, True, (0, 0, 0))
        self.headerText_rect = self.headerText.get_rect()
        self.headerText_rect.center = ((self.headerBox_left+self.headerBox_right)/2), ((self.headerBox_top+self.headerBox_bottom)/2)

    # Define the popup message
    def message(self, msg, size=40):
        self.msg = msg
        self.msgsize = size
        self.messageText = pygame.font.SysFont('Arial', size, True).render(msg, True, (0, 0, 0))
        self.messageText_rect = self.messageText.get_rect()
        self.messageText_rect.center = ((self.messageBox_left+self.messageBox_right)/2), ((self.messageBox_top+self.messageBox_bottom)/2)

    # Popup Display
    def display(self):
        while self.displaying:
            # Display background 
            self.layer1.blit(self.popupbox_image, self.popupbox_position)

            # Display cross button 
            self.layer1.blit(self.crossbutton_image, self.crossbutton_rect)

            # Display ok button
            self.layer1.blit(self.okbutton_image, self.okbutton_rect)

            # Display header
            self.layer1.blit(self.headerText, self.headerText_rect)

            # Display message
            if self.drawWrappedText(self.layer1, self.msg, (0, 0, 0), self.messageBox_rect, pygame.font.SysFont('Arial', self.msgsize)):
                self.layer1.blit(self.messageText, self.messageText_rect)

            # Mouseover animations
            mouseover(self.crossbutton_image, self.crossbutton_rect)
            mouseover(self.okbutton_image, self.okbutton_rect)

            # Draw layer 1 onto the window surface
            self.display_surface.blit(self.layer1, (0,0))

            # Wait for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    self.displaying = self.action()

            self.layer1.fill((0,0,0,0))

            pygame.display.update()
            
    
    # Popup Actions
    def action(self):
        # Cross or Ok button is selected
        if self.crossbutton_rect.collidepoint(pygame.mouse.get_pos()) or self.okbutton_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return False
        else:
            return True

    def drawWrappedText(self, surface, text, color, rect, font, aa=True, bkg=None):
        rect = Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            image_rect = image.get_rect()
            image_rect.center =((self.messageBox_left+self.messageBox_right)/2, y+image_rect.height*2)

            surface.blit(image, image_rect)
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text
