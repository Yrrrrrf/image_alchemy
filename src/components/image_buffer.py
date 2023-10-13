# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QLabel, QMessageBox, QWidget, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import numpy as np
import cv2 as cv

# local imports
from config.globals import Assets
from logic.intel_sc import *

@dataclass
class ImageBuffer(QLabel):
    '''
    Image buffer class reference to the image buffer of the application.
    '''
    pix_data_map: QPixmap  # the image data
    img: np.ndarray  # the image
    # cost_matrix: np.ndarray  # the cost matrix

    img_path: str = Assets.TEST_IMAGES.value+'lenna.png'  # the path of the image buffer


    def __init__(self, parent: QWidget, width: int = 512, height: int = 512):
        '''
        Initialize the ImageBuffer class.

        ## Arguments:
            - parent: `QWidget`: the parent widget of the image buffer
            - width: `int`: the width of the image buffer
            - height: `int`: the height of the image buffer
        '''
        super().__init__(parent)
        self.setCursor(Qt.CursorShape.CrossCursor)
        self.setFixedSize(width, height)
        # style = 'QLabel {background-color: lightgray; border-radius: 10%;}'
        # hover_style = "QLabel:hover{background-color : lightgray; border : 1px solid gray;}"
        # self.setStyleSheet(style+hover_style)  # set the style of the image buffer

        # & YESNT
        # self.update_image()  # * Make the default image appear (Lenna)


    # * CREATE
    def save_image(self):
        '''
        Save the image buffer to the file system.
        If the image is not valid, it will show an error message.

        The image is stored on the `TEMP_IMAGES` directory.
        
        ## Arguments:
            - img_path: `str`: the path of the image
        '''
        store_path = Assets.TEMP_IMAGES.value + 'stored_image.png'
        match self.pix_data_map.save(store_path):
            case True:  # if the image is valid, show the image info
                print(f"\033[32mSuccessfully\x1B[37m stored at: \033[34m{store_path}\x1B[37m")
            case False:  # if the image is not valid, show an error message
                print(f"\033[31mError storing img\x1B[37m")


    # * READ
    def import_image(self):
        '''
        Open a file dialog to select an image.

        If the selected image is valid, it will update the image path of the image buffer.  
        
        If it's not valid, it will show an error message and do nothing. So the `image_path` will not be updated.
        
        ## Returns:
            - bool: `True` if the image is valid, `False` otherwise
        '''
        img_path = QFileDialog.getOpenFileName(self, 
            'Open File',  # title
            Assets.TEST_IMAGES.value,  # initial dir
            'Image Files ( *.bmp  *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm)'  # filter
        )[0]  # get the path of the selected image

        match img_path:  # check if the image is valid
            case '':  # if the image is not valid, show an error message
                print('\033[31mError: No file selected!\x1B[37m')
                QMessageBox.critical(self, 'Error', 'Please select a file.')
            case _:  # if the image is valid, show the image info
                # Return an error if the image is out of the root directory
                self.img_path = img_path.split('image_alchemy')[1][1:]  # get the relative path of the selected image
                self.update_image()  # Set the image buffer to the selected image


    # * UPDATE
    def update_image(self) -> None:
        '''
        Set the image buffer to a specific image.
        
        ## Arguments:
            - img_path: `str`: the path of the image
        '''
        height, width, _ = cv.imread(self.img_path).shape  # get the image info
        self.setFixedSize(width, height)  # update the size of the image buffer

        # Print the image info
        print(f"Selected: \033[32m{self.img_path}\x1B[37m")
        print(f"     Shape: ({height}, {width}) = {height*width} pixels")

        self.pix_data_map = QPixmap(self.img_path)  # Create a QPixmap object (contains image data)
        self.img = cv.imread(self.img_path)  # Create a np.ndarray object (contains image data)
        self.cost_matrix = get_cost_matrix(self.img)  # Create a np.ndarray object (contains cost matrix data)
        # self.draw_shapes(self.pix_data_map)  # ^ draw shapes on the image

        self.setPixmap(self.pix_data_map)  # set the image buffer to the selected image


    # ^ SOME EXTRA FEATURES ---------------------------------------------
    def print_px_data(self, event):
        '''
        Print the pixel data of the image at the given event position.
        Only if the click is inside the image.

        ## Args:
            - event (`QMouseEvent`): The mouse event that triggered the function.

        Prints the pixel data of the image at the given event position to the console.
        The pixel data is printed in the format (x, y)px = (r, g, b, a), where
        (x, y) is the position of the pixel, (r, g, b, a) are the red, green, blue,
        and alpha values of the pixel, respectively. The color values are printed
        in RGB format, with each value ranging from 0 to 255.
        '''
        x, y = event.pos().x(), event.pos().y()
        if x < self.width() and y < self.height():
            r, g, b, a = self.pixmap().toImage().pixelColor(event.pos()).getRgb()
            print(f"\033[38;2;{r};{g};{b}m({x:4}, {y:4})\033[0mpx = ", end="")
            print(f"\033[38;2;255;0;0m{r:3}\033[0m, \033[38;2;0;255;0m{g:3}\033[0m, \033[38;2;0;0;255m{b:3}\033[0m"
                , f", \033[38;2;0;0;0m{a:3}\033[0m" if a != 255 else "")
