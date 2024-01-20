# Class 6: More advanced screen materials

# GOAL: Creating a basic experiment using the psychopy package


################ Imports ############
from psychopy import visual, core


########### Experiment functions ##############
def drawRectangle(win):
    """
    Review from last time: how do we draw a rectangle??
    """
    print("drawing a rectangle!")

def drawRectangles(win):

    """
    part 1: how do we draw multiple things at once?
    """
    print("drawing rectangles!")
    pass

def drawImage(win):

    """
    part 2: how do we draw images?
    """
    print("drawing image!")
    
def clearScreen(win):
    print('Clearing screen')
    win.flip()
    
def drawText(win):
    text = visual.TextStim(win, text='RED')
    text.draw()
    win.flip()
    print('Drawing text')
    

"""
part 3: changing feedback based on response
"""
def collectResponse():
    print('Collecting a response')
    
def showFeedback(win):
    text = visual.TextStim(win, text='Correct')
    text.draw()
    win.flip()
    print('Showing feedback')

def wait(n):
    core.wait(n)


############ Experiment Scaffold ####################
"""
    Review from last time: how do we open up a new window??
"""

nTrials = 5
for trial in range(nTrials):
    print('Trial {}'.format(trial+1))
    
    drawRectangle(win)
    wait(1)
    clearScreen(win)
    wait(3)
    drawText(win)
    wait(2)
    collectResponse()
    showFeedback(win)
    wait(1)

win.close()
core.quit()

# -------------------------------------------------------------------------------------------------------------------

# EXERCISE 1:
# Create a task flow with the person next to you, based on the following experiment. 
# Just write the task flow, no need to define the actual functions, but you can if you have time.
#
# for 10 trials in a row:
#   First participants will see a fixation cross ('+') for 1.5 seconds
#   Next, participants will view a picture of a dog or cat for 3 seconds
#   Next participants will press a button if it is a dog or cat ('z' or 'm')
#   Finally, we'll give them feedback based on if they are correct or not for 1 second (if resp matches stim)

# SOLUTION: (will vary based on preference)


# nTrials = 5
# for i in range(nTrials):
#     drawFixation()
#     wait(1.5)
#     stim = chooseDogOrCat()
#     drawImage(stim)
#     response = recordButtonPress()
#     feedback = getFeedback(stim, response)
#     drawFeedback(feedback)



# -------------------------------------------------------------------------------------------------------------------

# Comment out PART 3 before proceeding....

# -------------------------------------------------------------------------------------------------------------------

# EXERCISE 2:
# We are creating an MRI experiment, looking at the brain activity when people view squares versus circles
# There are no responess in this task, participants are just passively viewing the screen
#
# Create a task flow for and fill in the functions for the following experiment. There are no responess in this task
# First, participants will view a fixation cross ('+') for 5 seconds
# Then, they will do, for nTrials = 5 trials:
#   they will see a fixation cross for 1.5 seconds
#   they will see either a red square or a red circle, depending on a random coin flip for that trial,, for 2 seconds
# finally, they will see a fixation cross for 5 seconds
#
# SOLUTION: (will vary based on preference)


# nTrials = 5
# for i in range(nTrials):
#     drawFixation()
#     core.wait(1.5)
#     shape = chooseShape()
#     drawShape(shape)
#     core.wait(2)
#     drawFixation()
#     core.wait(5)
