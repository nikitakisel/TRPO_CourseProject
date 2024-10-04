from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QTableWidgetItem, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox, QComboBox, \
    QScrollArea, QVBoxLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)
        self.label = QLabel(content)

        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)

    def setText(self, text):
        # setting text to the label
        self.label.setText(text)


class InfoWindow(QMainWindow):
    def __init__(self, parent=None):
        # You must call the super class method
        super().__init__(parent)

        self.mw = None
        self.setFixedSize(QSize(620, 380))  # Set sizes
        self.setWindowTitle("Информация о программе 'Электронная кафедра, 1 курс'")  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        self.img_label = QLabel(self)
        icon_image = QPixmap('img/about_us_img.png')
        self.img_label.setPixmap(icon_image)
        self.img_label.resize(280, 380)

        self.program_name_label = QLabel("Программное средство 'Электронная\nкафедра, 1 курс'", self)
        self.program_name_label.move(315, 15)
        self.program_name_label.resize(295, 50)
        self.program_name_label.setStyleSheet('QLabel {font-weight: bold; }')

        self.program_version_label = QLabel("Верисия программы: v2.3", self)
        self.program_version_label.move(315, 55)
        self.program_version_label.resize(295, 50)

        self.developer_name_label = QLabel("Разработал: Киселев Никита\nКонстантинович", self)
        self.developer_name_label.move(315, 95)
        self.developer_name_label.resize(295, 50)

        self.date_of_release_label = QLabel("Дата выпуска: 04 октября 2024г.", self)
        self.date_of_release_label.move(315, 135)
        self.date_of_release_label.resize(295, 50)

        self.program_target_label = ScrollLabel(self)
        self.program_target_label.setText(
            "Программное средство 'Электронная\n"
            "кафедра, 1 курс' разработано для учёта\n"
            "результатов сданной студентами\n"
            "первого курса сессии.\n\n"
            "В разработанном ПО доступны функции:\n\n"
            "  - добавления и удаления записей;\n"
            "  - внесения изменений в записи;\n"
            "  - сортировка таблицы студентов;\n"
            "  - подсчёта количества активистов;\n"
            "  - расчёта стипендии по стандартной;\n"
            "  - формирование отчёта по группе;\n"
            "  - удаления двоечников;\n"
            "  - формирования рейтинга студентов.",
        )
        self.program_target_label.move(315, 175)
        self.program_target_label.resize(285, 150)

        self.close_button = QPushButton('ОК', self)
        self.close_button.move(310, 335)
        self.close_button.resize(80, 30)

        self.close_button.clicked.connect(self.close_info_window)

    def close_info_window(self):
        self.close()
