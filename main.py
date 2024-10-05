from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import sqlite3
from windows import LoginWindow

connection = sqlite3.connect('main_database.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    group_name TEXT NOT NULL,
    surname TEXT NOT NULL PRIMARY KEY,
    marks TEXT NOT NULL,
    social_activities BOOL,
    salary INTEGER
)
''')
connection.commit()


def show_alert(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


def show_critical(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


def show_information(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


def main():
    app = QApplication(sys.argv)
    lw = LoginWindow.LoginWindow()
    lw.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    cursor.close()
    connection.close()
