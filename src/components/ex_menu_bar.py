from img_operations.load_image import open_file
from globals import SNAPSHOT, APP_COLOR
from components.workspace import Workspace
from PyQt6.QtWidgets import QMenuBar, QMenu, QFileDialog
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtCore import QCoreApplication
import cv2 as cv
from dataclasses import dataclass

@dataclass
class MenuBar(QMenuBar):
    '''
    Menu Bar class contains the menus and the options of the application.
    Set the menu bar of the main window.
    '''
    def __init__(self):
        super().__init__()
        self.setProperty('class', 'menu_bar')
        self.set_menu_bar()


    def set_menu_bar(self):
        for [menu_name, action_list] in menu_bar_dict.items():
            menu = QMenu(menu_name, self)
            menu.setProperty('class', 'menu_bar_submenu')
            for action_dict in action_list:
                if action_dict['name'] == 'Separator':
                    menu.addSeparator()
                    continue
                action = QAction(action_dict['name'], self)
                if 'shortcut' in action_dict:
                    action.setShortcut(action_dict['shortcut'])
                if 'description' in action_dict:
                    action.setStatusTip(action_dict['description'])
                if 'function' in action_dict:
                    action.triggered.connect(action_dict['function'])
                menu.addAction(action)
            self.addMenu(menu)
                    

menu_bar_dict = {
    'File': [
        {
            'name': 'Select Image',
            'shortcut': 'Ctrl+O',
            'function': lambda x: open_file(x),
        },
        {
            'name': 'Save Image',
            'shortcut': 'Ctrl+S',
            'description': 'Save the image in the current state'
        },
        {
            'name': 'Save Image As',
            'shortcut': 'Ctrl+Shift+S'
        },
        {
            'name': 'Separator'
        },
        {
            'name': 'Random Image',
            'shortcut': 'Ctrl+R',
            # 'function': lambda: load_cat
        },
        {
            'name': 'Separator'
        },
        {
            'name': 'Exit',
            'shortcut': 'Ctrl+W',
            'function': lambda: QCoreApplication.instance().quit()
        }
    ],

    'View': [
        {
            'name': 'Zoom In',
            'shortcut': 'Ctrl++',
            'function': lambda: print(f'[{SNAPSHOT}]    Still working on it...!')
        },
        {
            'name': 'Zoom Out',
            'shortcut': 'Ctrl+-',
            'function': lambda: print(f'[{SNAPSHOT}]    Still working on it...!')
        },
        {
            'name': 'Separator'
        },
        {
            'name': 'Change Theme',
            'shortcut': 'Ctrl+T',
            'function': lambda: print(f'[{SNAPSHOT}]    Still working on it...!')
        }
    ],

    'Help': [
        {
            'name': 'About',
            'shortcut': 'Ctrl+H',
            'function': lambda: print(f'[{SNAPSHOT}]    Still working on it...!')
        }
    ]
}

