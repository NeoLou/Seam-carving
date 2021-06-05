'''
Lab 7
=====

1. In this question, you will familiarize yourself with working with images using c_img.c and png2bin.py,
   files that were given to you as part of Project 2.

   You can make an image brighter by multiplying all the pixel values by a constant
   larger than 1; and you can make an image darker by multiplying all the pixel values
   by a constant smaller than one.

   c_img.c/c_img.h store reg/green/blue pixel values as uint8_t's -- values between 0
   and 255. If you are trying to make an image brighter, you may need to round the products
   you obtain by multiplying by a larger constant down to 255.

   Download the image

   https://www.president.utoronto.ca/secure-content/uploads/2017/09/UofTPresidentMericGertler-smaller.jpg

   Convert the image to a bin file using png2bin.py

   Write C code to create five different versions of the image at different levels of brightness.

2. Write Python code to find the cost of the minimum-energy seam in a list of lists.

energies = [[24,      22,      30,      15,      18,      19],
            [12,      23,      15,      23,      10,      15],
            [11,      13,      22,      13,      21,      14],
            [13,      15,      17,      28,      19,      21],
            [17,      17,      7,       27,      20,      19]]

    The correct output for the given energies data is 15+10+13+17+7 = 62.
'''

from png2bin import write_image, read_image
from PIL import Image

def create_png2bin(fname_in):
    img = Image.open(fname_in + ".png")
    write_image(img, fname_in + ".bin")

def create_bin2png(fname_in):
    img = read_image(fname_in + ".bin")
    img.save(fname_in + ".png")
    img.close()

def create_n_bin2png(fname_in, n):
    for i in range(n):
        img = read_image(fname_in + str(i) + ".bin")
        img.save(fname_in + "%d.png" %i)
        img.close()

def carve(data):
    if len(data) == 1:
        return min(data[0])
    w = len(data[0])
    for i in range(w):
        data[1][i] += min_prev(data, i)
    data.pop(0)
    return carve(data)

def neo_carve(data, i, j):
    h = len(data)
    w = len(data[0])
    if i == 0:
        return data[i][j]
    elif j == 0 and w >= 2:
        return data[i][j] + min(neo_carve(data, i-1, j), neo_carve(data, i-1, j+1))
    elif j == w - 1 and w >= 2:
        return data[i][j] + min(neo_carve(data, i-1, j-1), neo_carve(data, i-1, j))
    elif w == 1:
        return data[i][j] + neo_carve(data, i-1, j)
    return data[i][j] + min(neo_carve(data, i-1, j-1), neo_carve(data, i-1, j), neo_carve(data, i-1, j+1))

def min_prev(data, col):
    prev = data[0]
    w = len(prev)
    if col == 0 and w >= 2:
        return min(prev[0], prev[1])
    elif col == w-1 and w >= 2:
        return min(prev[w-1], prev[w-2])
    elif w == 1:
        return prev[0]

    return min(prev[col-1], prev[col], prev[col+1])

if __name__ == "__main__":
    #Problem 1

    #Creates meric.bin
    #create_png2bin("meric")
    #Go to C code to create meric1.bin, meric2.bin, etc.
    #Now convert bin2png
    #create_5_bin2png("meric")

    #Problem 2
    '''
    energies = [[24,      22,      30,      15,      18,      19],
                [12,      23,      15,      23,      10,      15],
                [11,      13,      22,      13,      21,      14],
                [13,      15,      17,      28,      19,      21],
                [17,      17,      7,       27,      20,      19]]
    h = len(energies)
    w = len(energies[0])
    for i in range(w):
        print(neo_carve(energies, 4, i))
    '''

    #Project 2
    #create_bin2png("test")
    create_n_bin2png("img", 20)
