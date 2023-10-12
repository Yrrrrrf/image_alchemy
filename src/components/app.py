"""
This file defines the main App class.


"""

#? Imports ------------------------------------------------------------------------------------

# Built-in imports
from dataclasses import dataclass  # dataclass decorator

# Third-party imports
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

# Own imports
from config.globals import *
from components.display import Display
from components.menu_bar import MenuBar
from sass import compile


#? Logic --------------------------------------------------------------------------------------

@dataclass
class App(QMainWindow):
    """
    App class
    This class contains the logic for the GUI
    """
    # display: Display

    def __init__(self):
        """
        Initialize the app
        """
        super().__init__()
        self.setProperty('class', 'app_window')  # set the class name for the stylesheet

        self.setWindowTitle(Config.NAME.value)
        self.setWindowIcon(QIcon(f"{Assets.ICONS.value}scissors.png"))
        self.setMinimumSize(Config.WIDTH.value, Config.HEIGHT.value)
        self.setMouseTracking(True)  # track mouse even when not clicking
        # self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)  # focus on the window

        # # set a stylesheet for the app
        self._set_theme('default')
        # self._set_theme('dev')

        self.menu_bar = MenuBar()
        self.setMenuBar(self.menu_bar)

        self.display = Display()
        self.setCentralWidget(self.display)

        # connect the mnenu bar to the workspace
        # self.menu_bar.select_image.triggered.connect(self.display.workspace.image_buffer.import_image)
        # self.menu_bar.save_image.triggered.connect(self.display.workspace.image_buffer.save_image)


    def _set_theme(self, theme: str = 'default') -> None:
        """
        Load the stylesheet from the sass file
        """
        with open(f"{Assets.THEMES.value}{theme}.scss", 'r') as file:
            self.setStyleSheet(compile(string=file.read()))


    def keyPressEvent(self, event):
        """
        Handle key press events
        """
        if event.key() == Qt.Key.Key_Escape:
            self.close()

