# Brings in all the pygame keywords we need
from pygame.locals import *

# Import tkinter for file directory 
import tkinter as tk
from tkinter import filedialog 

# Get file name
import os

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Imports Text Box
from friendinputBox import InputBox

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
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio\Click.wav'), maxtime=2000)

class UploadAssignment:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        # Background1 is for the header
        # Button 1 is back button
        # Button 2 is query button

    def loadAssets(self):

        self.done = False
        # Set background
        self.background1_image = pygame.image.load("images/teacher_upload_assignment.jpg")
        self.background1_position = [0,0]

        #Set back button 
        self.backbutton1_position = pygame.Rect(40, 39, 67, 56)

        # Set assignment name input
        self.assignmentnameinput_box = InputBox(616, 279, 512, 40)
        self.input_boxes = [self.assignmentnameinput_box]

        # Set choose assignment file button
        self.chooseassignment_rect = pygame.Rect(354, 488, 316, 43)
        pygame.draw.rect(self.screen, (255, 255, 255), self.chooseassignment_rect)
        self.chooseassignment_rect_position = [0,0]

        # Set current upload path text
        self.filepath = ""
        self.uploadpathtext = pygame.font.SysFont('Broadway', 30).render(self.filepath, True, (0, 0, 0))
        self.uploadpathtext_position = [354,564]

        # Set upload assignment file button
        self.uploadassignment_rect = pygame.Rect(845, 696, 223, 52)
        pygame.draw.rect(self.screen, (255, 255, 255), self.uploadassignment_rect)
        self.uploadassignment_rect_position = [0,0]

        # Set facebook button
        self.facebook_rect = pygame.Rect(420, 770, 49, 52)
        pygame.draw.rect(self.screen, (255, 255, 255), self.facebook_rect)
        self.facebook_rect_position = [0,0]

        # Set twitter button
        self.twitter_rect = pygame.Rect(509, 773, 49, 52)
        pygame.draw.rect(self.screen, (255, 255, 255), self.twitter_rect)
        self.twitter_rect_position = [0,0]

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

            # Display Username Text
            self.screen.blit(self.uploadpathtext, self.uploadpathtext_position)

            # Display friend input
            self.assignmentnameinput_box.draw(self.screen)

            # Refresh Page on key press
            pygame.display.update()
            clock.tick(30)

    def action(self):
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Back Button Clicked")
            return True
        if self.chooseassignment_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Choose File Button Clicked")

            # Get filename
            self.filepath = openfile()
            # Set filename to postion
            self.uploadpathtext = pygame.font.SysFont('Broadway', 30).render(self.filepath, True, (0, 0, 0))
        if self.uploadassignment_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Upload Button Clicked")
        if self.facebook_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Facebook Button Clicked")
        if self.twitter_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Twitter Button Clicked")

# Select file from file directory
def openfile():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path
