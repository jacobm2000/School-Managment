# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:07:50 2023

@author: maure
"""

import sqlite3
conn=sqlite3.connect('studentManagment.db')
c=conn.cursor()


 #creates student table
#c.execute("""
        #  CREATE TABLE students
#         (
       #  student_id INTEGER PRIMARY KEY AUTOINCREMENT ,
#          first TEXT,
#          last TEXT,
      #   grade INTEGER
      #    )
     #     """)
#c.execute(" INSERT INTO students(first,last,grade) VALUES('jimmy','smith',9)")
c.execute("SELECT * FROM students")
print(c.fetchall())
conn.commit()

#Creates the teacher table
#c.execute("""CREATE TABLE teachers(
 #   teacher_id INTEGER PRIMARY KEY AUTOINCREMENT ,
  #  first TEXT,
   # last TEXT
    #)""")
    
#c.execute("INSERT INTO teachers(first,last) VALUES('John','Adams')")

c.execute("select * from teachers")
print(c.fetchall())
conn.commit()

# adding class table
#c.execute("""
 #         CREATE TABLE classes(
  #        class_id INTEGER PRIMARY KEY AUTOINCREMENT,
   #       class_name TEXT,
    #      teacher_id TEXT,
     ##    ) """)
#c.execute("INSERT INTO classes(class_name,teacher_id,block) VALUES('Geometry',2,1)")

#see all classes
c.execute("SELECT * FROM classes")

#getting what teachers teach what classes
c.execute("SELECT classes.class_name,teachers.first,teachers.last FROM classes JOIN teachers ON classes.teacher_id=teachers.teacher_id ")
print(c.fetchall())
conn.commit()
conn.close()

