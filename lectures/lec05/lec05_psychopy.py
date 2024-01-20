# Class 5: Basics of experimental design in PsychoPy

# GOAL: Creating a basic experiment using the psychopy package

# -------------------------------------------------------------------------------------------------------------------

# PART 1: Review and Basics

# 1. What is the differences between a .py file and a .ipynb file? Which is better for which circumstances?
# 2. How do I run .py files? How do I run them in a paticular conda environment, using a particular version of psychopy and python?
# 3. What is the difference between a function and a method?

# -------------------------------------------------------------------------------------------------------------------

# PART 2: Exercise 0

# Import the package `numpy` aliased as a variable called np
# Create a function called chooseNumber that takes an input N, and returns a random number between 0 and N inclusive
# Hint: google "numpy randint" to learn about the randint function.



# import numpy here


# define the function here


# call the function and print the result


# -------------------------------------------------------------------------------------------------------------------

# Comment out PART 2 before proceeding....

# -------------------------------------------------------------------------------------------------------------------

# PART 3: Introduction to Psychopy

# We are going to be creating a simple 1-back color memory task. 
# 
# For 5 trials in a row:
#
# Participants will first view a colored rectangle that is either red or blue, for 1 second
#
# |---------------|
# |      ___      |
# |     |___|     |
# |               |
# |---------------|
#
# Then, they will wait for 3 seconds while looking at a blank screen
#
# Then, they will see the word 'Red' or the word 'Blue', and they will have to indicate if the color word matches 
# or doesn't match the color of the rectangle they just saw. They will have 2 seconds to respond
#
# |---------------|
# |               |
# |      RED      |
# |               |
# |---------------|
#
# Finally, we will given them feedback if they responded correctly, for 1 second
#
# |---------------|
# |               |
# |    CORRECT    |
# |               |
# |---------------|
#
# In the future we'll incorporate the actual button responses to indicate yes or no, but for today we will focus on:
# 1. How do display the rectangle and text onto the screen using the psychopy visual module
# 2. How do wait for a given number of seconds using the psychopy core module
# 3. How to do the above in the context of a "TASK FLOW", which will help us organize our code using functions.
# 4. How to use np.random to randomly choose colors for each trial



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

