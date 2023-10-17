# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QLabel, QMessageBox, QWidget, QFileDialog, QFrame
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import numpy as np
import cv2 as cv

# local imports
from config.globals import Assets
from logic.intel_sc import *


@dataclass
# class ImageBuffer(QLabel, QPixmap):
class ImageBuffer(QLabel):
    # QLabel allows us to display images
    # QPixmap allows us to store images
    '''
    Image buffer class reference to the image buffer of the application.
    '''
    # img: np.ndarray  # the image
    # import_button: QWidget  # the import button
    # delete_button: QWidget  # the delete button
    # replace_button: QWidget  # the replace button

    # pix_data_map: QPixmap  # the image data
    # img_path: str = Assets.TEST_IMAGES.value+'lenna.png'  # the path of the image buffer
    # img_path: str =   # the path of the image buffer


    def __init__(self, parent: QWidget, width: int = 512, height: int = 512):
        '''
        Initialize the ImageBuffer class.

        ## Arguments:
            - parent: `QWidget`: the parent widget of the image buffer
            - width: `int`: the width of the image buffer
            - height: `int`: the height of the image buffer
        '''
        super().__init__(parent)  # initialize the parent class
        self.setFixedSize(width, height)
        self.setProperty('class', 'image_buffer')

        # pixmap = QPixmap(Assets.TEST_IMAGES.value+'lenna_gray.png')
        # pixmap = QPixmap(Assets.TEST_IMAGES.value+'lenna.png')
        # self.setPixmap(pixmap)

        # make the ImageBuffer invisible
        # self.setVisible(False)

        # & YESNT
        # self.update_image()  # * Make the default image appear (Lenna)


    # # * CREATE
    # def save_image(self):
    #     '''
    #     Save the image buffer to the file system.
    #     If the image is not valid, it will show an error message.

    #     The image is stored on the `TEMP_IMAGES` directory.
        
    #     ## Arguments:
    #         - img_path: `str`: the path of the image
    #     '''
    #     store_path = Assets.TEMP_IMAGES.value + 'stored_image.png'
    #     match self.pix_data_map.save(store_path):
    #         case True:  # if the image is valid, show the image info
    #             print(f"\033[32mSuccessfully\x1B[37m stored at: \033[34m{store_path}\x1B[37m")
    #         case False:  # if the image is not valid, show an error message
    #             print(f"\033[31mError storing img\x1B[37m")


    # # * READ
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
                self.update_image()

                # # Update the image buffer to show the selected image
                # self.img = cv.imread(self.img_path)  # read image with opencv
                # self.img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)  # convert image to RGB format
                # height, width, channel = self.img.shape  # get image infos
                # self.pix_data_map = QPixmap.fromImage(QImage(self.img.data, width, height, channel*width, QImage.Format.Format_RGB888))
                # self.setPixmap(self.pix_data_map)  # set pixmap to label widget
                # print(f"Selected: \033[32m{self.img_path}\x1B[37m")  # Print the image info
                

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
        # self.img = cv.imread(self.img_path)  # Create a np.ndarray object (contains image data)
        # self.cost_matrix = get_cost_matrix(self.img)  # Create a np.ndarray object (contains cost matrix data)
        # self.draw_shapes(self.pix_data_map)  # ^ draw shapes on the image

        self.setPixmap(self.pix_data_map)  # set the image buffer to the selected image


    # * DELETE
    def remove_image(self):
        '''
        Remove the image buffer from the file system.
        '''
        self.img_path = ''
        self.pix_data_map = QPixmap(512, 512)
        self.pix_data_map.fill(Qt.GlobalColor.transparent)  # * This will be a pixmap with all values set as null (None)
        self.setPixmap(self.pix_data_map)
        print(f"\033[32mSuccessfully\x1B[37m removed image")
