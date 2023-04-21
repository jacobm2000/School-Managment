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

#c.execute("INSERT INTO classes(subject_id,teacher_id,block) VALUES(2,5,1)")

#see all classes
c.execute("SELECT * FROM classes")

#getting what teachers teach what classes
c.execute("""SELECT subjects.subject_name,teachers.first,teachers.last FROM classes
          JOIN teachers ON classes.teacher_id=teachers.teacher_id 
          JOIN subjects ON classes.subject_id=subjects.subject_id """)
print(c.fetchall())
          
#creates table that connects students to classes they are enrolled in
#c.execute("""
 #          CREATE TABLE StudentToClass(
  #         id INTEGER PRIMARY KEY AUTOINCREMENT,
   #        student_id INTEGER,
    #       class_id INTEGER
     #          )
      #     """)
#c.execute("INSERT INTO studentToClass(student_id,class_id) VALUES(1,1)")

c.execute("""SELECT students.first,students.last,subjects.subject_name,teachers.last 
          FROM students JOIN studentToClass ON students.student_id=studentToClass.student_id
          JOIN classes ON classes.class_id=studentToClass.class_id
          JOIN subjects ON classes.subject_id=subjects.subject_id
          JOIN teachers ON teachers.teacher_id=classes.teacher_id""")

print(c.fetchall())
conn.commit()
conn.close()

