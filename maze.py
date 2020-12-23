import os
import numpy as np
import cv2
import random
import vlc
import time
from termcolor import colored
# Colors format of opencv: BGR

cap = cv2.VideoCapture(0)
maxCamWidth = 640
maxCamheight = 480

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def printGameField(gameField, posX, posY):
    print(colored("---------------------------------------", 'green'))
    print(colored("|            Maze Runner!             |", 'green'))
    print(colored("---------------------------------------", 'green'))
    # how to change pixel color: frame[5, 5] = (0, 0, 255)
    (b, g, r) = frame[1, 1]
    # print("r: " , r , " b:" , b , " g:" , g) 
    for i in range(20):
        print()
        for j in range(20):
            if(i==posX and j==posY):
                print(colored("& ", 'yellow'), end='');
                continue
            print(gameField[i][j] + " ", end='');

    print();

def buildMaze(choosenMaze):
    game = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

    if choosenMaze=="1":
        game[1][16] = "#";
        game[1][17] = "#";
        game[1][18] = "#";
        game[2][0] = "#";
        game[2][1] = "#";
        game[2][3] = "#";
        game[2][4] = "#";
        game[2][5] = "#";
        game[2][7] = "#";
        game[2][8] = "#";
        game[2][9] = "#";
        game[2][10] = "#";
        game[2][11] = "#";
        game[2][12] = "#";
        game[2][14] = "#";
        game[3][1] = "#";
        game[3][3] = "#";
        game[3][4] = "#";
        game[3][5] = "#";
        game[3][11] = "#";
        game[3][12] = "#";
        game[3][13] = "#";
        game[3][14] = "#";
        game[3][15] = "#";
        game[3][16] = "#";
        game[3][17] = "#";
        game[4][3] = "#";
        game[4][4] = "#";
        game[4][8] = "#";
        game[4][9] = "#";
        game[4][13] = "#";
        game[4][14] = "#";
        game[4][16] = "#";
        game[4][17] = "#";
        game[5][1] = "#";
        game[5][2] = "#";
        game[5][3] = "#";
        game[5][4] = "#";
        game[5][5] = "#";
        game[5][6] = "#";
        game[5][7] = "#";
        game[5][8] = "#";
        game[5][9] = "#";
        game[5][10] = "#";
        game[5][11] = "#";
        game[5][13] = "#";
        game[5][14] = "#";
        game[5][17] = "#";
        game[6][1] = "#";
        game[6][2] = "#";
        game[6][13] = "#";
        game[6][14] = "#";
        game[6][15] = "#";
        game[6][16] = "#";
        game[6][17] = "#";
        game[6][18] = "#";
        game[7][1] = "#";
        game[7][2] = "#";
        game[7][4] = "#";
        game[7][6] = "#";
        game[7][7] = "#";
        game[7][8] = "#";
        game[7][9] = "#";
        game[7][10] = "#";
        game[7][11] = "#";
        game[7][14] = "#";
        game[7][15] = "#";
        game[7][16] = "#";
        game[7][17] = "#";
        game[7][18] = "#";
        game[8][4] = "#";
        game[8][10] = "#";
        game[8][11] = "#";
        game[8][12] = "#";
        game[9][2] = "#";
        game[9][4] = "#";
        game[9][6] = "#";
        game[9][7] = "#";
        game[9][8] = "#";
        game[9][10] = "#";
        game[9][11] = "#";
        game[9][12] = "#";
        game[9][13] = "#";
        game[9][14] = "#";
        game[9][15] = "#";
        game[9][16] = "#";
        game[9][17] = "#";
        game[10][2] = "#";
        game[10][4] = "#";
        game[10][6] = "#";
        game[10][7] = "#";
        game[10][8] = "#";
        game[10][11] = "#";
        game[10][17] = "#";
        game[11][2] = "#";
        game[11][4] = "#";
        game[11][6] = "#";
        game[11][7] = "#";
        game[11][8] = "#";
        game[11][9] = "#";
        game[11][10] = "#";
        game[11][11] = "#";
        game[11][13] = "#";
        game[11][15] = "#";
        game[11][17] = "#";
        game[12][1] = "#";
        game[12][2] = "#";
        game[12][4] = "#";
        game[12][7] = "#";
        game[12][11] = "#";
        game[12][13] = "#";
        game[12][15] = "#";
        game[12][17] = "#";
        game[13][1] = "#";
        game[13][2] = "#";
        game[13][4] = "#";
        game[13][5] = "#";
        game[13][6] = "#";
        game[13][7] = "#";
        game[13][9] = "#";
        game[13][10] = "#";
        game[13][11] = "#";
        game[13][13] = "#";
        game[13][15] = "#";
        game[13][17] = "#";
        game[14][1] = "#";
        game[14][4] = "#";
        game[14][5] = "#";
        game[14][6] = "#";
        game[14][11] = "#";
        game[14][13] = "#";
        game[14][15] = "#";
        game[14][17] = "#";
        game[15][1] = "#";
        game[15][3] = "#";
        game[15][4] = "#";
        game[15][5] = "#";
        game[15][6] = "#";
        game[15][8] = "#";
        game[15][9] = "#";
        game[15][11] = "#";
        game[15][13] = "#";
        game[15][15] = "#";
        game[15][17] = "#";
        game[16][1] = "#";
        game[16][3] = "#";
        game[16][4] = "#";
        game[16][5] = "#";
        game[16][6] = "#";
        game[16][8] = "#";
        game[16][9] = "#";
        game[16][11] = "#";
        game[16][13] = "#";
        game[16][15] = "#";
        game[16][17] = "#";
        game[16][18] = "#";
        game[17][1] = "#";
        game[17][8] = "#";
        game[17][9] = "#";
        game[17][13] = "#";
        game[17][15] = "#";
        game[17][17] = "#";
        game[17][18] = "#";
        game[18][1] = "#";
        game[18][3] = "#";
        game[18][4] = "#";
        game[18][5] = "#";
        game[18][6] = "#";
        game[18][10] = "#";
        game[18][11] = "#";
        game[18][12] = "#";
        game[18][13] = "#";
        game[18][14] = "#";
        game[18][15] = "#";
    if(choosenMaze=="2"):
        x = 0
    if(choosenMaze=="3"):
        x = 0

    return game

