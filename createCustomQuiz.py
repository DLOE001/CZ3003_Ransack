# Brings in all the pygame keywords we need
from pygame.locals import *

# Import and initialize the pygame library
import pygame
from pickle import TRUE
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

class CreateCustomQuiz:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.popup= popup.PopUp(display_surface)
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):
        # Set background
        self.background1_image = pygame.image.load("images/student_create_custom_quiz.jpg")
        self.background1_position = [0,0]

        # Set back button
        self.backbutton1_position = pygame.Rect(29, 29, 60, 50)
        
        # Set register button
        self.create_rect = pygame.Rect(754, 628, 179, 44)
        pygame.draw.rect(self.screen, (255, 255, 255), self.create_rect)
        self.create_rect_position = [0,0]
        
        # Set the fields for user to key in
        self.quizName_box1 = InputBox(505, 157, 423, 45)
        self.question_box2 = InputBox(288, 250, 640, 82)
        self.answer_box3 = InputBox(442, 355, 490, 45)
        self.wrongAnswer1_box4 = InputBox(442, 421, 490, 45)
        self.wrongAnswer2_box5 = InputBox(441, 488, 490, 45)
        self.wrongAnswer3_box6 = InputBox(441, 560, 490, 45)
        
        self.errorMessage = ""
        self.done = False
        self.input_boxes = [self.quizName_box1, self.question_box2, self.answer_box3, self.wrongAnswer1_box4, self.wrongAnswer2_box5, self.wrongAnswer3_box6]
        
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
                    
            # Display background
            self.display_surface.blit(self.background1_image, self.background1_position)
    
            # Display quiz name, question, answer and 3 wrong answer input
            for box in self.input_boxes:
                box.draw(self.screen)

            # Refresh create custom quiz page on key press
            pygame.display.update()
            clock.tick(30)
            
    def action(self):
        if self.create_rect.collidepoint(pygame.mouse.get_pos()):
            quizName = self.quizName_box1.retrieveBoxValues()
            question = self.question_box2.retrieveBoxValues()
            answer = self.answer_box3.retrieveBoxValues()
            wrongAnswer1 = self.wrongAnswer1_box4.retrieveBoxValues()
            wrongAnswer2 = self.wrongAnswer2_box5.retrieveBoxValues()
            wrongAnswer3 = self.wrongAnswer3_box6.retrieveBoxValues()
            if(self.checkInputFields(quizName, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)):
                mysqlConnection.createCustomQuiz(self.username, quizName, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)
                self.popup.success("Custom Quiz Successfully Created")
                return True
            else:
                self.popup.fail(self.errorMessage)
                for box in self.input_boxes:
                    box.resetText()
                return False
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            return True
        else:
            return False        
        
    # Method to check whether input fields have been properly filled 
    def checkInputFields(self, quizName, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
        passCheck = False
        self.errorMessage =""
        if (len(quizName) <= 0 or len(question) <= 0 or len(answer) <= 0 or len(wrongAnswer1) <= 0 or len(wrongAnswer2) <= 0 or len(wrongAnswer3) <= 0):
            self.errorMessage = "One or more field(s) have not been filled"
            return passCheck
        else:
             allCustomQuizNames = mysqlConnection.retrieveCustomQuizNames()
             if(len(allCustomQuizNames) == 0):
                 passCheck = True
             else:
                 for i in allCustomQuizNames:
                     if(quizName == i):
                         self.errorMessage = "Quiz name has already been taken"
                         break
                     passCheck = True  
        return passCheck