import sys

import cv2 as cv
from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction, QFont

from config.globals import Config
from components.workspace import Workspace


APP_COLOR = '#00ff00'


# @dataclass
class MenuBar(QMenuBar):
    '''
    Menu Bar class contains the menus and the options of the application.
    Set the menu bar of the main window.
    '''
    def __init__(self):
        super().__init__()
        self.setProperty('class', 'menu_bar')
        # Set the menu bar style sheet
        self.setFont(QFont('Segoe Print', 10, QFont.Weight.Bold))
        # menu_bar_style ='QMenuBar{background-color: #2d2d2d; color: white;} QMenuBar::item::selected{background-color: '+f'{APP_COLOR}'+';}'
        # menu_style = 'QMenu{background-color: #2d2d2d; color: white; border: 1px solid '+f'{APP_COLOR}'+'; margin: 1px;} QMenu::item::selected{background-color: '+f'{APP_COLOR}'+';}'
        # self.setStyleSheet(menu_bar_style+menu_style)  # Set the style of the menu bar

        # ? Set all the QMenus and actions of the menu bar.
        self.set_file_menu()
        # self.set_edit_menu()
        # self.set_tools_menu()
        # self.set_view_menu()
        # self.set_help_menu()


    def set_file_menu(self):
        '''
        Set the file menu.
        '''
        self.file_menu = QMenu('File', self)  # Create the file menu

        # Add the menu to the menu bar
        self.select_image = QAction('Select Image', self)
        self.select_image.setShortcut('Ctrl+O')
        self.file_menu.addAction(self.select_image)

        # # Add Save Image action
        self.save_image = QAction('Save Image', self)
        self.save_image.setShortcut('Ctrl+S')
        self.file_menu.addAction(self.save_image)

        # # Add Save Image As action
        # save_image_as = QAction('Save Image As', self)
        # save_image_as.setShortcut('Ctrl+Shift+S')
        # file_menu.addAction(save_image_as)
        # # Add Separator
        # file_menu.addSeparator()

        # # Add Save Project action
        # random_image = QAction('Random Image', self)
        # random_image.setShortcut('Ctrl+R')
        # # random_image.triggered.connect(lambda: Workspace.visualizer[0].set+
        # file_menu.addAction(random_image)
        # # Add Separator
        # file_menu.addSeparator()

        # # Add Exit action
        # exit_app = QAction('Exit', self)
        # exit_app.setShortcut('Ctrl+W')  # xdn't
        # # exit_app.setShortcut('Ctrl+Q')  # xdn't
        # exit_app.triggered.connect(sys.exit)
        # file_menu.addAction(exit_app)

        # Add the menu to the menu bar
        self.addMenu(self.file_menu)


    def set_view_menu(self):
        '''
        Set the view menu.
        '''
        view_menu = QMenu('View', self)

        # Add the zoom in action
        zoom_in = QAction('Zoom In', self)
        zoom_in.setShortcut('Ctrl++')
        zoom_in.triggered.connect(lambda: print(f'[{Config.VERSION.value}]    Still working on it...!'))
        view_menu.addAction(zoom_in)

        # Add the zoom out action
        zoom_out = QAction('Zoom Out', self)
        zoom_out.setShortcut('Ctrl+-')
        zoom_out.triggered.connect(lambda: print(f'[{Config.VERSION.value}]    Still working on it...!'))
        view_menu.addAction(zoom_out)

        # # Add change theme action
        # change_theme = QAction('Change Theme', self)
        # change_theme.setShortcut('Ctrl+T')
        # change_theme.triggered.connect(lambda: print(f'[{Config.VERSION.value}]    Still working on it...!\n    The actual color is {Settings.APP_COLOR.value}'))
        # view_menu.addAction(change_theme)

        # Add the menu to the menu bar
        self.addMenu(view_menu)


    def set_help_menu(self):
        '''
        Set the help menu.
        '''
        help_menu = QMenu('Help', self)

        # Add the about action
        about = QAction('About', self)
        about.setShortcut('Ctrl+H')
        about.triggered.connect(lambda: print(f'[{Config.VERSION.value}]    Still working on it...!'))
        help_menu.addAction(about)

        # Add the menu to the menu bar
        self.addMenu(help_menu)
        # help_menu.triggered.connect(print(Settings.))


    # def set_tools_menu(self):
    #     '''
    #     Set the tools menu.
    #     '''
    #     pass


    # def set_edit_menu(self):
    #     '''
    #     Set the edit menu.
    #     '''
    #     pass



# * random cat image

# from requests import get
# filename = 'resources\\img\\temp\\cat.jpg'


# def load_cat() -> str:
#     '''
#     Load a cat image from the internet and store it to the resources folder.
#     :return: the filename of the cat image
#     '''
#     request = get('https://cataas.com/cat', stream=True)
#     with open (filename, 'wb') as file:
#         file.write(request.content)
#         img = cv.imread(filename)
#         return filename
