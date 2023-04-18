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


# creates subjects table
#c.execute("""
 #         CREATE TABLE subjects(
  #      subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
   #     subject_name TEXT
    #          )
     #    """)
     
#c.execute("INSERT INTO subjects(subject_name) VALUES('Geometry')")

 #adding class table
#c.execute("""
 #         CREATE TABLE classes(
  #       class_id INTEGER PRIMARY KEY AUTOINCREMENT,
   #       subject_id TEXT,
    #      teacher_id TEXT,
     #     block INTEGER
      #   ) """)

#c.execute("INSERT INTO classes(subject_id,teacher_id,block) VALUES(2,1,1)")

#see all classes
c.execute("SELECT * FROM classes")

#getting what teachers teach what classes
c.execute("""SELECT subjects.subject_name,teachers.first,teachers.last FROM classes
          JOIN teachers ON classes.teacher_id=teachers.teacher_id 
          JOIN subjects ON classes.subject_id=subjects.subject_id """)
print(c.fetchall())
conn.commit()
conn.close()

