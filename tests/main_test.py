import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main


def test_add_note():
    main.cursor.execute('''
        SELECT Count(*) FROM Students
        ''')
    count_begin = main.cursor.fetchall()[0][0]
    main.connection.commit()

    data = [
        ['23-к-кт2', 'Иванов', '53453', False],
        ['2-кб-пр4', 'Зайцев', '53453', True],
        ['', 'Сахаров', '34455', False],
        ['24-км-ас1', 'Бурунов', '13444', True],
        ['24-км-ас1', 'Актов', '3433', True],
        ['23-кб-пи', 'Смолов', '43454', True],
        ['21-к-кт7', 'Смолов', '45554', True],
        ['23-кб-пи2', 'Иванов', '54454', True],
    ]

    for item in data:
        group_name, surname, marks, social_activities = map(str, item)
        main.cursor.execute('''
                SELECT surname FROM Students
                ''')
        records = main.cursor.fetchall()
        main.connection.commit()

        group_name_pattern = re.compile(r'[0-9]{2}([-][к])(?:[а-я]|)+[-]([а-я]{2})[1-6]')

        if not(group_name == '' or surname == '' or marks == '' \
                or (surname,) in records or not group_name_pattern.match(group_name) \
                or len(marks) != 5 or sum([marks.count('2'), marks.count('3'), marks.count('4'),
                                           marks.count('5'), marks.count('_')]) != 5):

            main.cursor.execute('''
                    INSERT INTO Students (group_name, surname, marks, social_activities) VALUES (?, ?, ?, ?);
                    ''', (group_name, surname, marks, social_activities))
            main.connection.commit()

    main.cursor.execute('''
            SELECT Count(*) FROM Students
            ''')
    count_end = main.cursor.fetchall()[0][0]
    main.connection.commit()

    assert count_end - count_begin == 1


def test_delete_note():
    main.cursor.execute('''
            SELECT Count(*) FROM Students
            ''')
    count_begin = main.cursor.fetchall()[0][0]
    main.connection.commit()

    main.cursor.execute('''
            SELECT surname FROM Students
            ''')
    records = main.cursor.fetchall()
    main.connection.commit()

    surname = 'Иванов'

    if (surname,) in records:
        main.cursor.execute('''
                DELETE FROM Students WHERE surname = ?
                ''', (surname,))
        main.connection.commit()

    main.cursor.execute('''
                SELECT Count(*) FROM Students
                ''')
    count_end = main.cursor.fetchall()[0][0]
    main.connection.commit()

    assert count_begin - count_end == 1


def test_count_activities():
    main.cursor.execute('''
    SELECT Count(*) FROM Students WHERE social_activities = 1
    ''')
    activities_count = main.cursor.fetchall()[0][0]
    main.connection.commit()
    assert activities_count


def test_inverse_best():
    main.cursor.execute('''
    SELECT Count(*) FROM Students WHERE marks = '55555' AND social_activities = 1
    ''')
    count_activities_begin = main.cursor.fetchall()[0][0]
    main.connection.commit()

    main.cursor.execute('''
    UPDATE Students
    SET social_activities = NOT social_activities
    WHERE marks = '55555'
    ''')
    main.connection.commit()

    main.cursor.execute('''
    SELECT Count(*) FROM Students WHERE marks = '55555' AND social_activities = 1
    ''')
    count_activities_end = main.cursor.fetchall()[0][0]
    main.connection.commit()

    main.cursor.execute('''
        SELECT Count(*) FROM Students WHERE marks = '55555'
        ''')
    count_perfect = main.cursor.fetchall()[0][0]
    main.connection.commit()

    assert count_activities_begin + count_activities_end == count_perfect


def test_delete_outsiders():
    main.cursor.execute('''
            SELECT Count(*) FROM Students
            ''')
    count_begin = main.cursor.fetchall()[0][0]
    main.connection.commit()

    data = [
        ['23-кб-пр4', 'Спецрянов', '24453', False],
        ['22-км-иб2', 'Глебовский', '33323', False],
        ['24-кб-ас4', 'Татаренский', '34432', True],
        ['21-к-кб2', 'Батчи', '22342', False],
        ['22-кб-ит3', 'Эльдаренкосалам', '53342', True]
    ]

    for item in data:
        group_name, surname, marks, social_activities = map(str, item)
        main.cursor.execute('''
                    INSERT INTO Students (group_name, surname, marks, social_activities) VALUES (?, ?, ?, ?);
                    ''', (group_name, surname, marks, social_activities))
        main.connection.commit()

    main.cursor.execute('''
            DELETE FROM Students
            WHERE length(marks) - length(replace(marks, '2', '')) > 0
            ''')
    main.connection.commit()

    main.cursor.execute('''
                SELECT Count(*) FROM Students
                ''')
    count_end = main.cursor.fetchall()[0][0]
    main.connection.commit()

    assert count_begin == count_end
