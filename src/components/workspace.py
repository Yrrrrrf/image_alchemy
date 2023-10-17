# This file contains the workspace component

# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QPushButton, QFrame, QScrollArea
# the QStackedLayout stacks the widgets on top of each other (like a deck of cards)
# from PyQt6.QtWidgets import QStackedLayout  
from PyQt6.QtGui import QIcon, QPainter, QColor
from PyQt6.QtCore import QSize, Qt
import numpy as np
import cv2 as cv

# local imports
from logic.intel_sc import *
from config.globals import Assets
from components.vistualizer import Visualizer


@dataclass
# todo: probably this should be a QScrollArea
class Workspace(QScrollArea):
    '''
    # This probably should hold an ImageVisualizer instead of an ImageBuffer
    # And the ImageVisualizer should hold one or more ImageBuffers (for the layers)
    # Also the ImageVisualizer should be responsible for managing all the ImageBuffers
    # And the Workspace should be responsible for managing all the ImageVisualizers
    '''
    visualizer: Visualizer


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'workspace')
        self.visualizer = Visualizer(self)



        # * See the scroll bars only when needed

        # self.setWidgetResizable(True)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)



        # * This is a temporary solution
        # * It's used to enable the MouseMoveEvent updates without clicking
        # self.setMouseTracking(True)  # enable mouse tracking without clicking

        # todo: this shouln't be a class attribute
        # ^ I mean, this should be a local variable
        # ^ Just for testing purposes (it will be removed later) 
        # self.trace_points = []  # create a list of the points
        # self.trace_points = [(0, 0)]  # create a list of the points

        # * Get a normalized version of the cost matrix (for debugging purposes)
        # * The original cost matrix is not normalized & it's not a good idea to display it
        # * Because it has values that are too low, so we can't really see anything

        # normalized_cost_matrix = cv.normalize(self.image_buffer.cost_matrix, None, 0, 255, cv.NORM_MINMAX)  # type: ignore
        # cv.imwrite(Assets.TEMP_IMAGES.value+'normalized_cost_matrix.png', normalized_cost_matrix)

        self.set_visualizer_buttons()
        # Set the 


    def set_visualizer_buttons(self):
        '''
        Set the buttons of the visualizer.
        '''
        for img_buffer in self.visualizer.images:
            import_button = self.define_button('import')
            import_button.move(img_buffer.x() + (int)((img_buffer.width()-import_button.width())/2), img_buffer.y() + (int)((img_buffer.height()-import_button.height())/2))

            delete_button = self.define_button('remove', b_size=32)
            delete_button.move(img_buffer.x() + img_buffer.width() - delete_button.width(), img_buffer.y() - delete_button.height() - 4)
            delete_button.hide()

            replace_button = self.define_button('replace', b_size=32)
            replace_button.move(img_buffer.x() + img_buffer.width() - 2 * delete_button.width() - 8, img_buffer.y() - delete_button.height() - 4)
            replace_button.hide()

            import_button.clicked.connect(lambda: {
                img_buffer.import_image(),
                import_button.hide(),
                delete_button.show(),
                replace_button.show(), 
                }
            )

            delete_button.clicked.connect(lambda: {
                print('delete'),
                import_button.show(),
                delete_button.hide(),
                replace_button.hide(),
                }
            )

            replace_button.clicked.connect(lambda: {
                print('replace'),
                }
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


    # ^ --------------------------------------------------------------------------------------

    # ^ DEFINE SOME BUTTONS TO EDIT THE IMAGE (IMPORT, REPLACE, REMOVE)
    # ^ I think that this shlould be part of the workspace or something like that
    # ^ Because the image buffer should only be responsible for displaying the image
    # ^ And some buttons shouold be out of the image buffer boundaries
    # ^ Only the import button should be inside the image buffer
    def define_button(self, icon_type: str, b_size: int = 72) -> QPushButton:
        '''
        Define a button with a specific icon.

        ## Arguments:
            - icon_type: the type of the icon (import, replace, remove)

        ## Returns:
            - the button instance
        '''
        button = QPushButton(self)
        button.setIcon(QIcon(Assets.ICONS.value+icon_type+'.png'))
        button.setIconSize(QSize((int)(b_size*0.8), (int)(b_size*0.8)))
        button.setFixedSize(b_size, b_size)
        button.setStyleSheet('QPushButton {background-color: white; border: 1px solid white; border-radius: 10%;} QPushButton:hover{background-color : lightgray;}')

        return button

