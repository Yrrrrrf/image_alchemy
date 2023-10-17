# standard imports
from dataclasses import dataclass

# third-party imports
from PyQt6.QtWidgets import QFrame, QPushButton, QWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

# local imports
from config.globals import Assets


@dataclass
class SidePanel(QFrame):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    margin: int = 8  # margin between the buttons
    is_expanded: bool = False  # Flag to track the toggle state


    def __init__(self):
        super().__init__()
        self.setProperty('class', 'side_panel')
        self.setFixedWidth(self.margin*4)  # set the initial size of the side bar (not expanded)
        # self.setFixedHeight(600)  # * only if the AlignmentFlag is not set
        # * If the AlignmentFlag is set, the size of the widget is ignored
        # * If it's not, the Height will be the minimum height of the widgets inside (0 if empty)

        # self.setFixedWidth(self.margin*4+SideBarButton.size)  # set the initial size of the side bar

        # This also need to be stored as a variable to manipulate it later
        s = SPButton(self, 'import', [{'name': 'Crop', 'fn': lambda: print('Crop')}])
        s.move(self.margin, self.margin)  # * move the button to the top of the side bar
        # Is not a var yet because is a test of the SPButton (SidePanelButton) button


    def mousePressEvent(self, event):
        '''
        When the mouse is pressed, the side bar will expand or collapse.
        '''
        if event.button() == Qt.MouseButton.LeftButton:
            match self.is_expanded:
                # Toggle the side bar
                case True: self.setFixedWidth(self.margin*4)
                case False: self.setFixedWidth(200)
            self.is_expanded = not self.is_expanded  


@dataclass
class SPButton(QPushButton):
    '''
    SideBarButton class contains a list of operations that can be executed to an image.
    Every operation is a button will appear in the Operations Menu.
    '''
    side_panel: QWidget  # ? Parent Widget
    name: str  # ? name corresponds to the Operation type (Enum)
    operations: list[dict]  # ? list of operations
    size: int = 48


    def __init__(self, side_panel: QWidget, name: str, operations: list[dict]):
        super().__init__()
        self.name = name
        self.operations = operations
        self.setParent(side_panel)
        self.setProperty('class', 'sidebar_button')

        # If there's only one file with that posible name*, then the path will be autocompleted to the file.
        # print(Assets.ICONS.value+self.name.lower()+'.png')

        self.setIcon(QIcon(Assets.ICONS.value+self.name.lower()+'.png'))
        self.setIconSize(QSize((int)(self.size*0.8), (int)(self.size*0.8)))
        self.setFixedSize(self.size, self.size)  # default size
        # set the operation to execute when the button is pressed
        self.clicked.connect(self.operations[0]['fn'])

