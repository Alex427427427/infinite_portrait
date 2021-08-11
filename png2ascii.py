# created by Alexander Li
# To convert a series of png files drawn using Microsoft paint, into ASCII strings.

from PIL import Image
import math
# NOTE: IF PIL NEEDS TO BE INSTALLED, INSTALL "pillow" INSTEAD. 

greyscale_70 = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?!lI-_+~<>i;:,\"^`'. "  # define 70 levels of brightness
greyscale_10 = "@%#*+=-:. "  # Define 10 levels of brightness


def ascii_content(image, greyscale: str) -> list:
    """ To translate a series of pixels into ascii, and present it as a 32_rows x 64_columns text string.

    :param greyscale: string containing ascii representation of brightness levels in ascending order
    :param image: opened and converted png file
    :return: list of strings, each string containing every ascii character for a line in a textfile
    """
    output = []
    pixel_array = image.load() # obtain pixel data array
    # for every y value (i.e. for every ROW)
    for y in range(image.size[1]): # image.size = [width, height]
        string = ""
        # for every pixel in the row...
        for x in range(image.size[0]):
            value = pixel_array[x, y] # 0 - 255 raw brightness value
            a = value[0]  # convert from tuple (immutable), to a float (now mutable)
            brightness_level = a / 255  # rescale it into a fraction

            # The brighter in the png, the brighter we want at the terminal -> the lesser the index within the greyscale
            access_index = math.floor((1 - brightness_level) * (len(greyscale) - 1))  # value of 0 - 69

            # append the ascii character representation of that pixel
            string += greyscale[access_index]

        string += "\n" # new line
        output.append(string)

    return output



# main
frame_count = 115 # set number of frames
image_names = []
output_files = []
# add all image names and filenames
for i in range(frame_count):
    image_names.append("png_frames\\AI" + str(i + 1) + ".png") # ["AI1.png", "AI2.png", ... ]
    output_files.append("ascii_frames\\AI" + str(i + 1) + ".txt") # ["AI1.txt", "AI2.txt", ... ]

# for every image...
for i in range(len(image_names)):
    # open image... convert to greyscale
    img = Image.open(image_names[i]).convert('LA')

    # convert its pixels into ascii using the function we wrote above
    content = ascii_content(img, greyscale_70)

    # Open new text file, write all content into it
    out = open(output_files[i], 'w')
    out.writelines(content)
    out.close()
