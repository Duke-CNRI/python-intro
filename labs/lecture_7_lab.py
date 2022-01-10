# # Class 7: Collecting, storing, and saving in PsychoPy
# # Created by Ben Muzekari, edited by Abby Hsiung
#
# # Last class, we learned how to create stimuli, display these stimuli to the screen, and how to randomize and
# # counterbalance stimuli.
#
# # However, in experiments we often like to display stimuli AND collect responses from the participant.
#
# # Some common responses to collect are:
# #    1) The choice option (which option the participant chose)
# #    2) Reaction times (how quickly the participant chose)
#
# # Today, we will:
# #    - Learn how to collect keyboard responses
# #    - Learn how to store responses
# #    - Learn how save data
#
# # Lets get started!!!!
#
# # First, let's import the classes we will need. 
# # Last lesson, we learned about the visual class which allows us to display different stimuli to the participant,
# # and about the core class which allows us to set, manipulate, and keep track of time in our experiment.
#
# # Today, we will introduce two more classes that are required for building an experiment.
# # One of these classes is the event class. The event class allows us to track and allow for participant responses.
#
# # Below are some examples using the event class:
# # event.Mouse():         easy way to track what your mouse is doing
# # event.waitKeys():      wait for certain keyboard responses before moving on
# # event.getKeys():       returns a list of keys that were pressed
#
# # The way that we record and save data uses a new python library called pandas.
# # Pandas allows us to keep track and store relevant data in a data frame. More on this below!
#
# # -------------------------------------------------------------------------------------------------------------------
# # Great. Let's do some coding!
#
# # UNCOMMENT BELOW: to import the visual, core, event, and data classes
# from psychopy import visual, core, event, data
#
# # UNCOMMENT BELOW: to create a window so we can display experiment.
# win = visual.Window(size=(800, 800), pos=(400, -300), color=([-0.8, 0.2, 0.1]))
#
# # Now, let's set up a decision-making task where subjects are to choose from two stimuli on the screen.
# # Let's create a green triangle and an orange triangle. Hint: use the Polygon component.
#
# # UNCOMMENT BELOW: let's create the stimuli
# green_triangle = 
# orange_triangle = 
# 
# # We have created the stimuli, but since this is a decision-making task, we need to display both stimuli on the
# # screen simultaneously. Therefore, we need to specify the position of each stimuli. Ideally, we'd like to draw one
# # stimulus to the left of the screen and one to the right.
#
# # Last lesson, we also learned about the importance of randomization. Let's create a randomizer in which we can use
# # to randomize the location of each stimuli.
#
# # UNCOMMENT BELOW: to import the random module
# import random
#
# # Now, we will need to make a list containing two possible stimulus locations. Let's make one location (-.4, 0) and
# # the other location (.4, 0).
#
# # Then, let's shuffle the list using the random function and then assign the first position in the list to the green
# # triangle and the second to the orange triangle.
#
# # UNCOMMENT BELOW and code away.
# position_list =
#
# # shuffle the list here
# green_triangle_pos =                                              # select the first element of the position list
# orange_triangle_pos =                                            # select the second element of the position list
#
# # Awesome. Now we can assign each of our stimuli a position.
#
# # UNCOMMENT BELOW: to assign each stimulus to their position which was randomized above. How are we doing this?
# green_triangle.pos = green_triangle_pos
# orange_triangle.pos = orange_triangle_pos
#
# draw the green triangle
# draw the orange triangle
#
# flip the window
# wait 2 seconds
# 
# # NOW: Run the code and see what happens!
# # Note: If the stimuli are overlapping, try changing the size of both
#
# # -------------------------------------------------------------------------------------------------------------------
# # Now let's collect responses from the keyboard. First,
# # UNCOMMENT BELOW x 4: This help break up our script into separate parts
# fixation_cross = visual.TextStim(win, text = '+')
# fixation_cross.draw()
# win.flip()
# core.wait(2)
# 
# # Now, let's shuffle  the position list again, assign each stimulus a position, and draw the stimuli. You can copy
# # the code you've created above.
#
# # UNCOMMENT BELOW
# shuffle the list here
#
# green_triangle_pos =                                              # select the first element of the position list
# orange_triangle_pos =                                            # select the second element of the position list
#
# green_triangle.pos = green_triangle_pos
# orange_triangle.pos = orange_triangle_pos
#
# draw the green triangle
# draw the orange triangle
#
# flip the window
#
# # Now we have the same set-up as before. However, after we flip the window, there is a few things we want to do.
# # One of them is collect reaction item, since we want to know how quickly participants respond.
#
# # To do this, we can use the clock component from the core class
#
# # UNCOMMENT BELOW: to create the clock variable
# clock = core.Clock()
# # Note: the clock will start wherever we first create, so we are creating right after the window flips and the
# # trial starts
# 
# # Now we will create a variable that allows us to collect a keyboard response
# # We can do this by using event.waitKeys
#
# # The variable has been created for you below. However, some parameters need to specified:
# #     - Set the wait time to 5 seconds
# #     - Only look for input from the 'w' and 'o' keys. Participants will use 'w' if they want to select
# #       the stimulus on the left and 'o' if they want to select the stimulus on the right
# #     - Lastly use the timeStamped parameter and pass in the clock variable we created
#
# # Use the documentation as a guide: https://psychopy.org/api/event.html
#
# # UNCOMMENT DOWN x 2: to create keyboard variable
# resp_key = event.waitKeys() # Note: All of the parameters above should be placed here
# print(resp_key) # Let's also print the variable to the screen to see its output.
#
# # Now, run the code and try to make a decision!
#
# # What happened? Did it work? If so, your decision should have ended the trial. 
# # Check the output as well. We printed the resp_key, so we should get some information. 
# # Specifically, we should see a list that tells us which key was pressed as well as the reaction time. Do you see it?
#
# # Amazing! We collected a keyboard response and allowed the participant to make a decision to between stimuli.
# # However, sometimes in experiments, the stimuli may represent some reward value and depending on the choice of
# # the participant, they will receive some feedback about the outcome.
# # -------------------------------------------------------------------------------------------------------------------
#
# # For this lesson, let's say this is a learning task and the participant is attempting to choose the better stimulus.
# # One is a good stimulus and one is a bad stimulus. Then, depending on their choice, the participant receives feedback
# # as to whether they made a good choice or bad one.
#
# # UNCOMMENT BELOW to make a new trial.
# fixation_cross.draw()
# win.flip()
# core.wait(2)
#
# # Now, let's shuffle  the position list again, assign each stimulus a position, and draw the stimuli. You can copy
# # the code you've created above.
#
# # UNCOMMENT BELOW
# shuffle the list here
#
# green_triangle_pos =                                              # select the first element of the position list
# orange_triangle_pos =                                            # select the second element of the position list
#
# green_triangle.pos = green_triangle_pos
# orange_triangle.pos = orange_triangle_pos
#
# # Now, let's assign each stimulus to a condition. We can use counterbalancing to ensure the good and bad stimuli vary
# # between the green and orange triangle.
#
# # UNCOMMENT BELOW: to counterbalance the good and the bad stimulus
# stim_outcome_list =  # put two strings in this list, 'good' and 'bad'
#
# shuffle the list here
#
# green_triangle_outcome = # select the first element of the list
# orange_triangle_outcome = # select the second element of the list
#
# draw the green triangle
# draw the orange triangle
#
# flip the window
# print(green_triangle_outcome, orange_triangle_outcome)
#
# # Did the print statement print what you expected?
#
# # Great, now we are ready to create and if/else statement to identify which stimulus the participant chose and what
# # the outcome was. Remember when we printed the key_resp variable and the first element was the key pressed?
#
# # We will need to reference that key pressed by indexing the list. We will also need to know the position of the
# # stimulus and whether it was the good or bad stimulus.
#
# # Additionally, we will create a few empty variables so we can add info to them as we go through the if/else statement
#
# # UNCOMMENT BELOW: and complete the if/else statement
# feedback_text = [] # leave this empty
# stim_chosen = [] # leave this empty
#
# # things in [brackets] are verbal explanations of what the code should be
# if [key in response key list (indexed)]: # reference key pressed by indexing the list.
#    if [left triangle is green and the green triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'green_triangle'
#    elif [left triangle is orange and the orange triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'orange_triangle'
#    else:
#        feedback_text = 'bad choice :('
# elif [other key in response key list (indexed)]: # reference key pressed by indexing the list.
#    if [right triangle is green and the green triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'green_triangle'
#    elif [right triangle is orange and the orange triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'orange_triangle'
#    else:
#        feedback_text = 'bad choice :('
#
#
# Lastly, to display the feedback to participants, complete the statement below
#
# # Now, let's create the feedback text stim and pass our feedback_text variable as the text
#
# # UNCOMMENT ME: to create the feedback stim and draw it to the screen
# feedback = visual.TextStim(win, text = feedback_text)
# feedback.draw() # draw the feedback text to the screen
#
# win.flip() # flip the screen
# core.wait(2) # wait 2 seconds
#
# # UNCOMMENT ME to make a new trial.
# fixation_cross.draw()
# win.flip()
# core.wait(2)
#
# # Run the code! Did you get feedback about your decision? Did you make the right choice?!
# # -------------------------------------------------------------------------------------------------------------------
# # Cool. We have learned to collect a response from the keyboard and show feedback accordingly.
#
# # Now if we're interested in doing many trials of this and seeing if participants can learn which triangle is good and
# # which is bad, we might also have them rate their confidence of their choice. This can give us a measure of how well
# # people are learning across time!
#
# # Let's include a rating scale so after each choice but before feedback, participants rate how confident they are that
# # they chose to right triangle.
#
# # Hint: look at the documentation here: https://www.psychopy.org/api/visual/ratingscale.html
#
# # UNCOMMENT BELOW: and fill in the rest of the code!
#
# fixation_cross.draw()
# win.flip()
# core.wait(2)
#
# stim_outcome_list =  # put two strings in this list, 'good' and 'bad'
#
# shuffle the list here
#
# green_triangle_outcome = # select the first element of the list
# orange_triangle_outcome = # select the second element of the list
#
# draw the green triangle
# draw the orange triangle
#
# flip the window
# print(green_triangle_outcome, orange_triangle_outcome)
#
# # RATING SCALE GOES HERE!
# # First, set up the parameters of you confidence ratings scale
# min_confidence = ??
# max_confidence = ??
#
# # Next, identify that range of your confidence scale (make sure to add + 1 to your max to get the full range included)
# confidence_range = [range]
#
# # Next, identify the labels points you want to have on your rating scale on range 0 - 1
# label_points = # the fractions of the range you want to have labels at
#
# # Then determine the labels of your label_points (can be numbers (0, 5,..., 100) or words (low, medium, high))
# labels = # the actual text for each label
# ticks = [len(confidence_range) * point for point in label_points]  # the position along the track for each label
# ​​
# ratingScale = visual.RatingScale(win, choices=??, labels=??, tickMarks=??)
#
# # Next, set up the actual question you will be asking participants with TextStim
# scale_Q = visual.TextStim(win, "[Question to participants]")
#
# # Lastly, this loop will allow participants to select a rating and submit that rating (and we can record it!)
# while ratingScale.noResponse:
#     item.draw()
#     ratingScale.draw()
#     win.flip()
# rating = ratingScale.getRating()
#
# print(rating)
#
# feedback_text = [] # leave this empty
# stim_chosen = [] # leave this empty
#
# # things in [brackets] are verbal explanations of what the code should be
# if [key in response key list (indexed)]: # reference key pressed by indexing the list.
#    if [left triangle is green and the green triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'green_triangle'
#    elif [left triangle is orange and the orange triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'orange_triangle'
#    else:
#        feedback_text = 'bad choice :('
# elif [other key in response key list (indexed)]: # reference key pressed by indexing the list.
#    if [right triangle is green and the green triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'green_triangle'
#    elif [right triangle is orange and the orange triangle is good]:
#        feedback_text = 'good choice :)'
#        stim_chosen = 'orange_triangle'
#    else:
#        feedback_text = 'bad choice :('
#
#
# feedback = visual.TextStim(win, text = feedback_text)
# feedback.draw() # draw the feedback text to the screen
#
# win.flip() # flip the screen
# core.wait(2) # wait 2 seconds
#
# fixation_cross.draw()
# win.flip()
# core.wait(2)
#
# # -------------------------------------------------------------------------------------------------------------------
#
# # Great! We've learned how to collect keyboard responses and how to temporarily store and refer to those responses
# # The final lesson for today is how to save all of our data and export it. This way, we can analyze it later :)
# # First, let's examine an example with fake data
#
# # The pandas library is a python library used for data analysis. It allows us to convert our data into a lovely
# # dataframe, which facilitates data manipulation and analysis.
#
# # Before we get started saving data, let's first decide where we are going to save that data to (aka, the data needs
# 3 a place to live on your computer! It cannot live in PsychoPy!
#
# # First: create a folder in your CNRI folder where your psychopy scripts live, name it Data. Then find the path for
# # your Data folder (should be something like /Users/[your computer name]/[path to CNRI folder]/Data)
#
# # UNCOMMENT BELOW:
# import pandas as pd 
# subject_id = 999 # create a subject id num - this will be used to name our file
# output_path =  # set up your output path, i.e. where you'd like the data file to be exported (aka, the Data folder)
# save_name = # name the file by the subject id and then in a 'csv' format
# save_file = output_path + save_name # create full file path
#
# # Now, we need to decide what we want to put in our dataframes and how we want them to be organized. For typical
# # experiments, we organize our dataframes so that each column is a variable of interest (e.g., like the ratings, the
# # choices, the position of the two triangles, etc.) and each row represents a different trial the participants did.
#
# # So, because we know the variables that we want before collecting data, we can initial our dataframe with just the
# # names of the columns.
# output_file = pd.DataFrame(columns=[]) # fill in the columns=[] with the columns you want to have for data analysis
#
# # Now we'll create some fake data to put into our pandas data frame.
#
# num_fake_trials = ??
#
# for i in range(num_fake_trials):
#     output_file.loc[i] = [data for each column (ask for help on this once you've decided what columns you're including)]
#
# # The last thing you want to do is export your data into the Data folder so we can see our output in a clean and
# # organized way!
# output_file.to_csv(save_file, index = False) # export the data!
#
# # Now, check where you exported the data - do you see it? What is the layout like?
#
# # HOMEWORK: Awesome. Now that you know how to export data, copy the code from our decision-making task, but this time
# # try to export the real data from the task. Make the columns: which stimulus was chosen, the outcome, and the
# # reaction time.
#
# Code away below!
#
#
#
#
#
#
#
#
#
#
#
#