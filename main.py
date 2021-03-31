# EyeLearnSE Game by Team Ransack(2021)

# Brings in all the pygame keywords we need
from pygame.locals import *

# Main Menu Class
import mainmenu

# World Select Class
import worldselect

# Login Page Class
import loginPage

# Login Register Class
import registerPage

# Login Recover Class
import recoverPage

# Quiz Level Page Class
import quizLevel

# Leadeboard  Class
import leaderboard

# Friends  Class
import friends

# Upload Assignment Class
import uploadAssignmentPage

# Student Custom Quiz Lobby
import studentCustomQuizLobby

# Teacher Custom Quiz Lobby
import teacherCustomQuizLobby

# Teacher Summary Report
import teacherSummaryReport

# Teacher Class Managementr
import teacherClassManagement

# Profile Class
import profile

# Profile Class
import mailboxPage

# Import and initialize the pygame library
import pygame
pygame.init()

# Initialise Global Variables
running = True
state = 2

# Name of the game
pygame.display.set_caption("EyeLearnSE")

# Game window resolution
screen_width = 1200
screen_height = 900

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))
  
# Set the display surface 
display_surface = pygame.display.set_mode((screen_width, screen_height))

# Colour Coordinates(RGB)
white = [255, 255, 255]

# Sample User Data
username = ""
user = ""

# Create Login Object
login = loginPage.Login(username, user, screen, display_surface)
login.loadAssets()
    
# Create Login Object
register = registerPage.Register(username, user, screen, display_surface)
register.loadAssets()

# Create Login Object
recover = recoverPage.Recover(username, user, screen, display_surface)
recover.loadAssets()

# Create Main Menu Object
menu = mainmenu.MainMenu(username, user, screen, display_surface)
menu.loadAssets()
    
# Create World Select Object
worldSelect = worldselect.WorldSelect(username, user, screen, display_surface)
worldSelect.loadAssets()

# Create Leaderboard Object
leaderBoard = leaderboard.Leaderboard(username, user, screen, display_surface)
leaderBoard.loadAssets()

# Create Friends Object
friendMenu = friends.Friends(username, user, screen, display_surface)
friendMenu.loadAssets()

# Create Upload Assignment Object
uploadAssignment = uploadAssignmentPage.UploadAssignment(username, user, screen, display_surface)
uploadAssignment.loadAssets()

# Student Custom Lobby Object
studentCustomQuizMenu = studentCustomQuizLobby.StudentCustomQuizLobby(username, user, screen, display_surface)
studentCustomQuizMenu.loadAssets()

# Student Custom Lobby Object
teacherCustomQuizMenu = teacherCustomQuizLobby.TeacherCustomQuizLobby(username, user, screen, display_surface)
teacherCustomQuizMenu.loadAssets()

# Teacher Summary Report
teacherReport = teacherSummaryReport.TeacherSummaryReport(username, user, screen, display_surface)

# Teacher Class Management
teacherClass = teacherClassManagement.TeacherClassManagement(username, user, screen, display_surface)

# Create Profile Object
profileObject = profile.Profile(username, user, display_surface)

# Create Profile Object
mailBoxObject = mailboxPage.Mailbox(username, user, display_surface)

# Create Quiz Level Object
level = quizLevel.QuizLevel()

# Recreates the UI Objects passing in the logged in user's username and user type
def recreateUIObj(username, user):
    global login
    global menu
    global worldSelect
    global level
    global leaderBoard
    global friendMenu
    global uploadAssignment
    global studentCustomQuizMenu
    global teacherCustomQuizMenu
    global profileObject
    global mailBoxObject
    
     # Create Login Object
    login = loginPage.Login(username, user, screen, display_surface)
    login.loadAssets()
                
    # Create Main Menu Object
    menu = mainmenu.MainMenu(username, user, screen, display_surface)
    menu.loadAssets()
                
    #Create World Select Object
    worldSelect = worldselect.WorldSelect(username, user, screen, display_surface)
    worldSelect.loadAssets()
                
    # Create Leaderboard Object
    leaderBoard = leaderboard.Leaderboard(username, user, screen, display_surface)
    leaderBoard.loadAssets()
    
    # Create Friends Object
    friendMenu = friends.Friends(username, user, screen, display_surface)
    friendMenu.loadAssets()
    
    # Create Upload Assignment Object
    uploadAssignment = uploadAssignmentPage.UploadAssignment(username, user, screen, display_surface)
    uploadAssignment.loadAssets()
    
    # Student Custom Lobby Object
    studentCustomQuizMenu = studentCustomQuizLobby.StudentCustomQuizLobby(username, user, screen, display_surface)
    studentCustomQuizMenu.loadAssets()

    # Student Custom Lobby Object
    teacherCustomQuizMenu = teacherCustomQuizLobby.TeacherCustomQuizLobby(username, user, screen, display_surface)
    teacherCustomQuizMenu.loadAssets()

    #Profile Object
    profileObject = profile.Profile(username, user, display_surface)

    # Create Profile Object
    mailBoxObject = mailboxPage.Mailbox(username, user, display_surface)

    #Create Quiz Level Object
    level = quizLevel.QuizLevel()

