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

# Import Friend
import friends

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
    def __init__(self, user, quizName, username, display_surface, typeOfQuiz):
        self.user = user
        self.username = username
        self.quizName = quizName
        self.display_surface = display_surface
        self.typeOfQuiz = typeOfQuiz
        self.finished = False
        if (self.typeOfQuiz == "Custom" or self.typeOfQuiz == "View Pending Quiz"):
            self.quiz = mysqlConnection.retrieveStudentCustomQuiz(self.quizName)
        elif (self.typeOfQuiz == "Challenge"):
            self.quiz = mysqlConnection.retrieveSpecificChallengeQuizByQuizName(self.quizName)
            self.usernameSelectedFromFriendMenu = ""
            self.replyChallenge = False
            self.battleID = 0
            self.challengerUsername = ""
            self.notificationMessage = ""
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
     
    def passSelectedUsername(self, usernameSelected):
        self.usernameSelectedFromFriendMenu = usernameSelected
        
    def passChallengerUsername(self, challengerUsername):
        self.challengerUsername = challengerUsername
        
    def setReplyChallenge(self, replyChallenge):
        self.replyChallenge = replyChallenge
        
    def setBattleID(self, battleID):
        self.battleID = battleID
        
    def setNotificationMsg(self, notificationMessage):
        self.notificationMessage = notificationMessage
        
    def loadAssets(self):

        # Set background
        self.background1_image = pygame.image.load("images/taking_custom_quiz.jpg")
        self.background1_position = [0,0]

        # Set back button
        self.backbutton1_position = pygame.Rect(29, 29, 60, 50)

    # Main Menu Display
    def display(self):
        # Display background 
        self.display_surface.blit(self.background1_image, self.background1_position)

        # Displays Custom Quiz Info
        self.display_surface.blit(self.quizNametext, self.quizNametext_rect)
        self.display_surface.blit(self.questiontext, self.questiontext_position)
        self.display_surface.blit(self.answertext, self.answertext_position)
        self.display_surface.blit(self.wrongAnswer1text, self.wrongAnswer1text_position)
        self.display_surface.blit(self.wrongAnswer2text, self.wrongAnswer2text_position)
        self.display_surface.blit(self.wrongAnswer3text, self.wrongAnswer3text_position)
    
    # Main Menu Actions
    def action(self):
        if self.typeOfQuiz == "View Pending Quiz":
            if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
                    clicksound()
                    self.finished = True
                    return 8
        if self.typeOfQuiz == "Custom":
            if self.user == "Student":
                correctMessage = "Correct"
                wrongMessage = "Wrong"
                if self.answer_rect.collidepoint(pygame.mouse.get_pos()):
                    self.popup.success(correctMessage)
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
                    self.popup.fail(wrongMessage)
                    currentScore = mysqlConnection.retrieveStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username)
                    if len(currentScore) == 0:
                        mysqlConnection.insertStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username, self.score)
                    self.finished = True
                    return 8
                if self.wrongAnswer2_rect.collidepoint(pygame.mouse.get_pos()):
                    self.popup.fail(wrongMessage)
                    currentScore = mysqlConnection.retrieveStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username)
                    if len(currentScore) == 0:
                        mysqlConnection.insertStudentCustomQuizScore(int(self.quiz[0][0]), self.quizName, self.username, self.score)
                    self.finished = True
                    return 8
                if self.wrongAnswer3_rect.collidepoint(pygame.mouse.get_pos()):
                    self.popup.fail(wrongMessage)
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
        elif self.typeOfQuiz == "Challenge":
            if self.user == "Student":
                if (self.replyChallenge):
                    checkWinner = mysqlConnection.retrievePendingBattleStatus(self.challengerUsername, self.username)
                    challengerScore = 0
                    battleResult = ""
                    winner = ""
                    if(len(checkWinner) > 0):
                        for i in range(len(checkWinner)):
                            if(checkWinner[i][6] != None and checkWinner[i][7] != None):
                                pass
                            else:
                                if (checkWinner[i][6] == None and checkWinner[i][7] == None):
                                    challengerScore = checkWinner[i][4]
                                    break
                    if self.answer_rect.collidepoint(pygame.mouse.get_pos()):
                        self.score = 100
                        if (challengerScore == self.score):
                            battleResult = "Drew"
                            winner = "Drew Battle"
                        elif (challengerScore < self.score):
                            battleResult = "Won"
                            winner = self.username
                        self.popup.success("Correct, " + battleResult + " your battle against " + self.challengerUsername)
                        mysqlConnection.updateStudentChallengeQuizScore(int(self.battleID), self.score, winner)
                        mysqlConnection.removeNotification(self.username, self.notificationMessage)
                        self.finished = True
                        return 14
                    if self.wrongAnswer1_rect.collidepoint(pygame.mouse.get_pos()):
                        if (challengerScore == self.score):
                            battleResult = "Drew"
                            winner = "Drew Battle"
                        elif (challengerScore > self.score):
                            battleResult = "Lost"
                            winner = self.challengerUsername
                        self.popup.fail("Wrong, " + battleResult + " your battle against " + self.challengerUsername)
                        mysqlConnection.updateStudentChallengeQuizScore(int(self.battleID), self.score, winner)
                        mysqlConnection.removeNotification(self.username, self.notificationMessage)
                        self.finished = True
                        return 14
                    if self.wrongAnswer2_rect.collidepoint(pygame.mouse.get_pos()):
                        if (challengerScore == self.score):
                            battleResult = "Drew"
                            winner = "Drew"
                        elif (challengerScore > self.score):
                            battleResult = "Lost"
                            winner = self.challengerUsername
                        self.popup.fail("Wrong, " + battleResult + " your battle against " + self.challengerUsername)
                        mysqlConnection.updateStudentChallengeQuizScore(int(self.battleID), self.score, winner)
                        mysqlConnection.removeNotification(self.username, self.notificationMessage)
                        self.finished = True
                        return 14
                    if self.wrongAnswer3_rect.collidepoint(pygame.mouse.get_pos()):
                        if (challengerScore == self.score):
                            battleResult = "Drew"
                            winner = "Drew"
                        elif (challengerScore > self.score):
                            battleResult = "Lost"
                            winner = self.challengerUsername
                        self.popup.fail("Wrong, " + battleResult + " your battle against " + self.challengerUsername)
                        mysqlConnection.updateStudentChallengeQuizScore(int(self.battleID), self.score, winner)
                        mysqlConnection.removeNotification(self.username, self.notificationMessage)
                        self.finished = True
                        return 14
                    if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
                        clicksound()
                        self.finished = True
                        return 14
                    
                else:
                    correctMessage = "Correct, score saved for current challenge"
                    wrongMessage = "Wrong, score saved for current challenge"
                    notificationMessage = self.username + " sent you a challenge"
                    if self.answer_rect.collidepoint(pygame.mouse.get_pos()):
                        self.popup.success(correctMessage)
                        self.score = 100
                        mysqlConnection.insertStudentChallengeQuizScore(int(self.quiz[0][0]), self.quiz[0][1], self.username, self.score, self.usernameSelectedFromFriendMenu)
                        mysqlConnection.insertNotification(self.usernameSelectedFromFriendMenu, notificationMessage)
                        self.finished = True
                        return 5
                    if self.wrongAnswer1_rect.collidepoint(pygame.mouse.get_pos()):
                        self.popup.fail(wrongMessage)
                        mysqlConnection.insertStudentChallengeQuizScore(int(self.quiz[0][0]), self.quiz[0][1], self.username, self.score, self.usernameSelectedFromFriendMenu)
                        mysqlConnection.insertNotification(self.usernameSelectedFromFriendMenu, notificationMessage)
                        self.finished = True
                        return 5
                    if self.wrongAnswer2_rect.collidepoint(pygame.mouse.get_pos()):
                        self.popup.fail(wrongMessage)
                        mysqlConnection.insertStudentChallengeQuizScore(int(self.quiz[0][0]), self.quiz[0][1], self.username, self.score, self.usernameSelectedFromFriendMenu)
                        mysqlConnection.insertNotification(self.usernameSelectedFromFriendMenu, notificationMessage)
                        self.finished = True
                        return 5
                    if self.wrongAnswer3_rect.collidepoint(pygame.mouse.get_pos()):
                        self.popup.fail(wrongMessage)
                        mysqlConnection.insertStudentChallengeQuizScore(int(self.quiz[0][0]), self.quiz[0][1], self.username, self.score, self.usernameSelectedFromFriendMenu)
                        mysqlConnection.insertNotification(self.usernameSelectedFromFriendMenu, notificationMessage)
                        self.finished = True
                        return 5
                    if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
                        clicksound()
                        self.finished = True
                        return 5