# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

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
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class CustomQuizObjAsset:
    def __init__(self, quizName, rating, iteration,  display_surface):
        self.quizName = quizName
        self.rating = rating
        self.display_surface = display_surface
        self.ratingChange = ""
        self.y_axis = 210
        self.iteration = iteration
        y_axis_offset = self.iteration * 100
        
        self.upArrow_rect = pygame.Rect(832, y_axis_offset + self.y_axis, 50, 62)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.upArrow_rect)
        
        self.downArrow_rect = pygame.Rect(888, y_axis_offset + self.y_axis, 50, 62)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.downArrow_rect)
        
        # Set Rating Text
        self.ratingtext1 = pygame.font.SysFont('Courier New', 30).render(str(self.rating), True, (0, 0, 0))
        self.ratingtext1_position = [250,y_axis_offset + self.y_axis + 20]
        
        # Set Quiz Name Text
        self.quizNametext1 = pygame.font.SysFont('Courier New', 30).render(self.quizName, True, (0, 0, 0))
        self.quizNametext1_position = [305,y_axis_offset + self.y_axis + 20]
        
        # Popup box iamge
        self.popupbox_image = pygame.image.load("images/customQuizObjAsset.png")
        self.popupbox_position = [224, y_axis_offset + self.y_axis]    
        
    # Popup Display
    def display(self):
    
        # Display background 
        self.display_surface.blit(self.popupbox_image, self.popupbox_position)

        # Displays Custom Quiz Info
        self.display_surface.blit(self.ratingtext1, self.ratingtext1_position)
        self.display_surface.blit(self.quizNametext1, self.quizNametext1_position)

        """
        # Wait for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                
                #self.action()
                pass
        """
    
    # Popup Actions
    def action(self):
        if self.upArrow_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            self.rating += 1
            mysqlConnection.updateCustomQuizScore(self.quizName, self.rating)
        if self.downArrow_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            self.rating -= 1
            mysqlConnection.updateCustomQuizScore(self.quizName, self.rating)
        

