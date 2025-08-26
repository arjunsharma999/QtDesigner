from PyQt5 import QtWidgets, QtCore
import sys

# Import the two Designer-generated UI classes with aliases to avoid name clash
from home import Ui_MainWindow as Ui_Home
from Mainwindow import Ui_MainWindow as Ui_MainPage


class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        # Make the "HOME" area clickable to navigate
        # Prefer clicking directly on the text area if present; otherwise on its container
        if hasattr(self.ui, "textBrowser_2") and self.ui.textBrowser_2 is not None:
            self.ui.textBrowser_2.mousePressEvent = self._on_home_clicked
        elif hasattr(self.ui, "widget_3") and self.ui.widget_3 is not None:
            self.ui.widget_3.mousePressEvent = self._on_home_clicked

        self._main_page = None

    def _on_home_clicked(self, event):
        if self._main_page is None:
            self._main_page = MainPageWindow()
        self._fade_to_window(self._main_page)

    def _fade_to_window(self, next_window: QtWidgets.QMainWindow):
        next_window.setWindowOpacity(0.0)
        next_window.show()
        animation = QtCore.QPropertyAnimation(next_window, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        # Keep a reference to prevent GC
        next_window._fade_animation = animation
        def on_finished():
            self.close()
            next_window._fade_animation = None
        animation.finished.connect(on_finished)
        animation.start()


class MainPageWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)
        # Make the back arrow clickable to return to Home
        if hasattr(self.ui, "label_5") and self.ui.label_5 is not None:
            self.ui.label_5.mousePressEvent = self._on_back_clicked

        self._home_page = None

    def _on_back_clicked(self, event):
        if self._home_page is None:
            self._home_page = HomeWindow()
        self._fade_to_window(self._home_page)

    def _fade_to_window(self, next_window: QtWidgets.QMainWindow):
        next_window.setWindowOpacity(0.0)
        next_window.show()
        animation = QtCore.QPropertyAnimation(next_window, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        # Keep a reference to prevent GC
        next_window._fade_animation = animation
        def on_finished():
            self.close()
            next_window._fade_animation = None
        animation.finished.connect(on_finished)
        animation.start()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()