# standard imports
from dataclasses import dataclass

# Third-party imports
from sass import compile  # compile the sass stylesheet
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QMenu
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt

# Own imports
from config.globals import *
from components.display import Display
from components.menu_bar import MenuBar


@dataclass
class App(QMainWindow):
    """
    App class
    This class contains the logic for the GUI
    """
    menu_bar: MenuBar
    display: Display


    def __init__(self):
        """
        Initialize the app
        """
        super().__init__()
        self.setProperty('class', 'app_window')  # set the class name for the stylesheet
        self.setWindowTitle(Config.NAME.value)
        self.setWindowIcon(QIcon(f"{Assets.ICONS.value}philosophers-stone.png"))
        self.setMinimumSize(Config.WIDTH.value, Config.HEIGHT.value)

        self.setMouseTracking(True)  # track mouse even when not clicking
        # self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)  # focus on the window
        # * Set a stylesheet for the app
        self._set_theme('default')
        # self._set_theme('dev')

        self.menu_bar = MenuBar()
        self.setMenuBar(self.menu_bar)

        self.display = Display()
        self.setCentralWidget(self.display)

        # set a variable for the elements of the menu bar
        # qmenus = self.menu_bar.findChildren(QMenu)
        # for menu in qmenus:
        #     print(menu.title())

        qactions = self.menu_bar.findChildren(QAction)
        # for action in qactions:
        #     print(action.text())
        # print(qactions)

        qactions[3].triggered.connect(lambda: self.display.workspace.v_list[0].save_image())
        print(qactions[3].text())


    def _set_theme(self, theme: str = 'default'):
        """
        Load the stylesheet from the sass file

        # Arguments
            theme (str): the name of the theme to load

        # Theme names
            - `default`: the default theme
            - `dark`: the dark theme (not implemented yet)
            - `dev`: the development theme (not implemented yet)
        """
        with open(f"{Assets.THEMES.value}{theme}.scss", 'r') as file:
            self.setStyleSheet(compile(string=file.read()))
