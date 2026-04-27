"""
File: flip_horizontally.py
Name: 
------------------------------------
This program demonstrates how to
create an empty SimpleImage and
produce a horizontally mirrored
version of poppy.png.

By copying pixels from the original
image to a new blank canvas, we will
practice basic image manipulation
and understand how pixel positions
can be transformed.
"""


from simpleimage import SimpleImage


def main():
    img = SimpleImage("images/poppy.png")
    img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
