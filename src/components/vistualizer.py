# from src.img_operations.load_image import load_cat
# from src.templates import templates

from src.components.image_buffer import ImageBuffer
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtGui import QImage, QPen, QPainter, QCursor, QShortcut
from dataclasses import dataclass
import cv2 as cv


@dataclass
class Visualizer(QLabel):
    '''
    This class contains one or more image buffer's, which are the images that are displayed in the workspace.
    The visualizer is the container of the image buffer's. 
    '''
    workspace: QFrame  # ! is this needed?
    images: list[ImageBuffer]  # list of image buffers
    margin: int = 16
    scale: float = 1.0
    template: str = 'square'
    selected: bool = False


    def __init__(self, workspace: QFrame, width: int = 512, height: int = 512, scale: float = 1.0, margin: int = 16, template: str = 'square'):
        super().__init__(workspace)
        self.setStyleSheet('background-color: white')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.scale = scale
        self.margin = margin
        self.template = template
        self.setMinimumSize(QSize((int)(width*scale), (int)(height*scale)))

        self.images = []
        # template = list(templates.keys())[self.template]  # get the n template (name: str)
        # for coors in templates[template](self.width(), self.height(), self.margin):
        #     self.images.append(ImageBuffer(coors[2], coors[3], self))
        #     self.images[-1].move(coors[0], coors[1])

        # self.set_delete_menu()

    # def mousePressEvent(self, event):
    #     '''
    #     When the mouse is pressed, the image buffer will be selected.
    #     '''
    #     # SET ARROW KEY SHORTCUTS

    #     self.shortcut = QShortcut(Qt.Key.Key_Left, self)
    #     self.shortcut.activated.connect(lambda: print('x'))
    #     self.shortcut = QShortcut(Qt.Key.Key_Right, self)
    #     self.shortcut.activated.connect(lambda: print('x'))
    #     self.shortcut = QShortcut(Qt.Key.Key_Up, self)
    #     self.shortcut.activated.connect(lambda: print('x'))
    #     self.shortcut = QShortcut(Qt.Key.Key_Down, self)
    #     self.shortcut.activated.connect(lambda: print('x'))

        # # def move functions
        # def move_left():
        #     self.move(self.pos() - 1, self.selected.y())
        # def move_right():
        #     self.move(self.pos() + 1, self.selected.y())
        # def move_up():
        #     self.move(self.pos(), self.selected.y() - 1)
        # def move_down():
        #     self.move(self.pos(), self.selected.y() + 1)


    # SELECT IMAGE BUFFER
    def select_image_buffer(self, image_buffer: ImageBuffer):
        '''
        Select an image buffer.
        '''
        self.selected = True
        # image_buffer.selected = True
        image_buffer.setStyleSheet('background-color: #e0e0e0')


    def deselect_image_buffer(self, image_buffer: ImageBuffer):
        '''
        Deselect an image buffer.
        '''
        self.selected = False
        # image_buffer.selected = False
        image_buffer.setStyleSheet('background-color: white')


    def set_template(self):
        '''
        Set the template of the visualizer.
        The template is the layout of the image buffer's.
        '''
        # self.images = []
        # # template = list(templates.keys())[]  # get the n template (name: str)
        # for coors in templates[template](self.width(), self.height(), self.margin):
        #     self.images.append(ImageBuffer(coors[2], coors[3], self))
        #     self.images[-1].move(coors[0], coors[1])


    # def set_delete_menu(self):
    #     '''
    #     Set the delete menu of a image buffer.
    #     Each image buffer has a delete menu, which is a button that can be used to delete the image of the image buffer.
    #     '''
    #     # from src.components.image_buffer import active_buffer
    #     # global active_buffer
    #     for image in self.images:
    #         self.delete_button = QPushButton(self)
    #         self.delete_button.setText('X')
    #         self.delete_button.move(image.x() + image.width() - self.delete_button.width(), image.y())
    #         self.delete_button.clicked.connect(active_buffer.delete_image)
    #     # self.delete_button.move(self.images[0].x() + self.images[0].width() - self.delete_button.width(), self.images[0].y())
    #     # self.delete_button.hide()


    def save_image(self, path: str = 'resources\\test.png'):
        '''
        Generate an equivalent constant image of the visualizer, but with the images of the image buffer's.
        This image can be saved to a file.
        The image will be reconstructed from the image buffer's.
        '''
        # create a new image using OpenCV and map the image buffer's to the new image
        image = cv.imread('resources\\test.png')
        # for image_buffer in self.images:
            # if image_buffer.image is not None:
            # image[image_buffer.y():image_buffer.y()+image_buffer.height(), image_buffer.x():image_buffer.x()+image_buffer.width()] = image_buffer.image
        # save the image to a file
        # image.save(path)
        # return the image
