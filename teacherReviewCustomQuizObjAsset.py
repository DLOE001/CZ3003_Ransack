# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Import SQL Connection 
import mysqlConnection

# Import Taking Custom Quiz UI 
import taking_custom_quiz

# Mouseover animation(Makes the image transparent if cursor is touching)
def mouseover(img, pos):
    if pos.collidepoint(pygame.mouse.get_pos()):
        img.set_alpha(50)
    else:
        img.set_alpha(255)

# Click sound
def clicksound():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class TeacherReviewCustomQuizObjAsset:
    def __init__(self, user, username, quizName, rating, iteration,  display_surface):
        self.user = user
        self.username = username
        self.quizName = quizName
        self.rating = rating
        self.display_surface = display_surface
        self.ratingChange = ""
        self.y_axis = 250
        self.iteration = iteration
        y_axis_offset = self.iteration * 100
        self.stopRunning = False
        self.typeOfQuiz = "Custom"
        
        self.approve_rect = pygame.Rect(757, y_axis_offset + self.y_axis, 90, 66)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.approve_rect)
        
        self.reject_rect = pygame.Rect(854, y_axis_offset + self.y_axis, 90, 66)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.reject_rect)
        
        self.selectQuiz_rect = pygame.Rect(294, y_axis_offset + self.y_axis, 459, 66)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.reject_rect)
        
        # Set Rating Text
        self.ratingtext1 = pygame.font.SysFont('Courier New', 30).render(str(self.rating), True, (247, 230, 82))
        self.ratingtext1_position = [250,y_axis_offset + self.y_axis + 20]
        
        # Set Quiz Name Text
        self.quizNametext1 = pygame.font.SysFont('Courier New', 30).render(self.quizName, True, (247, 230, 82))
        self.quizNametext1_position = [305,y_axis_offset + self.y_axis + 20]
        
        # Popup box iamge
        self.popupbox_image = pygame.image.load("images/teacherReviewCustomQuizObjAsset.png")
        self.popupbox_position = [232, y_axis_offset + self.y_axis]    
        
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
        if self.approve_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            mysqlConnection.updateUserCustomQuizStatus(self.quizName, "Approved")
        if self.reject_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            mysqlConnection.updateUserCustomQuizStatus(self.quizName, "Rejected")
            mysqlConnection.removeRejectedCustomQuiz()
        if self.selectQuiz_rect.collidepoint(pygame.mouse.get_pos()):
            # Create create custom quiz Object
            self.takingQuizUI = taking_custom_quiz.TakingQuizUI(self.user, self.quizName, self.username, self.display_surface, self.typeOfQuiz)
            self.takingQuizUI.loadAssets()
            clicksound()
            self.stopRunning = False
            while not self.stopRunning:  
                self.takingQuizUI.display()
                if(getattr(self.takingQuizUI, 'finished')):
                    self.stopRunning = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == MOUSEBUTTONDOWN:
                        self.takingQuizUI.action()
                    pygame.display.update()
            return 10

