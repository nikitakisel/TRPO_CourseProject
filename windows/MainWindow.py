from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QTableWidgetItem, QLineEdit, QPushButton, QLabel, QCheckBox, QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from windows import EditWindow, GroupFeedBackWindow
from windows import RatingWindow
from windows import OutsidersWindow
import re
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main


class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self, user_name, user_surname):
        # You must call the super class method
        super().__init__()

        self.rw = None
        self.ew = None
        self.ow = None
        self.gfw = None
        self.setFixedSize(QSize(1010, 360))  # Set sizes
        self.setWindowTitle(f'Электронная кафедра, 1 курс ({user_name} {user_surname})')  # Set the window title

        self.img_label = QLabel(self)
        main_image = QPixmap('img/layout.png')
        self.img_label.setPixmap(main_image)
        self.img_label.resize(1010, 360)

        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget
        central_widget.setMaximumSize(500, 1000)

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        self.table = QTableWidget(self)  # Create a table
        self.table.setColumnCount(5)  # Set three columns
        self.table.setRowCount(0)  # and one row

        # Set the table headers
        self.table.setHorizontalHeaderLabels(['Назв группы', 'Фамилия студента', 'Оценки', 'Общ работа', 'Размер стипендии'])

        # Set the tooltips to headings
        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")
        self.table.horizontalHeaderItem(4).setToolTip("Column 5 ")

        # Set the alignment to the headers
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(4).setTextAlignment(Qt.AlignHCenter)

        # self.table.setColumnWidth(0, 150)
        # self.table.setColumnWidth(1, 150)
        # self.table.setColumnWidth(2, 150)
        # self.table.setColumnWidth(3, 150)
        # self.table.setColumnWidth(4, 150)

        # Do the resize of the columns by content
        self.table.resizeColumnsToContents()
        grid_layout.addWidget(self.table, 0, 0)  # Adding the table to the grid

        # Инициализация
        self.upload_data()

        # Атрибуты "Добавление записи"

        self.group_name_textbox = QLineEdit(self)
        self.group_name_textbox.setPlaceholderText('Группа')
        self.group_name_textbox.move(510, 40)
        self.group_name_textbox.resize(120, 30)

        self.surname_textbox = QLineEdit(self)
        self.surname_textbox.setPlaceholderText('Фамилия')
        self.surname_textbox.move(510, 80)
        self.surname_textbox.resize(120, 30)

        self.marks_textbox = QLineEdit(self)
        self.marks_textbox.setPlaceholderText('Оценки')
        self.marks_textbox.move(510, 120)
        self.marks_textbox.resize(120, 30)

        self.social_activities = QCheckBox(self)
        self.social_activities.move(510, 160)
        self.label_name = QLabel('Общ. деят.', self)
        self.label_name.move(530, 160)
        self.label_name.setStyleSheet('QLabel {color: white; }')

        self.add_button = QPushButton('Добавить запись', self)
        self.add_button.move(505, 195)
        self.add_button.resize(130, 30)

        self.add_button.clicked.connect(self.add_note)

        # Атрибуты "Удаление по фамилии"

        self.delete_by_surname_textbox = QLineEdit(self)
        self.delete_by_surname_textbox.setPlaceholderText('Фамилия')
        self.delete_by_surname_textbox.move(660, 40)
        self.delete_by_surname_textbox.resize(120, 30)

        self.delete_button = QPushButton('Удалить запись', self)
        self.delete_button.move(655, 80)
        self.delete_button.resize(130, 30)

        self.delete_button.clicked.connect(self.delete_note)

        # Атрибуты "Расчёт стипендии"

        self.size_of_salary_textbox = QLineEdit(self)
        self.size_of_salary_textbox.setPlaceholderText('Размер стипендии')
        self.size_of_salary_textbox.move(660, 140)
        self.size_of_salary_textbox.resize(120, 30)

        self.solve_salary_button = QPushButton('Расчет стипендии', self)
        self.solve_salary_button.move(655, 180)
        self.solve_salary_button.resize(145, 30)

        self.solve_salary_button.clicked.connect(self.solve_salary)

        # Атрибуты "Сортировка данных"

        self.sort_data_combobox = QComboBox(self)
        self.sort_data_combobox.addItems(['Назв группы', 'Фамилия', 'Общ работа', 'Размер стипендии'])
        self.sort_data_combobox.move(505, 245)
        self.sort_data_combobox.resize(130, 30)

        self.sort_data_button = QPushButton('Сортировать', self)
        self.sort_data_button.move(505, 280)
        self.sort_data_button.resize(130, 30)

        self.sort_data_button.clicked.connect(self.sort_data)

        # Атрибуты "Отчёт по группе"

        self.group_feedback_textbox = QLineEdit(self)
        self.group_feedback_textbox.setPlaceholderText('Группа')
        self.group_feedback_textbox.move(660, 240)
        self.group_feedback_textbox.resize(120, 30)

        self.group_feedback_button = QPushButton('Сделать отчёт', self)
        self.group_feedback_button.move(655, 280)
        self.group_feedback_button.resize(130, 30)

        self.group_feedback_button.clicked.connect(self.show_group_feedback_window)

        # Атрибуты "Редактирование"

        self.edit_textbox = QLineEdit(self)
        self.edit_textbox.setPlaceholderText('Фамилия')
        self.edit_textbox.move(815, 40)
        self.edit_textbox.resize(120, 30)

        self.edit_button = QPushButton('Редактировать', self)
        self.edit_button.move(810, 80)
        self.edit_button.resize(130, 30)

        self.edit_button.clicked.connect(self.edit_note)
        
        # Атрибуты "РЕЙТИНГ"

        self.rating_button = QPushButton('Общий рейтинг', self)
        self.rating_button.move(810, 140)
        self.rating_button.resize(175, 30)

        self.rating_button.clicked.connect(self.show_rating)

        # Атрибуты "Ахалай-махалай"

        self.inverse_best_button = QPushButton('Ахалай-махалай', self)
        self.inverse_best_button.move(810, 175)
        self.inverse_best_button.resize(175, 30)
        self.inverse_best_button.clicked.connect(self.inverse_best)

        # Атрибуты "Подсчитать число активистов"

        self.count_activities_button = QPushButton('Подсчитать активистов', self)
        self.count_activities_button.move(810, 210)
        self.count_activities_button.resize(175, 30)
        self.count_activities_button.clicked.connect(self.count_activities)

        # Атрибуты "Удаление двоечников"

        self.delete_outsiders_button = QPushButton('Удалить двоечников', self)
        self.delete_outsiders_button.move(810, 245)
        self.delete_outsiders_button.resize(175, 30)
        self.delete_outsiders_button.clicked.connect(self.delete_outsiders)

        # Атрибуты "Удаление данных"

        self.delete_data_button = QPushButton('Удалить все данные', self)
        self.delete_data_button.move(810, 280)
        self.delete_data_button.resize(175, 30)
        self.delete_data_button.clicked.connect(self.delete_data)

    def add_note(self):
        main.cursor.execute('''
        SELECT surname FROM Students
        ''')
        records = main.cursor.fetchall()
        main.connection.commit()

        group_name_pattern = re.compile(r'[0-9]{2}([-][к])(?:[а-я]|)+[-]([а-я]{2})[1-6]')

        if self.group_name_textbox.text() == '' or self.surname_textbox.text() == '' or self.marks_textbox.text() == '':
            main.show_alert("Вы заполнили\nне все поля!")

        elif (self.surname_textbox.text(),) in records:
            main.show_critical(f"Запись с фамилией\n'{self.surname_textbox.text()}' уже существует!")

        elif not group_name_pattern.match(self.group_name_textbox.text()):
            main.show_alert("Некорректно заполнено\nполе 'Группа'!")

        elif len(self.marks_textbox.text()) != 5 or sum([self.marks_textbox.text().count('2'),
                self.marks_textbox.text().count('3'), self.marks_textbox.text().count('4'),
                self.marks_textbox.text().count('5'), self.marks_textbox.text().count('_')]) != 5:
            main.show_alert("Некорректно заполнено\nполе 'Оценки'!")

        else:
            main.cursor.execute('''
            INSERT INTO Students (group_name, surname, marks, social_activities) VALUES (?, ?, ?, ?);
            ''', (self.group_name_textbox.text(), self.surname_textbox.text(), self.marks_textbox.text(),
                  self.social_activities.isChecked()))
            main.connection.commit()

            main.cursor.execute('''
            SELECT Count(*) FROM Students
            ''')
            records_count = main.cursor.fetchall()[0][0]
            main.connection.commit()
            self.table.setRowCount(records_count)

            self.table.setItem(records_count - 1, 0, QTableWidgetItem(self.group_name_textbox.text()))
            self.table.setItem(records_count - 1, 1, QTableWidgetItem(self.surname_textbox.text()))
            self.table.setItem(records_count - 1, 2, QTableWidgetItem(self.marks_textbox.text()))
            self.table.setItem(records_count - 1, 3, QTableWidgetItem('Да' if self.social_activities.isChecked() else 'Нет'))
            self.table.setItem(records_count - 1, 4, QTableWidgetItem('-'))

            self.group_name_textbox.clear()
            self.surname_textbox.clear()
            self.marks_textbox.clear()
            self.social_activities.setCheckState(False)

    def delete_note(self):
        main.cursor.execute('''
        SELECT surname FROM Students
        ''')
        records = main.cursor.fetchall()
        main.connection.commit()

        if self.delete_by_surname_textbox.text() == '':
            main.show_alert('Введите\nфамилию!')
        elif not((self.delete_by_surname_textbox.text(),) in records):
            main.show_critical(f"Студента с фамилией\n'{self.delete_by_surname_textbox.text()}' не существует!")
        else:
            main.cursor.execute('''
            DELETE FROM Students WHERE surname = ?
            ''', (self.delete_by_surname_textbox.text(),))
            main.connection.commit()
            self.upload_data()
            self.delete_by_surname_textbox.clear()

    def edit_note(self):
        main.cursor.execute('''
        SELECT * FROM Students WHERE surname = ?
        ''', (self.edit_textbox.text(),))
        records = main.cursor.fetchall()
        main.connection.commit()

        if self.edit_textbox.text() == '':
            main.show_alert('Введите фамилию\nстудента!')
        elif len(records) == 0:
            main.show_critical(f"Студента с фамилией\n'{self.edit_textbox.text()}' не найдено")
        else:
            self.ew = EditWindow.EditWindow(records[0])
            self.ew.show()
            self.ew.done_button.clicked.connect(self.update_note)

    def update_note(self):
        main.cursor.execute('''
        SELECT surname FROM Students
        ''')
        records = main.cursor.fetchall()
        main.connection.commit()
        records.remove((self.edit_textbox.text(),))

        group_name_pattern = re.compile(r'[0-9]{2}([-][к])(?:[а-я]|)+[-]([а-я]{2})[1-6]')

        if self.ew.group_name_textbox.text() == '' or self.ew.surname_textbox.text() == '' or self.ew.marks_textbox.text() == '':
            main.show_alert("Вы заполнили\nне все поля!")

        elif (self.ew.surname_textbox.text(),) in records:
            main.show_critical(f"Запись с фамилией\n'{self.ew.surname_textbox.text()}' уже существует!")

        elif not group_name_pattern.match(self.ew.group_name_textbox.text()):
            main.show_alert("Некорректно заполнено\nполе 'Группа'!")

        elif len(self.ew.marks_textbox.text()) != 5 or sum([self.ew.marks_textbox.text().count('2'),
                self.ew.marks_textbox.text().count('3'), self.ew.marks_textbox.text().count('4'),
                self.ew.marks_textbox.text().count('5'), self.ew.marks_textbox.text().count('_')]) != 5:
            main.show_alert("Некорректно заполнено\nполе 'Оценки'!")

        else:
            main.cursor.execute('''
            UPDATE Students 
            SET group_name = ?, surname = ?, marks = ?, social_activities = ?, salary = ?
            WHERE surname = ?
            ''', (self.ew.group_name_textbox.text(), self.ew.surname_textbox.text(),
                  self.ew.marks_textbox.text(), self.ew.social_activities.isChecked(),
                  None, self.edit_textbox.text()))
            main.connection.commit()

            self.ew.close()
            self.upload_data()
            self.edit_textbox.clear()

    def solve_salary(self):
        if self.size_of_salary_textbox.text() == '':
            main.show_alert("Заполните поле\n'Размер стипендии'!")
        elif not self.size_of_salary_textbox.text().isdigit():
            main.show_critical("Вы ввели\nне число!")
        else:
            main.cursor.execute('''
            SELECT surname, marks, social_activities FROM Students
            ''')
            records = main.cursor.fetchall()
            main.connection.commit()
            standard_salary = int(self.size_of_salary_textbox.text())

            for i in range(len(records)):
                if not('_' in records[i][1]):
                    record = records[i]
                    marks = record[1]
                    salary = 0

                    if marks.count('5') == 5:
                        salary = int(standard_salary * 1.5)
                    elif marks.count('2') == 0 and marks.count('3') == 0 or marks.count('2') == 0 and \
                            marks.count('3') == 1 and record[2]:
                        salary = standard_salary

                    main.cursor.execute('''
                    UPDATE Students SET salary = ? WHERE surname = ?
                    ''', (salary, record[0]))
                    main.connection.commit()
            self.size_of_salary_textbox.clear()
            self.upload_data()

    def show_table(self, data):
        if len(data) > 0:
            for i in range(len(data)):
                self.table.setItem(i, 0, QTableWidgetItem(data[i][0]))
                self.table.setItem(i, 1, QTableWidgetItem(data[i][1]))
                self.table.setItem(i, 2, QTableWidgetItem(data[i][2]))
                self.table.setItem(i, 3, QTableWidgetItem('Да' if data[i][3] else 'Нет'))
                self.table.setItem(i, 4, QTableWidgetItem(
                    '-' if not(data[i][4]) and data[i][4] != 0 else str(data[i][4]) + ' р.'))

    def show_group_feedback_window(self):
        main.cursor.execute('''
        SELECT group_name FROM Students
        ''')
        records = main.cursor.fetchall()
        main.connection.commit()

        if self.group_feedback_textbox.text() == '':
            main.show_alert('Введите\nгруппу!')
        elif not((self.group_feedback_textbox.text(),) in records):
            main.show_critical(f"Группы '{self.group_feedback_textbox.text()}'\nне существует!")
        else:
            group_name = self.group_feedback_textbox.text()
            self.gfw = GroupFeedBackWindow.GroupFeedBackWindow(group_name)
            self.gfw.show()
            self.group_feedback_textbox.clear()

    def upload_data(self):
        main.cursor.execute('''
        SELECT * FROM Students
        ''')
        records = main.cursor.fetchall()
        main.connection.commit()
        self.table.setRowCount(len(records))
        self.show_table(records)

    def sort_data(self):
        if self.sort_data_combobox.currentText() == 'Назв группы':
            main.cursor.execute('''
            SELECT * FROM Students
            ORDER BY group_name
            ''')
        elif self.sort_data_combobox.currentText() == 'Фамилия':
            main.cursor.execute('''
            SELECT * FROM Students
            ORDER BY surname
            ''')
        elif self.sort_data_combobox.currentText() == 'Общ работа':
            main.cursor.execute('''
            SELECT * FROM Students
            ORDER BY social_activities DESC
            ''')
        else:
            main.cursor.execute('''
            SELECT * FROM Students
            ORDER BY salary DESC
            ''')
        records = main.cursor.fetchall()
        main.connection.commit()
        self.show_table(records)

    def show_rating(self):
        self.rw = RatingWindow.RatingWindow()
        self.rw.show()
    
    def inverse_best(self):
        main.cursor.execute('''
        UPDATE Students
        SET social_activities = NOT social_activities
        WHERE marks = '55555'
        ''')
        main.connection.commit()
        self.upload_data()

    def count_activities(self):
        main.cursor.execute('''
        SELECT Count(*) FROM Students WHERE social_activities = 1
        ''')
        activities_count = main.cursor.fetchall()[0][0]
        main.connection.commit()
        main.show_information('Количество\nактивистов: ' + str(activities_count))

    def delete_outsiders(self):
        self.ow = OutsidersWindow.OutsidersWindow() 
        self.ow.show()
        main.cursor.execute('''
        DELETE FROM Students
        WHERE length(marks) - length(replace(marks, '2', '')) > 0
        ''')
        main.connection.commit()
        self.upload_data()

    def delete_data(self):
        main.cursor.execute('''
        DROP TABLE IF EXISTS Students
        ''')
        self.table.setRowCount(0)
        main.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            group_name TEXT NOT NULL,
            surname TEXT NOT NULL PRIMARY KEY,
            marks TEXT NOT NULL,
            social_activities BOOL,
            salary INTEGER
        )
        ''')
        main.connection.commit()