def possiblePlay(gameField, posX, posY, direction):

        if direction=="A":
            if posX == 1 and posY == 0:
                return False
            if gameField[posX][posY-1]==" ": 
                return True;
            return False;
        if direction=="S":
            if gameField[posX+1][posY]==" ":
                return True;
            return False;
        if direction=="D":
            if gameField[posX][posY+1]==" ":
                return True;
            return False;
        if direction=="W":
            if gameField[posX-1][posY]==" ": 
                return True;
            return False;
        
        return False;

def randomplay():
    # test function
    randomNumberDirection = random.randint(1,4)
    if randomNumberDirection==1:
        return "A"
    if randomNumberDirection==2:
        return "S"
    if randomNumberDirection==3:    
        return "D"
    if randomNumberDirection==4:
        return "W"

def checkPlay():
    
    # rec2_pt1 = (482, 206)
    # rec2_pt2 = (572, 272)
    correctPixelCountRight = 0;
    for i in range(482, 572):
        for j in range(206, 272):
            (b, g, r) = frame[j, i]
            if b<=50 and g<=50 and r>=110:
                correctPixelCountRight = correctPixelCountRight + 1;

    # rec1_pt1 = (70, 206)
    # rec1_pt2 = (156, 272)
    correctPixelCountLeft = 0;
    for i in range(70, 156):
        for j in range(206, 272):
            (b, g, r) = frame[j, i]
            if b<=50 and g<=50 and r>=110:
                correctPixelCountLeft = correctPixelCountLeft + 1;

    # rec4_pt1 = (276, 364)
    # rec4_pt2 = (362, 430)           
    correctPixelCountDown = 0;
    for i in range(276, 362):
        for j in range(364, 430):
            (b, g, r) = frame[j, i]
            if b<=50 and g<=50 and r>=110:
                correctPixelCountDown = correctPixelCountDown + 1;

    # rec3_pt1 = (276, 50)
    # rec3_pt2 = (362, 116)            
    correctPixelCountUp = 0;
    for i in range(276, 362):
        for j in range(50, 116):
            (b, g, r) = frame[j, i]
            if b<=50 and g<=50 and r>=110:
                correctPixelCountUp = correctPixelCountUp + 1;

    maxPixels = max(correctPixelCountRight, correctPixelCountLeft, correctPixelCountDown, correctPixelCountUp);
    if(maxPixels==correctPixelCountRight and maxPixels>1000):
        return "D"
    if(maxPixels==correctPixelCountLeft and maxPixels>1000):
        return "A"
    if(maxPixels==correctPixelCountDown and maxPixels>1000):
        return "S"
    if(maxPixels==correctPixelCountUp and maxPixels>1000):
        return "W"

