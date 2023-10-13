# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
# from PyQt6.QtWidgets import QStackedLayout  
# the QStackedLayout stacks the widgets on top of each other (like a deck of cards)
from PyQt6.QtCore import Qt  # * for AlignmentFlag

# own imports
from components.workspace import Workspace
from components.side_panel import SidePanel


@dataclass
class Display(QFrame):
    '''
    Display class referece to the window that contains all the widgets.
    Also manage the position of the widgets and the size of the window.
    This class must the the main class of the application.
    '''
    side_panel: QWidget    
    workspace: Workspace


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'display')

        self.side_panel = SidePanel()
        self.workspace = Workspace()

        layout = QGridLayout()  # ? Set the layout distribution
        # layout.addWidget(self.side_panel, 0, 0, alignment=Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(self.workspace, 0, 1, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.side_panel, 0, 0)  # * Expand and fill the space
        layout.addWidget(self.workspace, 0, 1)

        self.setLayout(layout)
