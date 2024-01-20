#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:46:18 2022

@author: rmgeddert
"""

# Today we will be programming an experiment where participants need to respond whether a red square is located on the left or the right of the screen. 

from psychopy import visual, core, event
import random

def getPositions():
    positions = [-.3, .3]
    random.shuffle(positions)
    return positions

def drawSquares(win,positions):
    red_square = visual.Rect(win, width=0.4, height=0.4, fillColor="red", pos=(positions[0],0))
    blue_square = visual.Rect(win, width=0.4, height=0.4, fillColor="blue", pos=(positions[1],0))
    red_square.draw()
    blue_square.draw()
    win.flip()

########## Step 1: Get paths ##################
def getImage(paths):

    pass 

############ Step 2: Draw image #############
def drawImage(win,path):

    pass
    
def clearScreen():
    win.flip()
    win.flip()
    
def getResponse(s):
    clock = core.Clock()
    resp = event.waitKeys(maxWait = s, keyList=['z','m'], timeStamped = clock)
    return resp


############# Step 3: Update checkResponse ###########
def checkResponse(positions, response):
    if positions[0] == -.3:
        #red square is on the left
        return response[0][0] == 'z'
    else:
        #red square is on the right
        return response[0][0] == 'm'
    
def displayFeedback(positions, response):
    if response == None:
        feedback_text = "Too slow"
    elif checkResponse(positions, response):
        feedback_text = "Correct!"
    else:
        feedback_text = "Incorrect"
    
    feedback = visual.TextStim(win, text = feedback_text)
    feedback.draw() 
    win.flip()
    
win = visual.Window(size=(800, 800), color=([0, 0, 0]))

nTrials = 5

#### set up image paths ####

##### Set up data recording here #####

for i in range(nTrials):
    print(f'Trial {i + 1}')
    
    #determine which stimulus to display (update this)
    positions = getPositions()
    
    #draw the image (update this)
    drawSquares(win,positions)
    
    #wait for response, or max 2 seconds
    response = getResponse(2)
    
    #show feedback
    displayFeedback(positions, response)
    core.wait(2)
    
    clearScreen()
    core.wait(1)

    ###### Record data ########

win.close()
core.quit()
  