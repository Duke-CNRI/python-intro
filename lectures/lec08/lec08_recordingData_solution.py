#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:46:18 2022

@author: rmgeddert
"""

# Today we will be programming an experiment where participants need to respond whether a red square is located on the left or the right of the screen. 

from psychopy import visual, core, event
import random
import os
import pandas as pd

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

def getImage(paths):

    random.shuffle(paths)

    return paths[0]

def drawImage(win,path):

    image = visual.ImageStim(win,path,size=1)
    image.draw()

    win.flip()
    
def clearScreen():
    win.flip()
    win.flip()
    
def getResponse(win,s):

    t = visual.TextStim(win,text='Press "z" for scooby-doo, "m" for droopy dog') #
    t.draw()
    win.flip()
    clock = core.Clock()
    resp = event.waitKeys(maxWait = s, keyList=['z','m'], timeStamped = clock)
    return resp

def checkResponse(stimulus, response):
    if 'Scooby-Doo' in stimulus:
        #red square is on the left
        return response[0][0] == 'z'
    else:
        #red square is on the right
        return response[0][0] == 'm'
    
def displayFeedback(win,stimulus, response):
    if response == None:
        feedback_text = "Too slow"
    elif checkResponse(stimulus, response):
        feedback_text = "Correct!"
    else:
        feedback_text = "Incorrect"
    
    feedback = visual.TextStim(win, text = feedback_text)
    feedback.draw() 
    win.flip()


results = {
    'id':[],
    'trial':[],
    'rt': [],
    'response':[],
    'stimulus':[],
    'correct':[]
}
pid = input('Please input participant ID: ')
imagePath = 'C:\\Users\\mdm124\\Desktop\\Classes\\CNRI Python\\lec8\\images'
paths = [os.path.join(imagePath,'Droopy_dog.png'),os.path.join(imagePath,'Scooby-Doo.png')]
    
win = visual.Window(size=(800, 800), color=([0, 0, 0]))

nTrials = 5
for i in range(nTrials):
    print(f'Trial {i + 1}')
    
    #determine which image to draw
    
    stimulus = getImage(paths)
    
    #now draw the squares, giving the shuffled positions as an argument
    drawImage(win,stimulus)
    core.wait(0.25)
    
    #wait for response, or max 2 seconds
    response = getResponse(win,2)
    print(response)
    #show feedback
    displayFeedback(win,stimulus, response)
    core.wait(2)
    
    clearScreen()
    core.wait(1)

    results['id'].append(pid)
    results['trial'].append(i+1)
    results['rt'].append(response[0][-1])
    results['response'].append(response[0][0])
    results['stimulus'].append(stimulus)
    results['correct'].append(checkResponse(stimulus,response))

print(results)

df = pd.DataFrame(results)
df.to_csv(f'{pid}_dogdata.csv')
win.close()
core.quit()
  