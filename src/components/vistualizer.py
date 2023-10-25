# standard imports
from dataclasses import dataclass
from types import NoneType
from typing import Callable

# third-party imports
from PyQt6.QtWidgets import QLabel, QTabWidget, QWidget, QGridLayout
from PyQt6.QtGui import QCursor, QPixmap, QPainter, QColor, QPen
from PyQt6.QtCore import Qt
# import cv2 as cv

# local imports
from components.image_buffer import ImageBuffer
from config.globals import Assets
# from templates import Template


@dataclass
class Visualizer(QLabel):
    '''
    This class contains one or more image buffer's, which are the images that are displayed in the workspace.
    The visualizer is the container of the image buffer's. 
    '''
    bg_pixmap: QPixmap  # the main pixmap of the visualizer (This will be the image that will be saved)
    images: list[ImageBuffer]

    selected_image: ImageBuffer  # the image buffer that is selected (the one that is on top)


    def __init__(self, workspace: QWidget, width: int = 512, height: int = 512, border: int = 0):
        super().__init__(workspace)
        from templates import Template  # ^ AVOID 'General Type Issues' warning (not really necessary)

        self.setProperty('class', 'visualizer')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.setFixedSize(width, height)
        # self.setMargin(margin)  # Not uses because the QMargins can't be manipulated (paint on them)

        self.images = []  # * list of image buffer's
        # border = 16  # * Border of the visualizer

        # * Color the background
        self.bg_pixmap = QPixmap(self.width() + border * 2, self.height() + border * 2)
        self.bg_pixmap.fill(Qt.GlobalColor.transparent)
        # self.bg_pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.bg_pixmap)

        # * Set the template
        template: Callable = Template.SQUARE
        # template: Callable = Template.COL_21
        # template: Callable = Template.SQUARE_4

        self._set_template(template, border)


    def _set_template(self, template: Callable, border: int):
        '''
        Set the template of the visualizer.
        The template is the layout of the image buffer's.

        Set a new template will delete all the image buffer's and create new ones.
        '''
        [image.deleteLater() for image in self.images]  # Delete all the image buffer's
        self.images.clear()  # Clear the list of image buffer's

        new_width, new_height = self.width() + border * 2, self.height() + border * 2

        for coors in template(new_width, new_height, border):
            self.images.append(ImageBuffer(self, coors[2], coors[3]))
            self.images[-1].move(coors[0], coors[1])  # Move the image buffer to the given coordinates

        self.setFixedSize(new_width, new_height)  # Set the new size of the visualizer
        self.selected_image = self.images[0]  # Set the selected image buffer
        # self.draw_selected_border()  # Draw the selected border


    def draw_selected_border(self):
        self.selected_border = QLabel(self)
        self.selected_border.setProperty('class', 'selected_border')
        self.selected_border.setFixedSize(self.selected_image.width(), self.selected_image.height())
        self.selected_border.move(self.selected_image.x(), self.selected_image.y())
        # red border
        self.selected_border.setStyleSheet('border: 2px solid red;')


    def update_selected_border(self):
        if self.selected_image != None:  # If there is a selected image buffer
            self.selected_border.move(self.selected_image.x(), self.selected_image.y())
            self.selected_border.setFixedSize(self.selected_image.width(), self.selected_image.height())


    def remove_selected_border(self):
        self.selected_border.deleteLater()



    def draw_images(self):
        '''
        Draw the images on the visualizer.
        '''
        # todo: paint the image on the Visualizer
        # painter = QPainter(self.bg_pixmap)
        for image in self.images:
            # painter.drawPixmap(image.x(), image.y(), image.pixmap())
            QPainter(self.bg_pixmap).drawPixmap(image.x(), image.y(), image.pixmap())
            self.setPixmap(self.bg_pixmap)


    # * CREATE
    def save_image(self, file_name: str = 'stored_image.png'):
        '''
        Save the image buffer to the file system.
        If the image is not valid, it will show an error message.

        The image is stored on the `TEMP_IMAGES` directory.
        
        ## Arguments:
            - img_path: `str`: the path of the image
        '''
        self.draw_images()

        store_path = Assets.TEMP_IMAGES.value + file_name
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
        x, y = event.pos().x(), event.pos().y()
        match event.buttons():
            case Qt.MouseButton.LeftButton:
                new_selected: ImageBuffer = self.childAt(x, y)  # type: ignore
                # * If the new selected item is an ImageBuffer, set it as the selected_image
                if type(new_selected) == ImageBuffer: self.selected_image = new_selected
                # if type(self.selected_image) == NoneType:  # Means that pressed on the background (self)
                #     pass
                    # todo: This could be like selecting all to aplly a filter to all the images
                    # todo: Maybe this could be a new class (like a selector) that can select multiple images :O

                # print(self.selected_image)
                print(type(self.selected_image))
                # self.update_selected_border()  # Update the selected border size & position
            case Qt.MouseButton.RightButton:
                self.print_px_data(x, y)
            case _:
                pass


    def print_px_data(self, x: int, y: int):
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
        r, g, b, a = self.pixmap().toImage().pixelColor(x, y).getRgb()
        print(f"\033[38;2;{r};{g};{b}m({x:4}, {y:4})\033[0mpx = ", end="")
        print(f"\033[38;2;255;0;0m{r:3}\033[0m, \033[38;2;0;255;0m{g:3}\033[0m, \033[38;2;0;0;255m{b:3}\033[0m"
            , f", \033[38;2;0;0;0m{a:3}\033[0m" if a != 255 else "")
        
        # x, y = event.pos().x(), event.pos().y()
        # # if x < self.width() and y < self.height():
        # r, g, b, a = self.pixmap().toImage().pixelColor(event.pos()).getRgb()
        # print(f"\033[38;2;{r};{g};{b}m({x:4}, {y:4})\033[0mpx = ", end="")
        # print(f"\033[38;2;255;0;0m{r:3}\033[0m, \033[38;2;0;255;0m{g:3}\033[0m, \033[38;2;0;0;255m{b:3}\033[0m"
        #     , f", \033[38;2;0;0;0m{a:3}\033[0m" if a != 255 else "")
