# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QScrollArea, QTabWidget, QPushButton, QWidget
from PyQt6.QtGui import QIcon, QPainter, QColor, QPen
from PyQt6.QtCore import QSize, Qt
import numpy as np
import cv2 as cv
from config.globals import Assets

# local imports
from logic.intel_sc import *
from components.vistualizer import Visualizer


@dataclass
# todo: probably this should be a QScrollArea
class Workspace(QTabWidget):
    '''
    The workspace is the container of the visualizer.

    It handles the mouse events and the buttons of the visualizer.

    Also it handles the buttons of the image buffer's. (RUD operations)
    '''


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'workspace')
        self.setMovable(True)
        # self.setMouseTracking(True)
        # * New Tab button
        add_button = QPushButton(QIcon(Assets.ICONS.value+'sum.png'), '')
        add_button.clicked.connect(self._new_tab)
        self.setCornerWidget(add_button, Qt.Corner.TopRightCorner)
        # * Close Tab button
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self._close_tab)

        # * Set initial tabs
        [self._new_tab() for _ in range(3)]


    def _new_tab(self):
        '''
        Create a new tab with a visualizer.
        Also set the buttons of the image buffer's inside the visualizer.
        '''
        scroll_zone = QWidget()
        visualizer = Visualizer(scroll_zone)

        scroll_zone.setFixedSize(visualizer.width() + 2 *self.width(), visualizer.height() + 2 * self.height())
        visualizer.move(scroll_zone.width() // 2 - visualizer.width() // 2, scroll_zone.height() // 2 - visualizer.height() // 2)

        # # * Add the visualizer to the scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidget(scroll_zone)   # Set the scroll zone as the widget of the scroll area
        scroll_area.setWidgetResizable(True)  # Make the scroll area resizable
        # Activate the scroll bars
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # Set the scroll area to the center of the tab
        scroll_area.horizontalScrollBar().setValue(scroll_zone.width() // 2 - visualizer.width() // 2 - 32)  # type: ignore
        scroll_area.verticalScrollBar().setValue(scroll_zone.height() // 2 - visualizer.height() // 2 - 32)  # type: ignore


        # todo: Fix pos of the buttons
        # * Set the buttons of the image buffer's
        for img_buffer in visualizer.images:
            # img_buffer.import_button.setParent(scroll_area)
            img_buffer.import_button.setParent(scroll_zone)
            img_buffer.import_button.move(  # Import button (Create)
                visualizer.x() + img_buffer.x() + (img_buffer.width() - img_buffer.import_button.width()) // 2, 
                visualizer.y() + img_buffer.y() + img_buffer.height() // 2
            )
            img_buffer.delete_button.setParent(scroll_zone)
            img_buffer.delete_button.move(  # Delete button (Remove)
                visualizer.x() + img_buffer.x() + img_buffer.width() - img_buffer.delete_button.width() - 4, 
                visualizer.y() + img_buffer.y() - img_buffer.delete_button.height() - 4
            )
            img_buffer.replace_button.setParent(scroll_zone)
            img_buffer.replace_button.move(  # Replace button (Update)
                visualizer.x() + img_buffer.x() + img_buffer.width() - 2 * img_buffer.delete_button.width() - 8, 
                visualizer.y() + img_buffer.y() - img_buffer.delete_button.height() - 4
            )

        # self.addTab(scroll_zone, f'New_{self.count()+1}')
        self.addTab(scroll_area, f'New_{self.count()+1}')


    def _close_tab(self, index: int):
        # TODO: Add a confirmation dialog (are you sure you want to close this tab?)
        if self.count() == 1: self.addTab(Visualizer(self), f'New_{self.count()}')
        self.removeTab(index)


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

        # todo: fix the scroll area movement
        # ^ this is just a prof of concept (it works but it's not perfect)
        # if event.buttons() == Qt.MouseButton.MiddleButton:
        #     for scroll_area in self.findChildren(QScrollArea):
        #         scroll_value = event.pos().y() - self.height() // 2
        #         v_bar = scroll_area.verticalScrollBar()
        #         v_bar.setValue(v_bar.value() - scroll_value)

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
