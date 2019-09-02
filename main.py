from ui_ping import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    my_ui = Ui_MainWindow()
    my_ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
