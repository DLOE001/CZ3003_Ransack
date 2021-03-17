# Brings in all the pygame keywords we need
from pygame.locals import *
import random

# Import and initialize the pygame library
import pygame
pygame.init()
pygame.font.init()

class Quiz:
    def __init__(self, question, answer, dummy1, dummy2, dummy3):
        self.question = question
        self.answer = answer
        self.answers = []
        self.answers.append(answer)
        self.answers.append(dummy1)
        self.answers.append(dummy2)
        self.answers.append(dummy3)
        random.shuffle(self.answers)
        self.completed = False
        # answer1 is for the answer A
        # answer2 is for the answer B
        # answer3 is for the answer C
        # answer4 is for the answer D
        # Background1 is for the background
        #Texts
        self.answer1 = pygame.font.SysFont('Arial', 20, True).render("A) " + self.answers[0], True, (0, 0, 0))
        self.answer1_rect = self.answer1.get_rect().move(120,815)
        self.answer2 = pygame.font.SysFont('Arial', 20, True).render("B) " + self.answers[1], True, (0, 0, 0))
        self.answer2_rect = self.answer2.get_rect().move(self.answer1_rect.right + 100,815)
        self.answer3 = pygame.font.SysFont('Arial', 20, True).render("C) " + self.answers[2], True, (0, 0, 0))
        self.answer3_rect = self.answer3.get_rect().move(self.answer2_rect.right + 100,815)
        self.answer4 = pygame.font.SysFont('Arial', 20, True).render("D) " + self.answers[3], True, (0, 0, 0))
        self.answer4_rect = self.answer4.get_rect().move(self.answer3_rect.right + 100,815)
        #Background
        self.background1_image = pygame.image.load("images/quiz.png")
        self.background1_position = [0,0]

        self.box_rect = pygame.Rect(102, 595, 1000, 806) 

    def draw(self, canvas):
        # Copy of background image
        canvas.blit(self.background1_image, self.background1_position)
        
        #Copy text
        self.drawWrappedText(canvas, self.question, (0, 0, 0), self.box_rect, pygame.font.SysFont('Broadway', 50))
        canvas.blit(self.answer1, self.answer1_rect)
        canvas.blit(self.answer2, self.answer2_rect)
        canvas.blit(self.answer3, self.answer3_rect)
        canvas.blit(self.answer4, self.answer4_rect)

    def attempt(self, player):
        if self.answer1_rect.collidepoint(pygame.mouse.get_pos()):
            if self.answers[0] == self.answer:
                print("Correct")
                print("You have earned 100 points!")
                player.score += 100
                print("Current Score:" + str(player.score))
                self.completed = True
                player.monster.dead = True
            else:
                player.hearts -= 1
                print("Wrong")
                print("You have lost 25 points!")
                player.score -= 25
                print("Current Score:" + str(player.score))
                print("Player Hearts Left:" + str(player.hearts))
        elif self.answer2_rect.collidepoint(pygame.mouse.get_pos()):
            if self.answers[1] == self.answer:
                print("Correct")
                print("You have earned 100 points!")
                player.score += 100
                print("Current Score:" + str(player.score))
                self.completed = True
                player.monster.dead = True
            else:
                player.hearts -= 1
                print("Wrong")
                print("You have lost 25 points!")
                player.score -= 25
                print("Current Score:" + str(player.score))
                print("Player Hearts Left:" + str(player.hearts))
        elif self.answer3_rect.collidepoint(pygame.mouse.get_pos()):
            if self.answers[2] == self.answer:
                print("Correct")
                print("You have earned 100 points!")
                player.score += 100
                print("Current Score:" + str(player.score))
                self.completed = True
                player.monster.dead = True
            else:
                player.hearts -= 1
                print("Wrong")
                print("You have lost 25 points!")
                player.score -= 25
                print("Current Score:" + str(player.score))
                print("Player Hearts Left:" + str(player.hearts))
        elif self.answer4_rect.collidepoint(pygame.mouse.get_pos()):
            if self.answers[3] == self.answer:
                print("Correct")
                print("You have earned 100 points!")
                player.score += 100
                print("Current Score:" + str(player.score))
                self.completed = True
                player.monster.dead = True
            else:
                player.hearts -= 1
                print("Wrong")
                print("You have lost 25 points!")
                player.score -= 25
                print("Current Score:" + str(player.score))
                print("Player Hearts Left:" + str(player.hearts))
        else:
            pass
        player.monster = None

    # draw some text into an area of a surface
    # automatically wraps words
    # returns any text that didn't get blitted
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

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text
