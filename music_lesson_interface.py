import sqlite3
from tabulate import tabulate
import sys
from easygui import *

PASSWORD = "password"
DB_NAME = 'music_lesson_database.db'
TABLES = (" music_lessons "
       "LEFT JOIN instruments ON music_lessons.instrument_id = instruments.instrument_id "
       "LEFT JOIN parents ON music_lessons.parent_id = parents.parent_id "
       "LEFT JOIN schools ON music_lessons.school_id = schools.school_id ")

def print_query(view_name:str):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    codebox(tabulate(results,headings))
    db.close()

def print_parameter_query(fields:str, where:str, parameter):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    codebox(tabulate(results,fields.split(",")))
    db.close()  

while True:
    msg = "Enter your password"
    title = "Music lessons"
    password = passwordbox(msg, title)
    if password == PASSWORD:
        msgbox(msg = "Success", title = "Music lessons")
        break
    elif password == None:
        sys.exit()
    msgbox(msg = "Incorrect password", title = "Music lessons")

    
while True:
    msg ="What do you want to see?"
    title = "Music lessons"
    choices = ["Queries", "Day", "School", "Gender", "Instrument", "Year of birth"]
    choice = choicebox(msg, title, choices)
    if choice == None: sys.exit()

    if choice == "Queries":
        msg ="What do you want to see?"
        title = "Music lessons"
        choices = ["afternoon_lessons", "all_info", "drummers", "monday_lessons", "morning_lessons", "music_fees"]
        query = choicebox(msg, title, choices)
        if query == None:
            continue
        print_query(query)

    elif choice == "Day":
        msg ="What do you want to see?"
        title = "Music lessons"
        choices = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        day = choicebox(msg, title, choices)
        if day == None:
            continue
        print_parameter_query("name, surname, instrument, lesson_time, lesson_day", 
                            "lesson_day = ? ORDER BY lesson_time Asc",day)

    elif choice == "School":
        msg ="Which school?"
        title = "Music lessons"
        choices = ["LMS", "BKI", "CLS", "SPS"]
        school = choicebox(msg, title, choices)
        if school == None:
            continue
        print_parameter_query("name, surname, instrument, school, lesson_time, lesson_day", 
                            "school = ? ORDER BY lesson_time Asc",school)

    elif choice == "Gender":
        msg ="Which gender?"
        title = "Music lessons"
        choices = ["M", "F"]
        gender = choicebox(msg, title, choices)
        if gender == None:
            continue
        print_parameter_query("name, surname, gender, instrument, lesson_time, lesson_day", 
                            "gender = ? ORDER BY surname Asc, name ASC",gender)

    elif choice == "Instrument":
        msg ="Which instrument?"
        title = "Music lessons"
        choices = ["Piano", "Drums", "Guitar"]
        instrument = choicebox(msg, title, choices)
        if instrument == None:
            continue
        print_parameter_query("name, surname, instrument, school, lesson_time, lesson_day", 
                            "instrument = ? ORDER BY instr('MonTueWedThuFri', lesson_day), lesson_time ASC",instrument)

    elif choice == "Year of birth":
        msg ="What year do you want to see?"
        title = "Music lessons"
        choices = ["2005", "2006", "2007", "2008", "2009", "2010", "2011" ]
        year = choicebox(msg, title, choices)
        if year == None:
            continue
        print_parameter_query("name, surname, date_of_birth, instrument, school, lesson_time, lesson_day", 
                            "date_of_birth LIKE ? ORDER BY date_of_birth Asc", f'{year}%')
    else:
        break