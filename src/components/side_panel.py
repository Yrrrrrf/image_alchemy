# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import Qt


@dataclass
class SidePanel(QFrame):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    margin: int = 8  # margin between the buttons


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'side_panel')

        # self.setFixedHeight(600)  # * only if the AlignmentFlag is not set
        # * If the AlignmentFlag is set, the size of the widget is ignored
        # * If it's not, the Height will be the minimum height of the widgets inside (0 if empty)

        self.setFixedWidth(self.margin*4)  # set the initial size of the side bar
        # self.setFixedWidth(self.margin*4+SideBarButton.size)  # set the initial size of the side bar

        self.clicked = False  # Flag to track the toggle state

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            match self.clicked:
                case True: self.setFixedWidth(200)
                case False: self.setFixedWidth(50)
            self.clicked = not self.clicked  
