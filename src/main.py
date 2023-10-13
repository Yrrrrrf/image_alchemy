"""
Image Alchemy

Image Alchemy is a GUI application that allows you to manipulate images in a wide variety of ways.

Author: Yrrrrrf
"""


# standard
from sys import exit, argv

# external
from PyQt6.QtWidgets import QApplication  # pip install PyQt6

# internal
from config.globals import Config  # import config
from components.app import App  # import app


def main() -> None:
    """
    Application entry point. 

    It is also responsible for setting up the logging system and configuring it.
    """
    # Execute the loading screen
    # todo: fix the loading screen (it closes the entire app instead of just the loading screen)
    # from components.loading_screen import run as run_loading_screen
    # run_loading_screen()

    app = QApplication(argv)  # Manage the GUI application's control flow and main settings.
    window = App()  # Create the instance of the MainWindow
    window.show()  # Show the window
    exit(app.exec())  # Execute the app


if __name__ == "__main__":
    """
    This is the entry point of the application.
    Clean the terminal and print app data before running the main function.
    Then run the main function.
    """
    print("\033[2J\033[1;1H", end="")  # clear terminal
    print(f"\033[92m{Config.NAME.value}\033[0m", end=" ")  # print n puzzle solver in green
    print(f"\033[97m{Config.VERSION.value}\033[0m")  # print version in white
    print(f"Author(s): \033[94m{Config.AUTHOR.value}\033[0m", end="\n\n")  # print author in blue

    main()  # run main function