# Run until the user asks to quit
while running:
    # Display the different menus according to state.
    if state == 0:
        # Set done = false so to keep page refreshing 
        setattr(friendMenu, 'done', False)
        setattr(uploadAssignment, 'done', False)
        menu.display()
    elif state == 1:
        worldSelect.display()
    elif state == 2:
        if(getattr(register, 'backToLogin') or getattr(recover, 'backToLogin') or getattr(register, 'successfulRegister') or getattr(recover, 'successfulRecover')):
            setattr(login, 'done', False)
        login.display()
        if (getattr(login, 'done') and getattr(login, 'success')):
            username = getattr(login, 'username')
            user = getattr(login, 'user')
            recreateUIObj(username, user)
            state = 0
        elif (getattr(login, 'done') and getattr(login, 'registerClicked')):
            setattr(register, 'done', False)
            state = 6
        elif (getattr(login, 'done') and getattr(login, 'recoverClicked')):
            setattr(recover, 'done', False)
            state = 9
    elif state == 3:
        if level.display(username, getattr(worldSelect, 'worldSelected'), getattr(worldSelect, 'levelSelected')):
            leaderBoard.loadAssets()
            state = 1
    elif state == 4:
        leaderBoard.display()
    elif state == 5:
        friendMenu.display()
        if (getattr(friendMenu, 'done')):
            state = 0
    elif state == 6:
        register.display()
        if (getattr(register, 'done')):
            state = 2
            login.registerClicked = False
    elif state == 7:
        if (getattr(uploadAssignment, 'done')):
            state = 0
        uploadAssignment.display()
    elif state == 8:
        setattr(studentCustomQuizMenu, 'reload', True)
        studentCustomQuizMenu.display()
    elif state == 9:
        recover.display()
        if (getattr(recover, 'done')):
            state = 2
            login.recoverClicked = False
    elif state == 10:
        setattr(teacherCustomQuizMenu, 'reload', True)
        teacherCustomQuizMenu.display()
    elif state == 11:
        teacherReport.display()
    elif state == 12:
        teacherClass.display()
    elif state == 13:
        profileObject.display()
    elif state == 14:
        setattr(mailBoxObject, 'reload', True)
        mailBoxObject.display()
    elif state == -1:
        running = False
 
    # When user clicks the window close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("CLICKED")
            running = False
        # When user clicks
        if event.type == MOUSEBUTTONDOWN:
            if state == 0:
                state = menu.action()
            elif state == 1:
                state = worldSelect.action()
            elif state == 4:
                state = leaderBoard.action()
            #elif state == 5:
                #state = friendMenu.action()
            #elif state == 6:
                #state = register.action()
            #elif state == 2:
                #state = login.action()
            #elif state == 7:
                #state = uploadAssignment.action()
            elif state == 8:
                state = studentCustomQuizMenu.action()
            elif state == 10:
                state = teacherCustomQuizMenu.action()
            elif state == 11:
                state = teacherReport.action()
            elif state == 12:
                state = teacherClass.action()
            elif state == 13:
                state = profileObject.action()
            elif state == 14:
                state = mailBoxObject.action()
                
        # Draws the surface object to the screen.   
        pygame.display.update()

    # Fills the screen with colour
    screen.fill(white)

# Done! Time to quit.
pygame.quit()
quit()

