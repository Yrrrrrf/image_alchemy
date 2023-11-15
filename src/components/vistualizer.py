# standard imports
from dataclasses import dataclass
from typing import Callable

# third-party imports
from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout
from PyQt6.QtGui import QCursor, QPixmap, QPainter, QColor, QPen
from PyQt6.QtCore import Qt
# import cv2 as cv

# local imports
# from logic.intel_sc import *  # for intelligent scissors algorithm implementation
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

    selected_image: ImageBuffer  # the image buffer that is selected (the one that is on top)


    def __init__(self, workspace: QWidget, width: int = 512, height: int = 512, border: int = 0, template: Callable = Template.SQUARE):
        super().__init__(workspace)

        self.setProperty('class', 'visualizer')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        # width = 500
        # height = 300
        
        self.setFixedSize(width, height)
        # self.setMargin(margin)  # Not uses because the QMargins can't be manipulated (paint on them)

        self.images = []  # * list of image buffer's
        border = 16  # * Border of the visualizer

        # * Color the background
        self.bg_pixmap = QPixmap(self.width() + border * 2, self.height() + border * 2)
        self.bg_pixmap.fill(Qt.GlobalColor.transparent)
        # self.bg_pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.bg_pixmap)

        # * Set the template
        template = Template.COL_21
        # template = Template.SQUARE_4

        self._set_template(template, border)

        self.update_pixmap()

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

        # ^ Draw the selected border
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


    def update_pixmap(self):
        '''
        Draw the images on the visualizer.
        '''
        # todo: paint the image on the Visualizer
        # painter = QPainter(self.bg_pixmap)
        for image in self.images:
            # todo: draw it only if the image have a pixmap (or if it is not empty)
            image.setPixmap(
                image.pixmap().scaled(
                    image.width(), 
                    image.height(), 
                    Qt.AspectRatioMode.IgnoreAspectRatio
                )
            )
            # print(image.pixmap().width(), image.pixmap().height())
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
        self.update_pixmap()  # Update the pixmap of the visualizer (to save the image)

        store_path = Assets.TEMP_IMAGES.value + file_name
        match self.pixmap().save(store_path):
            case True:  # if the image is valid, show the image info
                print(f"\033[32mSuccessfully\x1B[37m stored at: \033[34m{store_path}\x1B[37m")
            case False:  # if the image is not valid, show an error message
                print(f"\033[31mError storing img\x1B[37m")


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
                    # todo: This could be like selecting all to aplly a filter to all the images
                    # todo: Maybe this could be a new class (like a selector) that can select multiple images :O
                # print(self.selected_image)
                # print(type(self.selected_image))
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


    # def mousePressEvent(self, event):
    #     '''
    #     Print the pixel data of the image
    #     '''
    #     match event.buttons():
    #         # case _:
    #         case Qt.MouseButton.LeftButton:
    #             self.selected_image.print_px_data(event)
    #         # case Qt.MouseButton.RightButton:
    #             x, y = event.pos().x(), event.pos().y()
    #             if x < self.selected_image.width() and y < self.selected_image.height():
    #                 self.trace_points.append((x, y))  # add the point to the list
    #                 # r, g, b, _ = self.image_buffer.pixmap().toImage().pixelColor(x, y).getRgb()
    #                 # print(f"\033[38;2;{r};{g};{b}m({x:4}, {y:4})\033[0m")

    #                 # * Create a painter to draw on the image
    #                 painter = QPainter(self.selected_image.pix_data_map)
    #                 painter.setPen(QColor(0, 255, 0))

    #                 if len(self.trace_points) > 1:  # Do it only if there are at least 2 points
    #                     # * DRAW THE POINTS USING THE INTELIGENT SCISSORS ALGORITHM
    #                     # Get an image of the region of interest (rectangle of the last 2 points) + margin
    #                     margin = 60  # margin must be greater than 0 (otherwise it will crash)
    #                     x_0, y_0 = self.trace_points[-1]  # last point
    #                     x_1, y_1 = self.trace_points[-2]  # second to last point

    #                     x_min = max(0, min(x_0, x_1) - margin)
    #                     y_min = max(0, min(y_0, y_1) - margin)
    #                     x_max = min(self.selected_image.width(), max(x_0, x_1) + margin)
    #                     y_max = min(self.selected_image.height(), max(y_0, y_1) + margin)

    #                     roi = self.selected_image.cost_matrix[y_min:y_max, x_min:x_max]

    #                     for y, x in dijkstra(roi, (y_0-y_min, x_0-x_min), (y_1-y_min, x_1-x_min)):
    #                     # for y, x in find_minimum_cost_path(roi, (y_0-y_min, x_0-x_min), (y_1-y_min, x_1-x_min)):
    #                         painter.setPen(QColor(0, 255, 0))
    #                         painter.drawPoint(x_min+x, y_min+y)

    #                 circle_size: int = 10
    #                 painter.setPen(QColor(0, 0, 255))  # Draw a circle on the last point
    #                 painter.drawEllipse(self.trace_points[-1][0] - circle_size // 2, self.trace_points[-1][1] - circle_size // 2, circle_size, circle_size)
    #                 painter.drawEllipse(self.trace_points[-1][0] - circle_size // 2 + 1, self.trace_points[-1][1] - circle_size // 2 + 1, circle_size - 2, circle_size - 2)

    #             # * Update the image
    #             self.selected_image.setPixmap(self.selected_image.pix_data_map)
