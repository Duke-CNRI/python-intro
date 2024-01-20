#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:46:18 2022

@author: rmgeddert
"""

# Today we will be programming an experiment where participants need to respond whether a red square is located on the left or the right of the screen. 

from psychopy import visual, core, event
import random

# def getPositions():

# def drawSquares(positions):
    
# def clearScreen():
    
# def getResponse(s):

# def checkResponse(positions, response):

#def displayFeedback(positions, response):
    
win = visual.Window(size=(800, 800), color=([0, 0, 0]))

nTrials = 5
for i in range(nTrials):
    print(f'Trial {i + 1}')

win.close()
core.quit()
  