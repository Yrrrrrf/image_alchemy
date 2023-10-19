# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QScrollArea
from PyQt6.QtGui import QIcon, QPainter, QColor
from PyQt6.QtCore import QSize, Qt
import numpy as np
import cv2 as cv

# local imports
from logic.intel_sc import *
from components.vistualizer import Visualizer


@dataclass
# todo: probably this should be a QScrollArea
class Workspace(QScrollArea):
    '''
    This probably should hold an ImageVisualizer instead of an ImageBuffer
    '''
    visualizer: Visualizer


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'workspace')
        self.visualizer = Visualizer(self)
        self.visualizer.move(80, 80)  # Move the Visualizer

        self._set_visualizer_buttons()


        # self.setWidgetResizable(True)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        # self.setMouseTracking(True)  # enable mouse tracking without clicking


    def _set_visualizer_buttons(self):
        '''
        Set the buttons that interact each ImageBuffer

        The buttons are defined in the ImageBuffer class but the Workspace is the one that handles the buttons.

        This is because the buttons are outside the ImageBuffer boundaries.
        '''
        for img_buffer in self.visualizer.images:
            img_buffer.import_button.setParent(self)
            img_buffer.import_button.move(  # Import button
                self.visualizer.x() + img_buffer.x() + (img_buffer.width() - img_buffer.import_button.width()) // 2, 
                self.visualizer.y() + img_buffer.y() + (img_buffer.height() - img_buffer.import_button.height()) // 2
            )
            img_buffer.delete_button.setParent(self)
            img_buffer.delete_button.move(  # Delete button
                self.visualizer.x() + img_buffer.x() + img_buffer.width() - img_buffer.delete_button.width() - 4, 
                self.visualizer.y() + img_buffer.y() - img_buffer.delete_button.height() - 4
            )
            img_buffer.replace_button.setParent(self)
            img_buffer.replace_button.move(  # Replace button
                self.visualizer.x() + img_buffer.x() + img_buffer.width() - 2 * img_buffer.delete_button.width() - 8, 
                self.visualizer.y() + img_buffer.y() - img_buffer.delete_button.height() - 4
            )


    # def mousePressEvent(self, event):
    #     '''
    #     Print the pixel data of the image
    #     '''
    #     match event.buttons():
    #         # case _:
    #         case Qt.MouseButton.LeftButton:
    #             self.image_buffer.print_px_data(event)
    #         # case Qt.MouseButton.RightButton:
    #             x, y = event.pos().x(), event.pos().y()
    #             if x < self.image_buffer.width() and y < self.image_buffer.height():
    #                 self.trace_points.append((x, y))  # add the point to the list
    #                 # r, g, b, _ = self.image_buffer.pixmap().toImage().pixelColor(x, y).getRgb()
    #                 # print(f"\033[38;2;{r};{g};{b}m({x:4}, {y:4})\033[0m")

    #                 # * Create a painter to draw on the image
    #                 painter = QPainter(self.image_buffer.pix_data_map)
    #                 painter.setPen(QColor(0, 255, 0))

    #                 if len(self.trace_points) > 1:  # Do it only if there are at least 2 points
    #                     # * DRAW THE POINTS USING THE INTELIGENT SCISSORS ALGORITHM
    #                     # Get an image of the region of interest (rectangle of the last 2 points) + margin
    #                     margin = 60  # margin must be greater than 0 (otherwise it will crash)
    #                     x_0, y_0 = self.trace_points[-1]  # last point
    #                     x_1, y_1 = self.trace_points[-2]  # second to last point

    #                     x_min = max(0, min(x_0, x_1) - margin)
    #                     y_min = max(0, min(y_0, y_1) - margin)
    #                     x_max = min(self.image_buffer.width(), max(x_0, x_1) + margin)
    #                     y_max = min(self.image_buffer.height(), max(y_0, y_1) + margin)

    #                     roi = self.image_buffer.cost_matrix[y_min:y_max, x_min:x_max]

    #                     for y, x in dijkstra(roi, (y_0-y_min, x_0-x_min), (y_1-y_min, x_1-x_min)):
    #                     # for y, x in find_minimum_cost_path(roi, (y_0-y_min, x_0-x_min), (y_1-y_min, x_1-x_min)):
    #                         painter.setPen(QColor(0, 255, 0))
    #                         painter.drawPoint(x_min+x, y_min+y)

    #                 circle_size: int = 10
    #                 painter.setPen(QColor(0, 0, 255))  # Draw a circle on the last point
    #                 painter.drawEllipse(self.trace_points[-1][0] - circle_size // 2, self.trace_points[-1][1] - circle_size // 2, circle_size, circle_size)
    #                 painter.drawEllipse(self.trace_points[-1][0] - circle_size // 2 + 1, self.trace_points[-1][1] - circle_size // 2 + 1, circle_size - 2, circle_size - 2)

    #             # * Update the image
    #             self.image_buffer.setPixmap(self.image_buffer.pix_data_map)


    def mouseMoveEvent(self, event):
        '''
        Handle the mouse move event.

        This is only **active when the mouse is moving & any button is pressed**.

        ## Args:
            - event (QMouseEvent): The mouse event that triggered the function.
        '''
        pass
        # self.image_buffer.print_px_data(event)  # print data while clicking and moving the mouse

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
