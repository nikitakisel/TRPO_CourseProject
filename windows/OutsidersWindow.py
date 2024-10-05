from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QTableWidgetItem, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox, QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main


class OutsidersWindow(QMainWindow):
    def __init__(self):
        # You must call the super class method
        super().__init__()

        self.setFixedSize(QSize(370, 340))  # Set sizes
        self.setWindowTitle('Двоечники')  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        self.table = QTableWidget(self)  # Create a table
        self.table.setColumnCount(4)  # Set three columns
        self.table.setRowCount(0)  # and one row

        # Set the table headers
        self.table.setHorizontalHeaderLabels(['Назв группы', 'Фамилия студента', 'Оценки', 'Общ работа'])

        # Set the tooltips to headings
        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")

        # Set the alignment to the headers
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)

        # Do the resize of the columns by content
        self.table.resizeColumnsToContents()
        grid_layout.addWidget(self.table, 0, 0)  # Adding the table to the grid

        main.cursor.execute('''
        SELECT group_name, surname, marks, social_activities FROM Students
        WHERE length(marks) - length(replace(marks, '2', '')) > 0
        ''')
        records = main.cursor.fetchall()
        main.connection.commit()
        self.table.setRowCount(len(records))
        self.show_table(records)

    def show_table(self, data):
        if len(data) > 0:
            for i in range(len(data)):
                self.table.setItem(i, 0, QTableWidgetItem(data[i][0]))
                self.table.setItem(i, 1, QTableWidgetItem(data[i][1]))
                self.table.setItem(i, 2, QTableWidgetItem(data[i][2]))
                self.table.setItem(i, 3, QTableWidgetItem('Да' if data[i][3] else 'Нет'))
