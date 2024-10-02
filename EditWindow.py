from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QTableWidgetItem, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox, QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap


class EditWindow(QMainWindow):
    def __init__(self, record):
        # You must call the super class method
        super().__init__()

        self.setFixedSize(QSize(240, 290))  # Set sizes
        self.setWindowTitle('Редактирование')  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        self.group_name_textbox = QLineEdit(self)
        self.group_name_textbox.setPlaceholderText('Группа')
        self.group_name_textbox.move(50, 50)
        self.group_name_textbox.resize(120, 30)
        self.group_name_textbox.setText(record[0])

        self.surname_textbox = QLineEdit(self)
        self.surname_textbox.setPlaceholderText('Фамилия')
        self.surname_textbox.move(50, 90)
        self.surname_textbox.resize(120, 30)
        self.surname_textbox.setText(record[1])

        self.marks_textbox = QLineEdit(self)
        self.marks_textbox.setPlaceholderText('Оценки')
        self.marks_textbox.move(50, 130)
        self.marks_textbox.resize(120, 30)
        self.marks_textbox.setText(record[2])

        self.social_activities = QCheckBox(self)
        self.social_activities.move(50, 170)
        self.social_activities.setCheckState(bool(record[3]))
        self.label_name = QLabel('Общ. деят.', self)
        self.label_name.move(70, 170)

        self.done_button = QPushButton('Сохранить', self)
        self.done_button.move(45, 210)
        self.done_button.resize(130, 30)
