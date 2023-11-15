# standard imports
from dataclasses import dataclass
from re import A

# third-party imports
from PyQt6.QtWidgets import QLabel, QMessageBox, QWidget, QFileDialog, QPushButton
from PyQt6.QtGui import QPixmap, QImage, QIcon, QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QSize
import numpy as np
import cv2 as cv

# local imports
from config.globals import Assets
from logic.intel_sc import *


@dataclass
class ImageBuffer(QLabel):
    '''
    Image buffer class reference to the image buffer of the application.

    It implements the RUD (Read, Update, Delete) operations of the image buffer.

    The Create (save image) operation is handled by the Visualizer class because it's the one that contains the image buffer.
    '''
    # * Interaction buttons
    import_button: QPushButton
    delete_button: QPushButton
    replace_button: QPushButton
    img_path: str = Assets.TEST_IMAGES.value+'lenna.png'  # default image


    def __init__(self, parent: QWidget, width: int = 512, height: int = 512):
        super().__init__(parent)  # initialize the parent class
        self.setProperty('class', 'image_buffer')
        self.setFixedSize(width, height)
        self._set_buttons()

        # self.set_image()  # * set a default image (for testing purposes)


    # # * READ
    def import_image(self):
        '''
        Open a file dialog to select an image.

        If the selected image is valid, it will update the image path of the image buffer.  

        If it's not valid, it will show an error message and do nothing. So the `image_path` will not be updated.

        ## Returns:
            - bool: `True` if the image is valid, `False` otherwise
        '''
        # todo: Make "lenna.png" the default image (selected when the dialog is opened)
        img_path = QFileDialog.getOpenFileName(self, 
            'Open File',  # title
            Assets.TEST_IMAGES.value,  # initial dir
            'Image Files (*.bmp  *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm)',  # filter
        )[0]  # get the path of the selected image

        match img_path:  # check if the image is valid
            case '':  # if the image is not valid, show an error message
                print('\033[31mError: No file selected!\x1B[37m')
                QMessageBox.critical(self, 'Error', 'Please select a file.')
            case _:  # if the image is valid, show the image info
                self.img_path = img_path.split('image_alchemy')[1][1:]  # get the relative path of the selected image
                self.set_image()


    # * UPDATE
    def set_image(self):
        '''
        Set the image buffer to a specific image.
        
        ## Arguments:
            - img_path: `str`: the path of the image
        '''
        height, width, _ = cv.imread(self.img_path).shape  # get the image info
        print(f"Selected: \033[32m{self.img_path}\x1B[37m")
        print(f"     Shape: ({height}, {width}) = {height*width} pixels")
        self.setPixmap(QPixmap(self.img_path))  # set the image buffer to the selected image
        # self.setFixedSize(width, height)  # update the size of the image buffer
        self.setScaledContents(True)  # strecth the image to fit the image buffer

        self.import_button.hide()
        self.delete_button.show()
        self.replace_button.show()


    # * DELETE
    def remove_image(self):
        '''
        Remove the image buffer from the file system.
        '''
        print(f"\033[31mRemoved\x1B[37m image (\033[34m{self.img_path}\x1B[37m)")
        self.img_path = ''
        self.pix_data_map = QPixmap(512, 512)
        self.pix_data_map.fill(Qt.GlobalColor.transparent)  # * This will be a pixmap with all values set as null (None)
        self.setPixmap(self.pix_data_map)

        #  * Update the buttons state
        self.delete_button.hide()
        self.import_button.show()
        self.replace_button.hide()
        # 


    # * Define an ImageBuffer button (import, replace, remove)
    def _define_img_button(self, icon_type: str, b_size: int = 72) -> QPushButton:
        '''
        Define a button with a specific icon.

        ## Arguments:
            - icon_type: the type of the icon (import, replace, remove)

        ## Returns:
            - the button instance
        '''
        button = QPushButton()
        button.setIcon(QIcon(Assets.ICONS.value+icon_type+'.png'))
        button.setIconSize(QSize((int)(b_size*0.8), (int)(b_size*0.8)))
        button.setFixedSize(b_size, b_size)
        button.setStyleSheet('QPushButton {background-color: white; border: 1px solid white; border-radius: 10%;} QPushButton:hover{background-color : lightgray;}')
        return button


    # * Set interaction Buttons (import, replace, remove)
    def _set_buttons(self):
        '''
        Set the buttons that interact with the ImageBuffer.
        
        The buttons are defined in the ImageBuffer class but the Workspace is the one that handles the buttons.
        '''
        self.import_button = self._define_img_button('import')
        self.import_button.clicked.connect(self.import_image)
        
        self.delete_button = self._define_img_button('remove', b_size=32)
        self.delete_button.clicked.connect(self.remove_image)
        self.delete_button.hide()

        self.replace_button = self._define_img_button('replace', b_size=32)
        self.replace_button.clicked.connect(self.import_image)
        self.replace_button.hide()
