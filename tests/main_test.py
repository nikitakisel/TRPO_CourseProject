import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main


def test_count_activities():
    main.cursor.execute('''
    SELECT Count(*) FROM Students WHERE social_activities = 1
    ''')
    activities_count = main.cursor.fetchall()[0][0]
    main.connection.commit()
    assert activities_count


def test_inverse_best():
    main.cursor.execute('''
    SELECT Count(*) FROM Students WHERE social_activities = 1
    ''')
    count_begin = main.cursor.fetchall()[0][0]
    main.connection.commit()

    main.cursor.execute('''
    UPDATE Students
    SET social_activities = NOT social_activities
    WHERE marks = '55555'
    ''')
    main.connection.commit()

    main.cursor.execute('''
    SELECT Count(*) FROM Students WHERE social_activities = 1
    ''')
    count_end = main.cursor.fetchall()[0][0]
    main.connection.commit()

    assert abs(count_end - count_begin)
