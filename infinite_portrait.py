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
    global song_selector
    global colour_selector
    global p

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
            screen.print_at(frame[l], 0, l, colours[colour_selector], 0, 0) 
        
        screen.refresh() # load buffer on screen

        time.sleep(0.1) # sleep for 0.1 second for a 10fps animation

        screen.clear_buffer(6, 1, 0) # clear what is in the buffer which by definition includes what's already on screen.

        frame_count = (frame_count + 1) % number_of_frames # move to the next frame mod number_of_frames

        # restart music if mediaplayer is not playing
        if not p.get_busy():
            p.unload()
            song_selector = (song_selector + 1) % len(music_selection) # rotate music
            p.load(music_selection[song_selector])
            p.play()
            colour_selector = (colour_selector + 1) % len(colours)



# global variables
number_of_frames = 144 # set number of frames
frame_count = 0 # global variable keeping track of where the animation praviously left off. 
colour_selector = 0 
colours = [7, 2, 3, 6,   3, 2, 7, 3,   5,   6, 3, 4, 3,    7,    6, 3, 2,   4, 7, 2,   7]
song_selector = 0 
music_selection = [
    
    "music\\1_elo_twilight.wav",
    "music\\2_scarborough_fair.wav",
    "music\\All_lovers_under_the_sky.wav",
    "music\\3_princess_of_the_moon.wav",

    "music\\4_les_vacances_au_bord_de_la_mer.wav",
    "music\\Eight_Melodies.wav",
    "music\\5_mebius.wav",
    "music\\6_soldiers_of_sorrow.wav",

    "music\\Le Festin Camille.wav",

    "music\\7_once_upon_a_memory.wav",
    "music\\L3_sea_of_the_stars.wav",
    "music\\8_once_upon_a_memory_again.wav",
    "music\\9_launch.wav",

    "music\\Still_Alive.wav",

    "music\\10_aurora.wav",
    "music\\11_seven_return_to_nebula_m78.wav",
    "music\\Kaiba_Never.wav",
    
    "music\\15_anya_by_the_stars.wav",
    "music\\13_two_shining_people.wav",
    "music\\14_beginning.wav",

    "music\\16_mib_finale.wav"
    
]


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

# load and play music
p = mixer.music
p.load(music_selection[song_selector])
p.play()

# construct screen and run the animation function
while True:
    Screen.wrapper(the_muse_comes_to_him)


    



