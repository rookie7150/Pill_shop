from PyQt5 import QtWidgets
from controller import MainWindow_Controller

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_Controller()
    window.show()
    sys.exit(app.exec_())