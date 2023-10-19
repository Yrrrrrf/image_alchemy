# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QGridLayout, QFrame, QTabWidget, QPushButton, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt  # * for AlignmentFlag

# local imports
from components.workspace import Workspace
from components.side_panel import SidePanel
from config.globals import Assets


@dataclass
class Display(QFrame):
    '''
    Display class referece to the window that contains all the widgets.
    Also manage the position of the widgets and the size of the window.
    This class must the the main class of the application.
    '''
    side_panel: SidePanel  # * Maybe the Display can have more than one side panel along the window
    workspace_tabs: QTabWidget  # * Handles 1 or many workspaces


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'display')

        self.side_panel = SidePanel()
        # self.workspace_tabs = Workspace()  # * 1 workspace
        self.workspace_tabs = self._set_workspace_tabs()  # * multiple workspaces
        
        layout = QGridLayout()  # ? Set the layout distribution
        layout.addWidget(self.side_panel, 0, 0)  # * Expand and fill the space
        layout.addWidget(self.workspace_tabs, 0, 1)
        # layout.addWidget(SidePanel(), 0, 2)  # Add a third column  (for testing purposes)
        # layout.addWidget(SidePanel(), 0, 3)  # Add a fourth column (for testing purposes)
        # layout.addWidget(SidePanel(), 0, 4)  # Add a fifth column  (for testing purposes)
        self.setLayout(layout)


    def _set_workspace_tabs(self) -> QTabWidget:
        '''
        This method handles the creation & behavior of the workspace tabs.
        
        It creates a QTabWidget object with tabs. Any tab contains a `Workspace` object.

        # Returns:
            - `QTabWidget`: A QTabWidget object
        '''
        workspace_tabs = QTabWidget(self)  # Add a tab widget to the Display
        workspace_tabs.setProperty('class', 'workspace_tabs')
        workspace_tabs.setMovable(True)
        # * Print the name of the selected tab
        # workspace_tabs.currentChanged.connect(lambda index: print(f"Selected tab: {workspace_tabs.tabText(index)}"))

        # * New Tab button
        add_button = QPushButton(QIcon(Assets.ICONS.value+'sum.png'), '')
        add_button.clicked.connect(lambda: {
            workspace_tabs.addTab(Workspace(), f'New_{workspace_tabs.count()+1}'),
            # print(f'Added tab {workspace_tabs.count()}'),
            }
        )
        workspace_tabs.setCornerWidget(add_button, Qt.Corner.TopRightCorner)

        # * Close Tab button
        workspace_tabs.setTabsClosable(True)
        workspace_tabs.tabCloseRequested.connect(lambda index: self._close_tab(index))

        # * Add tabs to the workspace
        initial_tabs: int = 3
        [workspace_tabs.addTab(Workspace(), f'New_{i+1}') for i in range(initial_tabs)]

        return workspace_tabs


    def _close_tab(self, index: int):
        # TODO: Add a confirmation dialog (are you sure you want to close this tab?)
        if self.workspace_tabs.count() == 1:
            self.workspace_tabs.addTab(Workspace(), f'New')
        self.workspace_tabs.removeTab(index)
        # print(f'Closed tab {index}')


    def keyPressEvent(self, event):
        event_mod = event.modifiers()  # *  is a var because it is used multiple times
        match event_mod:
            case Qt.KeyboardModifier.ControlModifier:
                # print('Ctrl')
                # print(event.key())
                number = event.key() - 88 if event.key() == 94 else event.key() - 48
                match number:
                    case 30:  # N  # * Create a new tab
                        self.workspace_tabs.addTab(Workspace(), f'New_{self.workspace_tabs.count()+1}')
                    case 39:  # W  # * Close the current tab
                        self._close_tab(self.workspace_tabs.currentIndex())
                    case _:  # * Go to the tab of the number
                        if number <= self.workspace_tabs.count():  # If the number is less than the number of tabs
                            self.workspace_tabs.setCurrentIndex(number - 1)  # Go to the tab of the number

            # case Qt.KeyboardModifier.ShiftModifier:
            #     print('Shift')

            # case Qt.KeyboardModifier.AltModifier:
            #     print('Alt')

            # case Qt.KeyboardModifier.MetaModifier:
            #     print('Meta')

            # case Qt.KeyboardModifier.NoModifier:
            #     print('No modifier')

            # case _:
            #     print(f'Other modifier {event.key()}')

