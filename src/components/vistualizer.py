# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QFrame, QLabel, QGridLayout
from PyQt6.QtCore import Qt, QRect, QSize, QPoint, QEvent
from PyQt6.QtGui import QCursor, QPixmap, QImage, QPainter
import cv2 as cv

# local imports
from components.image_buffer import ImageBuffer
from config.globals import Assets
from templates import templates
# from templates import Templates

# todo: Make the Visualizer scalable in size (also have to make the ImageBuffer scalable in size)
# todo: think about the logic above
@dataclass
class Visualizer(QLabel):
    '''
    This class contains one or more image buffer's, which are the images that are displayed in the workspace.
    The visualizer is the container of the image buffer's. 
    '''
    images: list[ImageBuffer]
    border: int = 0


    def __init__(self, workspace: QFrame, template: str = '1x1', border: int = 0):
    # def __init__(self, workspace: QFrame):
        super().__init__(workspace)
        self.setProperty('class', 'visualizer')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.setMinimumSize(QSize(512, 512))

        # * Color the background
        self.bg_pixmap = QPixmap(self.width(), self.height())
        # self.bg_pixmap.fill(Qt.GlobalColor.white)

        template = '1x1'
        # template = '2c'
        # template = '3r'
        self.border = 16
        # todo: fix the border behavior for some templates

        self.set_template(template)  # also set a default ImageBuffer
        self.draw_images()


    def draw_images(self):
        '''
        Draw the images on the visualizer.
        '''
        painter = QPainter(self.bg_pixmap)
        for image in self.images:
            painter.drawPixmap(image.x(), image.y(), image.pixmap())
            self.setPixmap(self.bg_pixmap)


    # def set_template(self, template: Templates) -> None:
    def set_template(self, template: str) -> None:
        '''
        Set the template of the visualizer.
        The template is the layout of the image buffer's.
        '''
        self.images = []
        for coors in templates[template](self.width(), self.height(), self.border):
            # print(coors)
            self.images.append(ImageBuffer(self, coors[2], coors[3]))
            self.images[-1].move(coors[0], coors[1])
            # * Set the new size of the visualizer
            self.setFixedSize(self.width(), self.height())


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
        match self.pixmap().save("test.png"):
            case True:  # if the image is valid, show the image info
                print(f"\033[32mSuccessfully\x1B[37m stored at: \033[34m{store_path}\x1B[37m")
            case False:  # if the image is not valid, show an error message
                print(f"\033[31mError storing img\x1B[37m")
                # print(self.pixmap())


    # * UPDATE
    def update_image(self) -> None:
        '''
        Set the image buffer to a specific image.
        
        ## Arguments:
            - img_path: `str`: the path of the image
        '''
        pass
        # height, width, _ = cv.imread(self.img_path).shape  # get the image info
        # self.setFixedSize(width, height)  # update the size of the image buffer

        # # Print the image info
        # print(f"Selected: \033[32m{self.img_path}\x1B[37m")
        # print(f"     Shape: ({height}, {width}) = {height*width} pixels")

        # self.pix_data_map = QPixmap(self.img_path)  # Create a QPixmap object (contains image data)
        # self.img = cv.imread(self.img_path)  # Create a np.ndarray object (contains image data)
        # self.cost_matrix = get_cost_matrix(self.img)  # Create a np.ndarray object (contains cost matrix data)
        # # self.draw_shapes(self.pix_data_map)  # ^ draw shapes on the image

        # self.setPixmap(self.pix_data_map)  # set the image buffer to the selected image


    def mousePressEvent(self, event):
        '''
        Print the pixel data of the image
        '''
        match event.buttons():
            case _:
                self.print_px_data(event)


    # ^ SOME EXTRA FEATURES ---------------------------------------------

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
