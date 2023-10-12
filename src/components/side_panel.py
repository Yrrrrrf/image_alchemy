from dataclasses import dataclass
from typing import Callable

from PyQt6.QtWidgets import QWidget, QFrame

# from components.side_bar_button import SideBarButton
# from components.operations_menu import OperationsMenu
# from components.operations_page import OperationsPage
# from components.operation_button import OperationButton
# from operations import operation_types_dict


@dataclass
class SidePanel(QFrame):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    # buttons_frame: QFrame
    # buttons: list[SideBarButton]
    # operations_menu: OperationsMenu  # contains the operation buttons
    margin: int = 8  # margin between the buttons


    # def __init__(self, display: QWidget):
    def __init__(self):
        # super().__init__(display)
        super().__init__()
        self.setProperty('class', 'side_panel')


        self.setFixedWidth(self.margin*4)  # set the initial size of the side bar
        # self.setFixedWidth(self.margin*4+SideBarButton.size)  # set the initial size of the side bar

        # ? set the buttons_frame on the left side of the side bar
        # self.buttons_frame = QFrame(self)
        # self.buttons_frame.setFixedWidth(self.margin*2+SideBarButton.size)
        # ? load the buttons
        # self.load_side_bar_buttons()
        # self.setProperty('class', 'sidebar')

        # self.center_side_bar()
        # example
        # OperationButton(self.operations_menu, {'a': lambda: print('a')}).setGeometry(32, 88, 2000, 32)


    def load_side_bar_buttons(self) -> None:
        '''
        Load the buttons of the side bar.
        Every buttons is associated to a Operations Menu, that contains many operations.
        '''
        pass
        # self.operations_menu = OperationsMenu(self)  # Is a stack widget that contains the operations
        # self.operations_menu.setProperty('class', 'operations_menu')
        # self.buttons = []

        # for idx, [op_type, op_list] in enumerate(operation_types_dict.items()):
        #     op_button = SideBarButton(op_type, op_list, self.buttons_frame)
        #     op_button.setGeometry(self.margin, self.margin+(SideBarButton.size+self.margin)*idx, SideBarButton.size, SideBarButton.size)
        #     self.buttons.append(op_button)
        #     self.operations_menu.addWidget(OperationsPage(self.operations_menu, op_button.name, op_list))

        # def sidebar_toggle(index: int) -> Callable:
        #     return lambda: self.toggle(index)

        # for idx in range(len(self.buttons)):
        #     self.buttons[idx].clicked.connect(sidebar_toggle(idx))

        # # ? set the operations_menu on the right side of the buttons_frame
        # self.operations_menu.setGeometry(self.margin*2+SideBarButton.size, 0, self.margin*2, self.margin+self.buttons[-1].y()+SideBarButton.size)


    def toggle(self, page_index: int) -> None:
        '''
        Toggle the Operations Menu. (show/hide)
        Update the title & buttons of the operations menu.
        '''
        # if self.operations_menu.deployed == True:  # if the operations menu is deployed
        #     if self.operations_menu.currentIndex() == page_index:
        #         self.operations_menu.hide()  # hide the operations menu
        #         self.setFixedWidth(self.margin*4+SideBarButton.size)
        #     else:  # if the operations menu is deployed, but the user clicked on a different button
        #         self.operations_menu.setCurrentIndex(page_index)
        #         self.operations_menu.setFixedHeight(len(self.buttons[page_index].operations)*(SideBarButton.size+self.margin))
        # else:  # if the operations menu is hidden
        #     self.operations_menu.setCurrentIndex(page_index)
        #     self.operations_menu.deploy()  # show the operations menu
        #     self.operations_menu.setFixedHeight(len(self.buttons[page_index].operations)*(SideBarButton.size+self.margin))
        #     # update the width of the side bar (to fit the operations menu)
        #     self.setFixedWidth(self.margin*2+SideBarButton.size+self.operations_menu.width())


    def center_side_bar(self) -> None:
        '''
        Center the side bar. (vertical)
        '''        
        # self.setFixedHeight(self.margin+self.buttons[-1].y()+SideBarButton.size)

