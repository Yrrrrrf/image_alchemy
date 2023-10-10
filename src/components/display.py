# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QWidget, QHBoxLayout

# local imports
from components.workspace import Workspace


@dataclass
class Display(QWidget):
    '''
    Display class referece to the window that contains all the widgets.
    Also manage the position of the widgets and the size of the window.
    This class must the the main class of the application.
    '''
    side_panel: QWidget    
    workspace: Workspace

    def __init__(self):
        super().__init__()

        # ? This lines below will eventually be moved to its own class (SidePanel)
        self.side_panel = QWidget()
        self.side_panel.setFixedWidth(64)  # Set the width of the side panel
        self.side_panel.setStyleSheet("background-color: #0f0f0f;")  # Set the background color of the side panel

        # ? Set the workspace
        self.workspace = Workspace()
        # self.workspace.setStyleSheet("background-color: #0f0f0f;")  # Set the background color of the workspace

        # ? Set the layout distribution
        layout = QHBoxLayout()
        layout.addWidget(self.side_panel)
        layout.addWidget(self.workspace, stretch=1)
        self.setLayout(layout)
