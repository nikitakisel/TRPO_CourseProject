from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QTableWidgetItem, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox, QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap


class InfoWindow(QMainWindow):
    def __init__(self, parent=None):
        # You must call the super class method
        super().__init__(parent)

        self.mw = None
        self.setFixedSize(QSize(340, 280))  # Set sizes
        self.setWindowTitle('Информация о программе')  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        self.img_label = QLabel(self)
        icon_image = QPixmap('img/Logo_Kubstu.png')
        self.img_label.setPixmap(icon_image)
        self.img_label.resize(90, 90)
        self.img_label.move(125, 15)

        self.program_name_label = QLabel('Общ. деят.', self)
        self.program_name_label.move(10, 10)
        self.program_name_label.setStyleSheet('QLabel {color: white; }')

        self.close_button = QPushButton('Выйти', self)
        self.close_button.move(55, 220)
        self.close_button.resize(230, 30)

        self.close_button.clicked.connect(self.close_info_window)

    def close_info_window(self):
        self.close()
