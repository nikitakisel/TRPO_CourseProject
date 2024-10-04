from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QTableWidgetItem, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox, QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
import hashlib
import main
import MainWindow
import InfoWindow


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        # You must call the super class method
        super().__init__(parent)

        self.iw = None
        self.mw = None
        self.setFixedSize(QSize(340, 320))  # Set sizes
        self.setWindowTitle('Вход')  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        self.img_label = QLabel(self)
        icon_image = QPixmap('img/Logo_Kubstu.png')
        self.img_label.setPixmap(icon_image)
        self.img_label.resize(90, 90)
        self.img_label.move(125, 15)

        self.login_textbox = QLineEdit(self)
        self.login_textbox.setPlaceholderText('Логин')
        self.login_textbox.move(60, 120)
        self.login_textbox.resize(220, 30)

        self.password_textbox = QLineEdit(self)
        self.password_textbox.setPlaceholderText('Пароль')
        self.password_textbox.setEchoMode(QLineEdit.Password)
        self.password_textbox.move(60, 160)
        self.password_textbox.resize(220, 30)

        self.enter_button = QPushButton('Вход', self)
        self.enter_button.move(55, 220)
        self.enter_button.resize(230, 30)

        self.enter_button.clicked.connect(self.try_to_enter)

        self.enter_button = QPushButton('О программе', self)
        self.enter_button.move(55, 250)
        self.enter_button.resize(230, 30)

        self.enter_button.clicked.connect(self.open_info_window)

    def try_to_enter(self):
        login = str(int(hashlib.md5(self.login_textbox.text().encode()).hexdigest(), 16))
        password = str(int(hashlib.md5(self.password_textbox.text().encode()).hexdigest(), 16))

        main.cursor.execute('''
        SELECT * FROM Teachers
        WHERE login = ?
        ''', (login,))
        record = main.cursor.fetchall()
        main.connection.commit()

        if self.login_textbox.text() == '':
            main.show_alert("Заполните\nполе 'Логин'!")
        elif self.password_textbox.text() == '':
            main.show_alert("Заполните\nполе 'Пароль'!")
        elif len(record) == 0:
            main.show_critical("Пользователь\nне найден!")
        elif password != record[0][3]:
            main.show_critical("Неверный\nпароль!")
        else:
            self.mw = MainWindow.MainWindow(record[0][0], record[0][1])
            self.mw.show()
            self.iw.close()
            self.close()

    def open_info_window(self):
        self.iw = InfoWindow.InfoWindow()
        self.iw.show()

