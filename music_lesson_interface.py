import sqlite3
from tabulate import tabulate

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

print_query("all_info")