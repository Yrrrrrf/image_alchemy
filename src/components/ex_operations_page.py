from dataclasses import dataclass

from components.operation_button import OperationButton
from PyQt6.QtWidgets import QFrame, QLabel, QStackedWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from globals import APP_COLOR


@dataclass
class OperationsPage(QFrame):
    '''
    Every page belongs to a OperationsMenu.
    Is a page that contains the operations that can be applied to the image.
    These operations are displayed as buttons.
    '''
    operations_menu: QStackedWidget  # ? Parent Widget
    operations: list[dict]
    deployed: bool = False  # ? Whether the operations menu is deployed or not
    showing_size = 240  # ? The width of the operations menu when it is deployed


    def __init__(self, operations_menu: QStackedWidget, title: str, operations: list[dict]):
        '''
        Initialize the operations page inside the operations menu.
        The page contains a OperationButton for each operation.
        '''
        super().__init__(operations_menu)
        self.operations_menu = operations_menu
        self.operations = operations
        self.title = QLabel(self)
        self.title.setProperty('class', 'operations_page_title')
        self.set_title(title)
        self.set_operations()
        self.setProperty('class', 'operations_page')


    def set_title(self, title: str) -> None:
        '''
        Set the title of the operations menu.
        Every time the title is changed, the title label is recentered.
        '''
        from components.side_bar import SideBar, SideBarButton
        self.title.setText(title)
        self.title.setFont(QFont('Segoe Print', 16, QFont.Weight.Bold))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setGeometry(SideBar.margin*4, SideBar.margin*2, self.showing_size-SideBar.margin*8, SideBarButton.size-SideBar.margin)


    def set_operations(self) -> None:
        '''
        Set the operations of the operations menu.
        '''
        from components.operation_button import OperationButton
        from components.side_bar import SideBar, SideBarButton
        ops_size = (int)(SideBarButton.size/2)

        for i in range(len(self.operations)):
            OperationButton(self, self.operations[i]) \
            .setGeometry(SideBar.margin*2, self.title.height()+SideBar.margin*4+(i*(SideBar.margin+ops_size)), self.showing_size-SideBar.margin*4, ops_size)

        self.setFixedHeight(self.title.height()+((1+len(self.operations))*(SideBar.margin+ops_size)))

    
