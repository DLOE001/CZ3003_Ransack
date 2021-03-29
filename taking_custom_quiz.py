# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

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
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/Click.wav'), maxtime=2000)

class TakingQuizUI:
    def __init__(self, user, quizName, username, display_surface):
        self.user = user
        self.username = username
        self.quizName = quizName
        self.display_surface = display_surface
        self.finished = False
        self.quiz = mysqlConnection.retrieveStudentCustomQuiz(self.quizName)
        self.score = 0
        self.popup= popup.PopUp(display_surface)
        
        #Define Colours
        WHITE = (255,255,255)
        GREEN = (144,238,144)
        RED = (255,0,0)
        BLUE = (0,0,255)
        BLACK = (0,0,0)
        FUCHSIA = (255, 0, 255)
        GRAY = (128, 128, 128)
        LIME = (0, 128, 0)
        MAROON = (128, 0, 0)
        NAVYBLUE = (0, 0, 128)
        OLIVE = (128, 128, 0)
        PURPLE = (128, 0, 128)
        TEAL = (0,128,128)
        
        self.headerBox = pygame.Rect(218, 60, 741, 70)
        self.headerBox_left = 218
        self.headerBox_right = 959
        self.headerBox_top = 60
        self.headerBox_bottom = 130
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.headerBox)
        
        # Set Quiz Name Text
        self.quizNametext = pygame.font.SysFont('Courier New', 30).render(self.quiz[0][1], True, GREEN)
        centerOffset = len(self.quiz[0][1]) * 9
        self.quizNametext_rect = [(218 + (741/2)) - centerOffset, self.headerBox_top + 20]
        
        # Set Question Text
        self.questiontext = pygame.font.SysFont('Courier New', 30).render(self.quiz[0][2], True, GREEN)
        self.questiontext_position = [285, 208]
        
        # Set Answer Text
        self.answertext = pygame.font.SysFont('Courier New', 30).render("a) " + self.quiz[0][3], True, GREEN)
        self.answertext_position = [293, 329]
        self.answer_rect = pygame.Rect(264, 310, 684, 73)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.answer_rect)
        
        # Set Wrong Answer 1 Text
        self.wrongAnswer1text = pygame.font.SysFont('Courier New', 30).render("b) " + self.quiz[0][4], True, GREEN)
        self.wrongAnswer1text_position = [293, 407]
        self.wrongAnswer1_rect = pygame.Rect(264, 388, 684, 73)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.wrongAnswer1_rect)
        
        # Set Wrong Answer 2 Text
        self.wrongAnswer2text = pygame.font.SysFont('Courier New', 30).render("c) " + self.quiz[0][5], True, GREEN)
        self.wrongAnswer2text_position = [293, 484]
        self.wrongAnswer2_rect = pygame.Rect(264, 465, 684, 81)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.wrongAnswer2_rect)
        
        # Set Wrong Answer 3 Text
        self.wrongAnswer3text = pygame.font.SysFont('Courier New', 30).render("d) " + self.quiz[0][6], True, GREEN)
        self.wrongAnswer3text_position = [293, 569]
        self.wrongAnswer3_rect = pygame.Rect(264, 553, 684, 78)
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.wrongAnswer3_rect)
        
    def loadAssets(self):

        # Set background
        self.background1_image = pygame.image.load("images/taking_custom_quiz.jpg")
        self.background1_position = [0,0]

        # Set back button
        self.backbutton1 = pygame.image.load("images/w2.png")
        self.backbutton1_position = self.backbutton1.get_rect().move(22, 21)

    # Main Menu Display
    def display(self):
        # Display background 
        self.display_surface.blit(self.background1_image, self.background1_position)

        # Display world 1 button 
        self.display_surface.blit(self.backbutton1, self.backbutton1_position)

        # Displays Custom Quiz Info
        self.display_surface.blit(self.quizNametext, self.quizNametext_rect)
        self.display_surface.blit(self.questiontext, self.questiontext_position)
        self.display_surface.blit(self.answertext, self.answertext_position)
        self.display_surface.blit(self.wrongAnswer1text, self.wrongAnswer1text_position)
        self.display_surface.blit(self.wrongAnswer2text, self.wrongAnswer2text_position)
        self.display_surface.blit(self.wrongAnswer3text, self.wrongAnswer3text_position)
     
        # Hide all buttons 
        self.backbutton1.set_alpha(0)

    
    # Main Menu Actions
    def action(self):
        if self.user == "Student":
            if self.answer_rect.collidepoint(pygame.mouse.get_pos()):
                self.popup.success("Correct")
                self.score = 100
                currentScore = mysqlConnection.retrieveStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username)
                if len(currentScore) > 0:
                    if currentScore[0][0] < self.score:
                        mysqlConnection.updateStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username, self.score)
                elif len(currentScore) == 0:
                    mysqlConnection.insertStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username, self.score)
                self.finished = True
                return 8
            if self.wrongAnswer1_rect.collidepoint(pygame.mouse.get_pos()):
                self.popup.fail("Wrong")
                currentScore = mysqlConnection.retrieveStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username)
                if len(currentScore) == 0:
                    mysqlConnection.insertStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username, self.score)
                self.finished = True
                return 8
            if self.wrongAnswer2_rect.collidepoint(pygame.mouse.get_pos()):
                self.popup.fail("Wrong")
                currentScore = mysqlConnection.retrieveStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username)
                if len(currentScore) == 0:
                    mysqlConnection.insertStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username, self.score)
                self.finished = True
                return 8
            if self.wrongAnswer3_rect.collidepoint(pygame.mouse.get_pos()):
                self.popup.fail("Wrong")
                currentScore = mysqlConnection.retrieveStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username)
                if len(currentScore) == 0:
                    mysqlConnection.insertStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username, self.score)
                self.finished = True
                return 8
            if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
                clicksound()
                self.finished = True
                return 8
        elif self.user == "Teacher":
            if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
                clicksound()
                self.finished = True
                return 10
        