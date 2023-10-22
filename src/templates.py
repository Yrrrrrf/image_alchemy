# standard imports
from enum import Enum


class Template(Enum):
    '''
    This enum contains the templates for the images.

    The templates are used to create the Visualizer layout.

    A template is a list of coordinates that define the position of the image buffer's.
    '''
    SQUARE = lambda w, h, m: [
        [m, m, int(w-m*2), int(h-m*2)]
    ]
    TWO_COLUMNS = lambda w, h, m: [
        [m, m, int(w/2-m*1.5), int(h-m*2)],
        [int((w/2)+m/2), m, int(w/2-m*1.5), int(h-m*2)]
    ]
    THREE_COLUMNS = lambda w, h, m: [
        [m, m, int((w/3)-m*1.5), int(h-m*2)],
        [int((w/3)+m/2), m, int((w/3)-m*1.5), int(h-m*2)],
        [int((w/3)*2+m/2), m, int((w/3)-m*1.5), int(h-m*2)]
    ]
    TWO_ROWS = lambda w, h, m: [
        [m, m, int(w-m*2), int(h/2-m*1.5)],
        [m, int((h/2)+m/2), int(w-m*2), int(h/2-m*1.5)]
    ]
    THREE_ROWS = lambda w, h, m: [
        [m, m, int(w-m*2), int((h/3)-m*1.5)],
        [m, int((h/3)+m/2), int(w-m*2), int((h/3)-m)],
        [m, int((h/3)*2+m/2), int(w-m*2), int((h/3)-m*1.5)]
    ]
    TWO_ROWS_TWO_COLUMNS = lambda w, h, m: [
        [m, m, int(w/2-m*1.5), int(h/2-m*1.5)],
        [int((w/2)+m/2), m, int(w/2-m*1.5), int(h/2-m*1.5)],
        [m, int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)],
        [int((w/2)+m/2), int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)]
    ]
    # 2 columns. 1 image in the first row, 2 images in the second row
    ONE_TWO_ROWS = lambda w, h, m: [
        [m, m, int(w/2-m*1.5), int(h-m*2)],
        [int((w/2)+m/2), m, int(w/2-m*1.5), int(h/2-m*1.5)],
        [int((w/2)+m/2), int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)]
    ]
    # 2 columns. 2 images in the first row, 1 image in the second row
    TWO_ONE_ROWS = lambda w, h, m: [
        [m, m, int(w/2-m*1.5), int(h/2-m*1.5)],
        [m, int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)],
        [int((w/2)+m/2), m, int(w/2-m*1.5), int(h-m*2)]
    ]

    # TODO: Make a micro-template system

    # ROW_ define that the template will be defined by rows
    # then the number indicates the number of images in each row
    # Example: ROW_2121 will be a template with 4 rows, the first and third row will have 2 images and the second and fourth row will have 1 image

    # COL_ define that the template will be defined by columns
    # then the number indicates the number of images in each column
    # Example: COL_312 will be a template with 3 columns, the first column will have 3 images, the second column will have 1 image and the third column will have 2 images
