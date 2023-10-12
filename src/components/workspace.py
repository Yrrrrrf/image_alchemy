# This file contains the workspace component

# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtGui import QIcon, QPainter, QColor
from PyQt6.QtCore import QSize, Qt
import numpy as np
import cv2 as cv

# local imports
from config.globals import Assets
from components.image_buffer import ImageBuffer

from logic.intel_sc import *


@dataclass
class Workspace(QWidget):
    '''
    # This probably should hold an ImageVisualizer instead of an ImageBuffer
    # And the ImageVisualizer should hold one or more ImageBuffers (for the layers)
    # Also the ImageVisualizer should be responsible for managing all the ImageBuffers
    # And the Workspace should be responsible for managing all the ImageVisualizers
    # So, the Workspace can:
    #  - Create a new ImageVisualizer (with default templates)
    #  - Have another tab open (or another Widget)
    #  - Close a tab (or another Widget)
    #  - Focus on a tab (or another Widget)
    '''
    image_buffer: ImageBuffer


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'workspace')
        self.image_buffer = ImageBuffer(self)  # create an image label

        # * This is a temporary solution
        # * It's used to enable the MouseMoveEvent updates without clicking
        self.setMouseTracking(True)  # enable mouse tracking without clicking
        
        # todo: this shouln't be a class attribute
        # ^ I mean, this should be a local variable
        # ^ Just for testing purposes (it will be removed later) 
        self.trace_points = []  # create a list of the points
        # self.trace_points = [(0, 0)]  # create a list of the points

        # * Get a normalized version of the cost matrix (for debugging purposes)
        # * The original cost matrix is not normalized & it's not a good idea to display it
        # * Because it has values that are too low, so we can't really see anything
        normalized_cost_matrix = cv.normalize(self.image_buffer.cost_matrix, None, 0, 255, cv.NORM_MINMAX)  # type: ignore
        cv.imwrite(Assets.TEMP_IMAGES.value+'normalized_cost_matrix.png', normalized_cost_matrix)
        # cv.imshow('normalized_cost_matrix', normalized_cost_matrix)


    def mousePressEvent(self, event):
        '''
        Print the pixel data of the image
        '''
        match event.buttons():
            # case _:
            case Qt.MouseButton.LeftButton:
                self.image_buffer.print_px_data(event)
            # case Qt.MouseButton.RightButton:
                x, y = event.pos().x(), event.pos().y()
                if x < self.image_buffer.width() and y < self.image_buffer.height():
                    self.trace_points.append((x, y))  # add the point to the list
                    # r, g, b, _ = self.image_buffer.pixmap().toImage().pixelColor(x, y).getRgb()
                    # print(f"\033[38;2;{r};{g};{b}m({x:4}, {y:4})\033[0m")

                    # * Create a painter to draw on the image
                    painter = QPainter(self.image_buffer.pix_data_map)
                    painter.setPen(QColor(0, 255, 0))

                    if len(self.trace_points) > 1:  # Do it only if there are at least 2 points
                        # * DRAW THE POINTS USING THE INTELIGENT SCISSORS ALGORITHM
                        # Get an image of the region of interest (rectangle of the last 2 points) + margin
                        margin = 60  # margin must be greater than 0 (otherwise it will crash)
                        x_0, y_0 = self.trace_points[-1]  # last point
                        x_1, y_1 = self.trace_points[-2]  # second to last point

                        x_min = max(0, min(x_0, x_1) - margin)
                        y_min = max(0, min(y_0, y_1) - margin)
                        x_max = min(self.image_buffer.width(), max(x_0, x_1) + margin)
                        y_max = min(self.image_buffer.height(), max(y_0, y_1) + margin)

                        roi = self.image_buffer.cost_matrix[y_min:y_max, x_min:x_max]
                        # ^ for ROI debugging
                        # cv.imshow(f'roi_{len(self.trace_points)}', roi)
                        # print(f"ROI: ({x_min}, {y_min}) -> ({x_max}, {y_max})")
                        # width, height = roi.shape[:2]
                        # print(f"     Shape: ({height}, {width}) = {height*width} pixels")

                        for y, x in dijkstra(roi, (y_0-y_min, x_0-x_min), (y_1-y_min, x_1-x_min)):
                            painter.setPen(QColor(0, 255, 0))
                            painter.drawPoint(x_min+x, y_min+y)
                        # for y, x in find_minimum_cost_path(roi, (y_0-y_min, x_0-x_min), (y_1-y_min, x_1-x_min)):
                        #     painter.setPen(QColor(255, 0, 0))
                        #     painter.drawPoint(x_min+x, y_min+y)

                    circle_size: int = 10
                    painter.setPen(QColor(0, 0, 255))  # Draw a circle on the last point
                    painter.drawEllipse(self.trace_points[-1][0] - circle_size // 2, self.trace_points[-1][1] - circle_size // 2, circle_size, circle_size)
                    painter.drawEllipse(self.trace_points[-1][0] - circle_size // 2 + 1, self.trace_points[-1][1] - circle_size // 2 + 1, circle_size - 2, circle_size - 2)

                # * Update the image
                self.image_buffer.setPixmap(self.image_buffer.pix_data_map)


    def mouseMoveEvent(self, event):
        '''
        Handle the mouse move event.

        This is only **active when the mouse is moving & any button is pressed**.

        ## Args:
            - event (QMouseEvent): The mouse event that triggered the function.
        '''
        # self.image_buffer.print_px_data(event)  # print data while clicking and moving the mouse
        pass

        # x, y = event.pos().x(), event.pos().y()
        # Make a line that follows the mouse since the last click
        # if x < self.image_buffer.width() and y < self.image_buffer.height():
        #     last_x, last_y = self.trace_points[-1]

        #     # * It works more or less
        #     painter = QPainter(self.image_buffer.pix_data_map)
        #     painter.setPen(QColor(0, 0, 0))
        #     print(f"{last_x}, {last_y} -> {x}, {y}")
        #     painter.drawPoint(x, y)

        #     painter.end()  # ^ idk if this it's needed

        #     # self.trace_points.append((x, y))  # add the current mouse position to the trace points
        #     # self.update()  # update the widget content
        #     self.image_buffer.setPixmap(self.image_buffer.pix_data_map)



    # ^ --------------------------------------------------------------------------------------

    # ^ DEFINE SOME BUTTONS TO EDIT THE IMAGE (IMPORT, REPLACE, REMOVE)
    # ^ I think that this shlould be part of the workspace or something like that
    # ^ Because the image buffer should only be responsible for displaying the image
    # ^ And some buttons shouold be out of the image buffer boundaries
    # ^ Only the import button should be inside the image buffer
    def define_button(self, icon_type: str) -> QPushButton:
        '''
        Define a button with a specific icon.

        ## Arguments:
            - icon_type: the type of the icon (import, replace, remove)

        ## Returns:
            - the button instance
        '''
        button = QPushButton(self)
        button.setIcon(QIcon(Assets.ICONS.value+icon_type+'.png'))
        button.setIconSize(QSize(64, 64))
        button.setFixedSize(72, 72)
        button.setStyleSheet('QPushButton {background-color: white; border: 1px solid white; border-radius: 10%;} QPushButton:hover{background-color : lightgray;}')
        # Center the button in the image buffer
        button.move((int)((self.width()-button.width())/2), (int)((self.height()-button.height())/2))
        return button


    #  ^ Button functions
    # import_button: QPushButton
    # replace_button: QPushButton
    # delete_button: QPushButton

    # ^ This buttons must be on every image buffer
    # ? Define the buttons
    # self.import_button = self.define_button('import')
    # self.import_button.clicked.connect(self.import_image)

    # self.replace_button = self.define_button('replace')
    # self.replace_button.clicked.connect(self.import_image)
    # self.replace_button.hide()

    # * idk if we need this button (maybe we can just use the replace button)
    # self.delete_button = self.define_button('remove')
    # self.delete_button.clicked.connect(self.delete_image)
    # self.delete_button.hide()
