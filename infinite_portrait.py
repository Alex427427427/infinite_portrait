"""
Created on 11/8/2021, by Alexander Li
To understand the asciimatics library and create a new animation.
Improvements: 
    terminal starts with correct size
    allows music looping
    allows music selection
    colours
    better art
"""
from asciimatics.screen import Screen
import time
import os
# set command line to be correct size on start up
os.system("mode con cols=128 lines=64")
from pygame import mixer

mixer.init()

"""
colour and attributes are defined as below
COLOUR_BLACK = 0
COLOUR_RED = 1
COLOUR_GREEN = 2
COLOUR_YELLOW = 3
COLOUR_BLUE = 4
COLOUR_MAGENTA = 5
COLOUR_CYAN = 6
COLOUR_WHITE = 7
A_BOLD = 1
A_NORMAL = 2
A_REVERSE = 3
A_UNDERLINE = 4
code format:
screen.print_at(text, x, y, colour=7, attr=0, bg=0, transparent=False)
directly prints a line of ascii
screen.clear_buffer(fg, attr, bg)
This is the superior way to clear screen. 
Normal cls clears the whole screen immediately before the next frame loads.
This creates flickering during animation.
This method merely clears all ascii waiting in the buffer (which includes ascii currently
on screen), awaiting for the next frame to load into the buffer. 
And by the time the next frame is ready, and screen.refresh() is called,
it will directly draw the next frame. 
"""


def the_muse_comes_to_him(screen):
    """
    function called by Screen.wrapper() - which is a constructor for a Screen object,
    constructing it according to the needs in this function. 
    
    the function itself carries out the actual animation.
    """
    screen.clear() # the screen should be clean at the start

    global frame_count 

    while True:
        if screen.has_resized():
            # this is needed to deal with residual text when screen is resized.
            # the function destroys the current object, leaves the function, and recreates it 
            # in the outside while loop, seen below.
            screen.close()
            return

        frame = frames[frame_count] # pick out next frame
        # load text line by line into a BUFFER
        for l in range(0, len(frame)):
            screen.print_at(frame[l], 0, l, 7, 0, 0) 
        
        screen.refresh() # load buffer on screen

        time.sleep(0.1) # sleep for 0.1 second for a 10fps animation

        screen.clear_buffer(6, 1, 0) # clear what is in the buffer which by definition includes what's already on screen.

        frame_count = (frame_count + 1) % number_of_frames # move to the next frame mod number_of_frames




# global variables
number_of_frames = 144 # set number of frames
frame_count = 0 # global variable keeping track of where the animation praviously left off. 

file_names = [] # list of files we will use to create the animation
frames = [] # this will contain a list, each element is a frame. Each frame is a LIST of lines

# add all filenames
for i in range(number_of_frames):
    file_names.append("ascii_frames\\AI" + str(i + 1) + ".txt")


# for each filename
for name in file_names:
    # open the files and read lines. 
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())

# construct screen and run the animation function
while True:
    Screen.wrapper(the_muse_comes_to_him)


    
