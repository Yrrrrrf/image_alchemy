# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QGridLayout, QFrame, QTabWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QStackedLayout  
# the QStackedLayout stacks the widgets on top of each other (like a deck of cards)
from PyQt6.QtCore import Qt  # * for AlignmentFlag

# own imports
from components.workspace import Workspace
from components.side_panel import SidePanel
from components.vistualizer import Visualizer
from config.globals import Assets


@dataclass
class Display(QFrame):
    '''
    Display class referece to the window that contains all the widgets.
    Also manage the position of the widgets and the size of the window.
    This class must the the main class of the application.
    '''
    side_panel: SidePanel  # * Maybe the Display can have more than one side panel along the window
    workspace_tabs: QTabWidget  # The workspace handles many Tabs


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'display')

        self.side_panel = SidePanel()
        self.workspace_tabs = self.set_workspace_tabs()

        layout = QGridLayout()  # ? Set the layout distribution

        # layout.addWidget(self.side_panel, 0, 0, alignment=Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(self.workspace, 0, 1, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.side_panel, 0, 0)  # * Expand and fill the space
        layout.addWidget(self.workspace_tabs, 0, 1)

        self.setLayout(layout)


    def set_workspace_tabs(self) -> QTabWidget:
        workspace_tabs = QTabWidget(self)
        workspace_tabs.setProperty('class', 'workspace_tabs')
        workspace_tabs.setMovable(True)

        # * Print the name of the selected tab
        workspace_tabs.currentChanged.connect(lambda index: print(f"Selected tab: {workspace_tabs.tabText(index)}"))

        # * New Tab button
        add_button = QPushButton(QIcon(Assets.ICONS.value+'sum.png'), '')
        add_button.clicked.connect(lambda: workspace_tabs.addTab(Visualizer(self), f'Workspace {workspace_tabs.count()+1}'))
        workspace_tabs.setCornerWidget(add_button, Qt.Corner.TopRightCorner)
        # self.workspace_tabs.setCornerWidget(add_button, Qt.Corner.TopLeftCorner)

        # * Close Tab button
        workspace_tabs.setTabsClosable(True)
        workspace_tabs.tabCloseRequested.connect(lambda index: {
            # Add a new tab if there is only one tab left
            workspace_tabs.addTab(Visualizer(self), f'New') if workspace_tabs.count() == 1 else None,
            workspace_tabs.removeTab(index),  # * Remove the tab
            }
        )

        # Add a new tab
        workspace_tabs.addTab(Visualizer(self), 'Workspace 1')
        # self.workspace_tabs.addTab(Visualizer(self), 'Workspace 2')
        return workspace_tabs