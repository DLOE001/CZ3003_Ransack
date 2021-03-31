# Brings in all the pygame keywords we need
from pygame.locals import *

# Import tkinter for file directory 
import tkinter as tk
from tkinter import filedialog 

# Get file name
import os

# Get today's date
from datetime import date

# Import and initialize the pygame library
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()

# Imports Text Box
from friendinputBox import InputBox

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

class UploadAssignment:
    def __init__(self, username, user, screen, display_surface):
        self.username = username
        self.user = user
        self.display_surface = display_surface
        self.screen = screen
        self.popup= popup.PopUp(display_surface)

        # 1 = upload page, 0 = view upload
        self.state = True

    def loadAssets(self):
        # false means will contiune staying on this page
        self.done = False
        self.platform = ""

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

        # Set current platform text
        self.platformtext = pygame.font.SysFont('Broadway', 30).render(self.platform, True, (0, 0, 0))
        self.platformtext_position = [457,830]

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

        # Set stateupload
        self.stateupload_rect = pygame.Rect(77, 480, 220, 85)
        pygame.draw.rect(self.screen, (255, 255, 255), self.stateupload_rect)
        self.stateupload_rect_position = [0,0]

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

            # At upload page
            if (self.state == True): 
                # Display background
                self.background1_image = pygame.image.load("images/teacher_upload_assignment.jpg")
                self.display_surface.blit(self.background1_image, self.background1_position)

                # Display uploadpath Text
                self.screen.blit(self.uploadpathtext, self.uploadpathtext_position)

                # Display usernames Text
                self.screen.blit(self.platformtext, self.platformtext_position)

                # Display assignment input
                self.assignmentnameinput_box.draw(self.screen)
            
            # At view upload page
            elif (self.state == False): 
                # Set background
                self.background1_image = pygame.image.load("images/teacher_viewuploadedassignment.jpg")
                self.display_surface.blit(self.background1_image, self.background1_position)

                self.displayassignmentlist()
            # Refresh Page on key press
            pygame.display.update()
            clock.tick(30)

    def action(self):
        if self.backbutton1_position.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Back Button Clicked")
            self.state == True
            return True
        if self.chooseassignment_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Choose File Button Clicked")
            # Get filename
            self.filepath = openfile()
            # Set filename to postion
            self.uploadpathtext = pygame.font.SysFont('Courier New', 25).render(self.filepath, True, (0, 0, 0))
        if self.facebook_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Facebook Button Clicked")
            self.platform = 'facebook'
            self.platformtext = pygame.font.SysFont('Courier New', 20).render(self.platform, True, (0, 0, 0))
        if self.twitter_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Twitter Button Clicked")
            self.platform = 'twitter'
            self.platformtext = pygame.font.SysFont('Courier New', 20).render(self.platform, True, (0, 0, 0))
        if self.uploadassignment_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            print("Upload Button Clicked")
            # Assignment name 
            assignmentname = self.assignmentnameinput_box.retrieveBoxValues()
            # Upload date
            today = date.today()
            uploaddate = today.strftime("%d/%m/%Y")
            # Check all inputs are filled
            if (len(assignmentname) == 0 or len(self.platform) == 0 or len(self.filepath) == 0):
                self.popup.fail("Please input all the fields!")
            else :
                mysqlConnection.insertAssignment(self.username, assignmentname, self.platform, uploaddate)
                self.popup.success("Assignment Uploaded!")
        
        if self.stateupload_rect.collidepoint(pygame.mouse.get_pos()):
            clicksound()
            # from upload page to view uploaded page
            if (self.state == True):
                self.state = False

                # Change button postion to upload page for teacher to click
                self.stateupload_rect = pygame.Rect(77, 359, 220, 85)
                pygame.draw.rect(self.screen, (255, 255, 255), self.stateupload_rect)
                self.stateupload_rect_position = [0,0]

                self.platform = ""
                self.filepath = ""
            # from view uploaded page to upload page
            else: 
                self.state = True

                # Change button postion to view upload page for teacher to click
                self.stateupload_rect = pygame.Rect(77, 480, 220, 85)
                pygame.draw.rect(self.screen, (255, 255, 255), self.stateupload_rect)
                self.stateupload_rect_position = [0,0]
            print("Uploadstate Clicked")

    # Display assignment when teacher clicked on view uploaded assignment
    def displayassignmentlist(self):
        assignmentlist = mysqlConnection.retrieveAssignment()
        index = 0
        for v in assignmentlist:
            print(v)
            # For each assignment, set and display the names accordingly
            self.assignment_text1 = pygame.font.SysFont('Broadway', 30).render(v[0], True, (0, 0, 0))
            self.assignment_text2 = pygame.font.SysFont('Broadway', 30).render(v[1], True, (0, 0, 0))
            self.assignment_text3 = pygame.font.SysFont('Broadway', 30).render(v[2], True, (0, 0, 0))

            self.assignment_text1_position = [391,341 + index*56]
            self.assignment_text2_position = [659 ,341 + index*56]
            self.assignment_text3_position = [887,341 + index*56]

            self.screen.blit(self.assignment_text1, self.assignment_text1_position)
            self.screen.blit(self.assignment_text2, self.assignment_text2_position)
            self.screen.blit(self.assignment_text3, self.assignment_text3_position)
            index = index + 1
        
# Select file from file directory
def openfile():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path