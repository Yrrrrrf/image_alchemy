# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame

# local imports
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

        layout = QGridLayout()
        # ? This lines below will eventually be moved to its own class (SidePanel)
        self.side_panel = SidePanel()  # create the side panel

        # ? Set the workspace
        self.workspace = Workspace()
        # set a white background

        # ? Set the layout distribution
        layout.addWidget(self.side_panel, 0, 0)  # 0, 0 = row, column
        layout.addWidget(self.workspace, 0, 1)  # 0, 1 = row, column
        self.setLayout(layout)


