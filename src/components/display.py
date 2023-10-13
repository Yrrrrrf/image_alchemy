# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QGridLayout, QFrame
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
    # * Maybe the Display can have more than one side panel along the window
    side_panel: SidePanel

    # * Maybe the Display could have more than one workspace (like tabs)
    # todo: explore the QStackedLayout & Tabs possibilities
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
        # add a third SidePanel below the second one

        
        # ^ The following code is just for testing --------------------------------------------
        # * This won't work because the size of the widgets is ignored
        # * So the height inside the Display will be 0 (invisible)
        # * to fix it must add a minimum height to the widgets
        # self.side_panel2 = SidePanel()
        # layout.addWidget(self.side_panel2, 0, 2)
        # self.side_panel3 = SidePanel()
        # self.side_panel3.setFixedHeight(200)
        # layout.addWidget(self.side_panel3, 1, 0, alignment=Qt.AlignmentFlag.AlignBottom)

        self.setLayout(layout)
