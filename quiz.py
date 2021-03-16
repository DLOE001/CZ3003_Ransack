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
        # Text1 is for the question
        # Text2 is for the answer A
        # Text3 is for the answer B
        # Text4 is for the answer C
        # Text5 is for the answer D
        # Background1 is for the background
        #Texts
        self.text1 = pygame.font.SysFont('Broadway', 50).render(self.question, True, (0, 0, 0))
        self.text1_position = [120,620]
        self.text2 = pygame.font.SysFont('Arial', 20, True).render("A) " + self.answers[0], True, (0, 0, 0))
        self.text2_position = self.text2.get_rect().move(120,815)
        self.text3 = pygame.font.SysFont('Arial', 20, True).render("B) " + self.answers[1], True, (0, 0, 0))
        self.text3_position = self.text3.get_rect().move(self.text2_position.right + 150,815)
        self.text4 = pygame.font.SysFont('Arial', 20, True).render("C) " + self.answers[2], True, (0, 0, 0))
        self.text4_position = self.text4.get_rect().move(self.text3_position.right + 150,815)
        self.text5 = pygame.font.SysFont('Arial', 20, True).render("D) " + self.answers[3], True, (0, 0, 0))
        self.text5_position = self.text5.get_rect().move(self.text4_position.right + 150,815)
        #Background
        self.background1_image = pygame.image.load("quiz.png")
        self.background1_position = [0,0]

        self.box_rect = pygame.Rect(102, 595, 1112, 806) 

    def draw(self, window, canvas):
        # Copy of background image
        canvas.blit(self.background1_image, self.background1_position)
        #Copy text
        canvas.blit(self.text1, self.text1_position)
        canvas.blit(self.text2, self.text2_position)
        canvas.blit(self.text3, self.text3_position)
        canvas.blit(self.text4, self.text4_position)
        canvas.blit(self.text5, self.text5_position)

    def attempt(self, player):
        if self.text2_position.collidepoint(pygame.mouse.get_pos()):
            if self.answers[0] == self.answer:
                self.completed = True
                player.monster.dead = True
            else:
                player.playerDie()
        elif self.text3_position.collidepoint(pygame.mouse.get_pos()):
            if self.answers[1] == self.answer:
                self.completed = True
                player.monster.dead = True
            else:
                player.playerDie()
        elif self.text4_position.collidepoint(pygame.mouse.get_pos()):
            if self.answers[2] == self.answer:
                self.completed = True
                player.monster.dead = True
            else:
                player.playerDie()
        elif self.text5_position.collidepoint(pygame.mouse.get_pos()):
            if self.answers[3] == self.answer:
                self.completed = True
                player.monster.dead = True
            else:
                player.playerDie()
        else:
            pass
        player.monster = None

    def display_message(surface, color, rect, font_name, size, text, xy, aa=False, bkg=None):
        font = pygame.font.Font(font_name, size)
        rendered_text = font.render(text, aa, (color))
        screen.blit(rendered_text,(xy))
