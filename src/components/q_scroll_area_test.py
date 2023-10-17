# To create a PyQt6 application with a QScrollArea that can move both horizontally (x-axis) and vertically (y-axis), you can follow the example below. This example will create a simple window with a scrollable area that contains a large widget. You can use the scroll bars to move in both the x and y directions.

# First, make sure you have PyQt6 installed. You can install it using pip:

# ```bash
# pip install PyQt6
# ```

# Here's the code for the example:

# ```python
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout

class ScrollableContent(QWidget):
    def __init__(self):
        super().__init__()

        # Create a large widget to go inside the scroll area
        self.large_widget = QWidget()
        self.large_widget.setGeometry(0, 0, 800, 800)
        self.large_widget.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(220, 220, 220))
        self.large_widget.setPalette(palette)

        # Create a scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.large_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        self.setLayout(layout)

class ScrollableWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scrollable QScrollArea Example")
        self.setGeometry(100, 100, 400, 400)

        scrollable_content = ScrollableContent()
        self.setCentralWidget(scrollable_content)

def main():
    app = QApplication(sys.argv)
    window = ScrollableWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
# ```

# In this example, we create a `QScrollArea` inside a `QMainWindow`. The `ScrollableContent` class contains a large widget that is placed inside the `QScrollArea`. We set the `QScrollArea` to always display both horizontal and vertical scroll bars, and we set the widget inside it to be resizable. You can then run the code, and it will create a window with a scrollable area that you can move both horizontally and vertically.