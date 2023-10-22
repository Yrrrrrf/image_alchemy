# standard imports
from dataclasses import dataclass
from typing import Callable

# third-party imports
from PyQt6.QtWidgets import QLabel, QTabWidget, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QPixmap
# import cv2 as cv

# local imports
from components.image_buffer import ImageBuffer
from config.globals import Assets
from templates import Template


@dataclass
class Visualizer(QLabel):
    '''
    This class contains one or more image buffer's, which are the images that are displayed in the workspace.
    The visualizer is the container of the image buffer's. 
    '''
    bg_pixmap: QPixmap  # the main pixmap of the visualizer (This will be the image that will be saved)
    images: list[ImageBuffer]


    def __init__(self, workspace: QWidget, width: int = 512, height: int = 512, border: int = 32):
        super().__init__(workspace)
        from templates import Template  # ^ AVOID 'General Type Issues' warning (not really necessary)

        self.setProperty('class', 'visualizer')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.setFixedSize(width, height)
        # self.setMargin(margin)  # Not uses because the QMargins can't be manipulated (paint on them)
        self.images = []
    
        # * Color the background
        self.bg_pixmap = QPixmap(self.width() + border * 2, self.height() + border * 2)
        self.bg_pixmap.fill(Qt.GlobalColor.transparent)
        self.setPixmap(self.bg_pixmap)

        # * Set the template
        template: Callable = Template.SQUARE
        # template: Callable = Template.TWO_COLUMNS

        self._set_template(template)  # also set a default ImageBuffer
        self._set_template(template, border)  # also set a default ImageBuffer

        # self.draw_images()


    def _set_template(self, template: Callable, border: int = 16):
        '''
        Set the template of the visualizer.
        The template is the layout of the image buffer's.

        Set a new template will delete all the image buffer's and create new ones.
        '''
        for image in self.images:
            image.close()
            self.images.remove(image)

        new_width, new_height = self.width() + border * 2, self.height() + border * 2
        
        for coors in template(new_width, new_height, border):
            self.images.append(ImageBuffer(self, coors[2], coors[3]))
            self.images[-1].move(coors[0], coors[1])  # Move the image buffer to the given coordinates

        self.setFixedSize(new_width, new_height)  # * Set the new size of the visualizer


    # def draw_images(self):
    #     '''
    #     Draw the images on the visualizer.
    #     '''
    #     # todo: paint the image on the Visualizer
    #     painter = QPainter(self.bg_pixmap)
    #     for image in self.images:
    #         painter.drawPixmap(image.x(), image.y(), image.pixmap())
    #         # QPainter(self.bg_pixmap).drawPixmap(image.x(), image.y(), image.pixmap())
    #         self.setPixmap(self.bg_pixmap)


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
        match self.pixmap().save(store_path):
            case True:  # if the image is valid, show the image info
                print(f"\033[32mSuccessfully\x1B[37m stored at: \033[34m{store_path}\x1B[37m")
            case False:  # if the image is not valid, show an error message
                print(f"\033[31mError storing img\x1B[37m")
                # print(self.pixmap())


    def mousePressEvent(self, event):
        '''
        Print the pixel data of the image
        '''
        match event.buttons():
            case _:
                self.print_px_data(event)


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
        # if x < self.width() and y < self.height():
        r, g, b, a = self.pixmap().toImage().pixelColor(event.pos()).getRgb()
        print(f"\033[38;2;{r};{g};{b}m({x:4}, {y:4})\033[0mpx = ", end="")
        print(f"\033[38;2;255;0;0m{r:3}\033[0m, \033[38;2;0;255;0m{g:3}\033[0m, \033[38;2;0;0;255m{b:3}\033[0m"
            , f", \033[38;2;0;0;0m{a:3}\033[0m" if a != 255 else "")

        # PRINT SELF SIZE
        # print(self.width(), self.height())
        # # print size of the pixmap
        # print(self.pixmap().width(), self.pixmap().height())
