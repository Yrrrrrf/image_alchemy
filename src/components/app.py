# standard imports
from dataclasses import dataclass

# Third-party imports
from sass import compile  # compile the sass stylesheet
from PyQt6.QtWidgets import QMainWindow, QMenu
from PyQt6.QtGui import QIcon, QAction

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

        # * Assign the actions to the menu bar
        self.assign_actions()  # Set all the actions to their respective elements to apply the logic


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


    def assign_actions(self):
        """
        Assign the actions to the menu bar
        """
        # [print(menu.title()) for menu in self.menu_bar.findChildren(QMenu)]  # print the title of the menus
        # * Get the actions of the menu bar
        qactions = list(filter(lambda x: x.text() != "", self.menu_bar.findChildren(QAction)))
        # [print(action.text()) for action in qactions]  # print the text of the actions

        # * Add the behavior to the actions
        # LOAD IMAGE
        qactions[1].triggered.connect(lambda: self.display.workspace.v_list[self.display.workspace.currentIndex()].selected_image.import_image())
        # REMOVE IMAGE
        qactions[2].triggered.connect(lambda: self.display.workspace.v_list[self.display.workspace.currentIndex()].selected_image.remove_image())
        # SAVE IMAGE
        qactions[3].triggered.connect(lambda: self.display.workspace.v_list[0].save_image())
