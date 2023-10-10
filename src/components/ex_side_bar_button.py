from PyQt6.QtWidgets import QPushButton, QWidget
from globals import APP_COLOR, ICON_PATH
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from dataclasses import dataclass


@dataclass
class SideBarButton(QPushButton):
    '''
    SideBarButton class contains a list of operations that can be executed to an image.
    Every operation is a button will appear in the Operations Menu.
    '''
    side_bar: QWidget  # ? Parent Widget
    name: str  # ? name corresponds to the Operation type (Enum)
    operations: list[dict]  # ? list of operations
    size: int = 48


    def __init__(self, name: str, operations: list[dict], side_bar: QWidget):
        super().__init__()
        from components.side_bar import SideBar  # this import is there to avoid circular imports
        self.name = name
        self.operations = operations
        self.setParent(side_bar)
        # If there's only one file with that posible name*, then the path will be autocompleted to the file.
        self.setIcon(QIcon(f"{ICON_PATH}\\{self.name}.png"))  # Just to be sure that is the format of the icon
        self.setIconSize(QSize((int)(self.size*0.8), (int)(self.size*0.8)))
        self.setFixedSize(self.size, self.size)  # default size
        self.setProperty('class', 'sidebar_button')

