# # Class 6: Basics of experimental design in PsychoPy
#
# # The main goal of today is to introduce some important building blocks when it comes to creating an
# # experiment in PsychoPy.
#
# # More specifically, we will:
# #    - Learn how to create stimuli
# #    - Learn how to display stimuli to the screen
# #    - Learn about randomization and counterbalancing
#
# # Lets get started!!!!
#
# # First we will learn how to create stimuli. Often in experiments, researchers will display different stimuli to the
# # screen for the participant to view and make a response.
#
# # For example, researchers who want to understand food preferences may display varying types of foods on the screen
# # and ask participants to select their preferences.
#
# # Before being able display stimuli on the screen, there are a few things we need to do.
#
# # The first step is importing the appropriate classes we will need. A reminder, classes contain their own set of
# # functions that will help us along the way.
#
# # For now, we will import the visual class from the library PsychoPy.
# # This class allows us to display different stimuli to the participant.
#
# # Below are some examples using the visual class:
#
# # visual.Window():                          setting up the screen on which you will display all of your stimuli
# # visual.TextBox():                         displaying text on your screen
# # visual.Circle():                          displaying circles on your screen
# # visual.RatingScale():                     display a rating scale to collect responses from
#
# # -------------------------------------------------------------------------------------------------------------------
#
# # The way these scripts will work will be different than how we're used to in Google Colab. When we run a .py script,
# # the ENTIRE script runs (not but the specific cell). This means that in order to move through this lecture, we will
# # be taking full advantage of comments (#). We will move through this lecture by slowly un-commenting lines of code
# # below so we can get a step-by-step sense of how we work with stimulus creation.
#
# # All of the code below is currently commented out. As we work through the script, you'll see "UNCOMMENT ME!" tags
# # above lines of code to uncomment as we move through.
#
# # Side note: a shortcut for commenting and un-commenting multiple lines of code is to select the code you want to
# # comment in or out and press 'Command' and '/'
#
To practice, comment
these lines of code out
which are not real lines of code
but me just typing out loud.
#
# # --------------------------------------------------------------------------------------------------------------------
#
# # UNCOMMENT ME: to import the visual class from main library, PsychoPy
# from psychopy import visual
#
# # We have imported the visual class!
# # Now, we need to create a screen so we can actually display our stimuli to the participant
#
# # UNCOMMENT ME: to create a window so we can display experiment.
# win = visual.Window() #  Note: "win" is commonly used to name the screen variable.
#
# # Let's run the script and see what happens!
# # Hopefully you were able to see a screen pop up! Let's next play with some of the arguments in the Window Function
# # to create something more custom
#
# # UNCOMMENT ME: to customize a window so we can display experiment.
# win = visual.Window(size=(800, 800), pos=(400, -300), color=([-0.5, 0.7, 0.7]))
# # full documentation for the many customizable elements of Window here: https://www.psychopy.org/api/visual/window.html
#
# # Now let's try to create our first stimulus!
# # Before we start, we'll comment out one of the windows so we don't dsiplay both to our screen everytime
#
# # UNCOMMENT ME: to create a circle using the Circle function
# my_circle = visual.Circle(win)
#
# # Cool. We've created the stimulus, but we still need to tell PsychoPy to actually display our stimulus.
# # To do this, we can use the draw function:
#
# # UNCOMMENT ME: to draw the circle
# my_circle.draw()
#
# # We also need to use the flip function.
# # PsychoPy has a buffer, meaning whatever is currently being drawn will be stored, but not actually displayed until...
# # we tell PsychoPy to "flip" the screen. Then, whatever is in the buffer is drawn.
#
# # UNCOMMENT ME: to reset the buffer
# win.flip()
#
# # Hmmmm. What happened?
# # Let's take a peak at the circle documentation: https://psychopy.org/api/visual/circle.html
#
# # UNCOMMENT ME X 3: to try our circl drawing again!
# my_circle = visual.Circle(win, fillColor='blue')
# my_circle.draw()  # draw the circle
# win.flip()  # flip window
#
# # We can also specify the amount of time we'd like to display the circle. To do this we need another class called Core.
# # The core class allows us to set, manipulate, and keep track of time in our experiment
#
# # UNCOMMENT ME: to import another class from the library PsychoPy
# from psychopy import core  # importing the core class
#
# # UNCOMMENT ME: to redraw the circle and have is appear for a longer interval
# my_circle.draw()  # draw the circle
# win.flip()  # flip window
# core.wait(2)  # wait 2 seconds before closing
#
# # Now let's try a text stim, a function to draw text to our screen!
#
# # UNCOMMENT ME x 4: to draw and display some text to the screen
# msg = visual.TextStim(win, text="Welcome to my experiment")  # create text stim
# msg.draw()  # draw text stim
# win.flip()  # flip the screen to display text stim
# core.wait(2)  # wait 2 seconds
#
# # Now let's try to draw TWO stimuli to the screen at the same time! What will we have to specify?
#
# # UNCOMMENT ME x 6: to draw and display two shapes onto our screen at the same time
# blue_rect = visual.Rect(win, fillColor='blue', pos=(-.4, 0))
# red_rect = visual.Rect(win, fillColor='red', pos=(.4, 0))
#
# blue_rect.draw()
# red_rect.draw()
# win.flip()
# core.wait(2)  # wait 2 seconds
#
# # Notice that as we build things onto the screen using .draw(), .flip(), we are cycling through the different
# # elements in a sequential order. This can be leveraged to help you advance from one screen to another in your exp.
#
# # --------------------------------------------------------------------------------------------------------------------
# # Now that we have some experience displaying stimuli, let's talk about randomization and counterbalancing.
#
# # Randomization is used in several ways during research experiments. In brief, randomization is when participants are
# # assigned by chance to different groups, treatments, or interventions in a study.
#
# # A classic example of randomization is during a clinical drug trial in which half the participants are randomly
# # assigned to receive the actual drug and the other half receive a placebo.
#
# # Randomization is important because we want to ensure that the observed behavior in the task is due to an
# # experimental factor and not an external factor.
#
# # Now let's apply this technique. Let's say we have an experiment in which we want to understand how a participant's
# # motivational state is effected by reading different key words on the screen.
#
# # We can create two conditions, one where the keywords may be related to feelings of motivations and another condition
# # that acts as a control
#
# # UNCOMMENT ME x 2: to create our condition text stimuli
# motivational_words = visual.TextStim(win, text="success, growth, achievement, accomplish")
# control_words = visual.TextStim(win, text="block, water, table, cloud")
#
# # UNCOMMENT ME: to import the random module which help us do random things...
# import random
#
# # UNCOMMENT ME x 6: to create a list with the stim, shuffle that list and display it to the screen!
# stim_list = [motivational_words, control_words]
# random.shuffle(stim_list) # shuffle the list
# stim_to_draw = stim_list[0] # select the first element for the list
#
# stim_to_draw.draw()
# win.flip()
# core.wait(2)
#
# # But what if we want to show BOTH conditions to the same participant but in a random order?
#
# # UNCOMMENT ME x 8: to create separate conditions with the motivational words and with the control words
# condition_one = stim_list[0] # select the first element for the list
# condition_two = stim_list[1] # select the second element for the list
#
# condition_one.draw()
# win.flip()
# core.wait(2)
#
# condition_two.draw()
# win.flip()
# core.wait(2)
#
# # Cool! But let's break this down?
#
# # 1. We created two text variables using the visual.Text function and put both of those elements into a list
# # 2. We then randomly shuffled the list and then chose the first element of the list to draw first
# # 3. We then chose the second element of the list and drew that to the screen.
#
# # By doing this, we counterbalanced conditions. Counterbalancing is the systematic variation of conditions in a study.
# # Similar to randomization, counterbalanacing is also important because it ensures that the observed behavior in
# # the task is due to an experimental factor and not an external factor.
#
# # In this example, we counterbalance the order of conditions, meaning some participants may see the motivational
# # condition first while others may see the control. This allows us to avoid potential order effects, meaning we
# # know the results are not due to the order in which they were presented.
#
# # Now, let's go back to our example of drawing two stimuli on the screen simultaneously. For example, we can again
# # draw the blue rectangle and the red rectangle...
# # but this time, maybe the participant is told that each rectangle represents a certain reward value and they are to
# # choose to the better one.
#
# # What will we want to randomize here?
# # What will we want to counterbalance here?
#
# # Lets code this one together!!
#
# # START:
#
#
# # END:
#
# # EXTRA!
#
# # Now let's try to display some real world stimuli.
# # Head to google and download two images to the folder where this script lives.
# # Try to load these images into Psychopy and display them side by side.
#
# # UNCOMMENT ME: to load in the stimuli by defining image path
# food_image_1 = ('YOUR/PATH/TO/IMAGE/HERE/picture.png")
# food_image_2 = ('YOUR/PATH/TO/IMAGE/HERE/other_picture.png")
#
# # write code to display images
#
# # START:
#
#
# # END
#
# # Amazing. Today we learned how to create and display stimuli, as well as the importance and implementation of
# # randomization and counterbalancing.
#
# # For next time: We will learn how to collect and store keyboard responses and how to save and export data!
