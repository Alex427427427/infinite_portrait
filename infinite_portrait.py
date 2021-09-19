"""
Created on 11/8/2021, by Alexander Li
Lightweight version, no music, no colour change.

"""
import time
import os
os.system("clear")

# set terminal window size in linux
import termios
import struct
import fcntl
def set_winsize(fd, row, col, xpix=0, ypix=0):
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=65, cols=128))



# global variables
number_of_frames = 144 # set number of frames
file_names = [] # list of files we will use to create the animation
frames = [] # this will contain a list, each element is a frame. Each frame is a LIST of lines

# add all filenames
for i in range(number_of_frames):
    file_names.append("ascii_frames/AI" + str(i + 1) + ".txt")


# for each filename
for name in file_names:
    # open the files and read lines. 
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())

# start animation, repeat indefinitely.
while True:
    # for each frame...
    for frame in frames:
        print("".join(frame)) # join everything into one string
        time.sleep(0.1) # sleep for 0.1 second for a 10fps animation
        os.system('clear') # clear screen

