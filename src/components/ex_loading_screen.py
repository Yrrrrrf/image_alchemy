import time
from dataclasses import dataclass

from PyQt6.QtGui import QPen, QPainter, QImage, QCursor, QBrush, QColor, QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QFrame, QProgressBar, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer


@dataclass
class LoadingScreen(QWidget):
    '''
    A progress bar with a custom style
    '''
    progress_bar: QProgressBar
    title_bar: QLabel
    loading_screen: QFrame
    timer: QTimer
    progress: int = 0


    def __init__(self):
        super().__init__()
        # set the window size
        self.setWindowTitle('Loading Scren')
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(420, 240)
        # set QWidgets...
        self.loading_screen = QFrame(self)
        self.set_image('resources\\static\\cells.png', 82, 0)
        self.set_title_bar()
        self.set_progress_bar()        
        # set the timer
        self.timer = QTimer()
        self.progress = 0
        self.timer.timeout.connect(loading)
        self.timer.start(100)


    def set_image(self, path: str, x: int, y: int) -> None:
        '''
        Set one image in the loading screen at the given position
        '''
        icon = QImage(path)
        icon = icon.scaled(256, 256, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        icon_label = QLabel(self.loading_screen)
        icon_label.move(x, y)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setPixmap(QPixmap.fromImage(icon))


    def set_title_bar(self) -> None:
        '''
        Set the title bar of the loading screen
        '''
        self.title_bar = QLabel(self.loading_screen)
        self.title_bar.setGeometry(0, 0, 420, 240)
        self.title_bar.setText('Canvas')
        self.title_bar.setFont(QFont('Segoe Print', 64, QFont.Weight.Bold))
        self.title_bar.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.title_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)


    def set_progress_bar(self):
        # ? Set progress bar
        self.progress_bar = QProgressBar(self.loading_screen)
        self.progress_bar.setGeometry(60, 180, 300, 32)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setFont(QFont('Segoe Print', 10, QFont.Weight.Bold))


    def close(self):
        self.timer.stop()
        self.close()


def loading():
    if LoadingScreen.progress < 100:
        LoadingScreen.progress += 1
        LoadingScreen.progress_bar.setValue(LoadingScreen.progress)
        print('a')
    else:
        LoadingScreen.timer.stop()
        # LoadingScreen.close()



# now test it
if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = LoadingScreen()
    window.show()
    sys.exit(app.exec())
