import sqlite3
from tabulate import tabulate
import sys
from easygui import *

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
    print(tabulate(results,headings))
    db.close()

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  

msg ="What do you want to see?"
title = "Music lessons"
choices = ["Queries", "Day", "School", "Gender", "Instrument", "Year of birth"]
choice = choicebox(msg, title, choices)

if choice == "Queries":
    msg ="What do you want to see?"
    title = "Music lessons"
    choices = ["afternoon_lessons", "all_info", "drummers", "monday_lessons", "morning_lessons", "music_fees"]
    query = choicebox(msg, title, choices)
    print_query(query)

elif choice == "Day":
    msg ="What do you want to see?"
    title = "Music lessons"
    choices = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = choicebox(msg, title, choices)
    print_parameter_query("name, surname, instrument, lesson_time, lesson_day", "lesson_day = ? ORDER BY lesson_time Asc",day)

elif choice == "School":
    msg ="Which school?"
    title = "Music lessons"
    choices = ["LMS", "BKI", "CLS", "SPS"]
    school = choicebox(msg, title, choices)
    print_parameter_query("name, surname, instrument, school, lesson_time, lesson_day", "school = ? ORDER BY lesson_time Asc",school)
elif choice == "Gender":
    print("not done")
elif choice == "Instrument":
    print("not done")
elif choice == "Year of birth":
    print("not done")