# theme song
p = vlc.MediaPlayer("song.mp3")
p.play()

# resize terminal
os.system('mode con: cols=42 lines=30')

clearConsole()

# Important Variables
actualPosition_X = 1;
actualPosition_Y = 0;
finalPosition_X = 18;
finalPosition_Y = 19;

# Game presentation and maze choice
print();
print(colored("---------------------------", 'green'));
print(colored("| Welcome to Maze Runner! |", 'green'));
print(colored("---------------------------", 'green'));
print();
print("Please, select the Maze you want to play.");
print("Insert a number from 1 to 3: ")
choosenMaze = input()

# Building Maze
gameField = buildMaze(choosenMaze);

# performance control
performanceControl = 0

# Let's start playing!
clearConsole()
while(True):

    if(actualPosition_X == finalPosition_X and actualPosition_Y == finalPosition_Y):
        break

    # Capture frame-by-frame
    ret, frame = cap.read()

    # flip
    frame = cv2.flip(frame, 180) 

    # rectangle LEFT
    rec1_pt1 = (70, 206)
    rec1_pt2 = (156, 272)
    rec1 = cv2.rectangle(frame, rec1_pt1, rec1_pt2, (180,105,255), 3)

    # rectangle RIGHT
    rec2_pt1 = (482, 206)
    rec2_pt2 = (572, 272)
    rec2 = cv2.rectangle(frame, rec2_pt1, rec2_pt2, (0,0,250), 3)

    # rectangle UP
    rec3_pt1 = (276, 50)
    rec3_pt2 = (362, 116)
    rec3 = cv2.rectangle(frame, rec3_pt1, rec3_pt2, (0,128,0), 3)

    # rectangle DOWN
    rec4_pt1 = (276, 364)
    rec4_pt2 = (362, 430)
    rec4 = cv2.rectangle(frame, rec4_pt1, rec4_pt2, (255,144,30), 3)

    # center circle
    center = (320, 240)
    radius = 60
    circle = cv2.circle(frame, center, radius, (255,255,255), thickness=3, lineType=8, shift=0) 

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    clearConsole()
    printGameField(gameField, actualPosition_X, actualPosition_Y)

    # performance control
    if(performanceControl<20):
        performanceControl = performanceControl + 1;
        continue;
    performanceControl = 0;
            
    chooseDirection = checkPlay()

    if chooseDirection=="A":
        if possiblePlay(gameField, actualPosition_X, actualPosition_Y, "A"): 
            actualPosition_Y = actualPosition_Y-1;

    if chooseDirection=="S":
        if possiblePlay(gameField, actualPosition_X, actualPosition_Y, "S"):
            actualPosition_X = actualPosition_X + 1;

    if chooseDirection=="D":
        if possiblePlay(gameField, actualPosition_X, actualPosition_Y, "D"):
            actualPosition_Y = actualPosition_Y + 1;

    if chooseDirection=="W":
        if possiblePlay(gameField, actualPosition_X, actualPosition_Y, "W"):
            actualPosition_X = actualPosition_X - 1;


p.stop()

# win song
w = vlc.MediaPlayer("victory.mp3")
w.play()

clearConsole()
printGameField(gameField, actualPosition_X, actualPosition_Y)
print("---------------------------------------")
print("|                WINNER                |")
print("---------------------------------------")

# wait for music to end
time.sleep(6)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

w.stop()