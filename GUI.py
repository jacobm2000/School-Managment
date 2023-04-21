import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import sqlite3

def deleteStudent():
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("Select * from Students WHERE student_id=?",[sbox.get(1.0,'end-1c')])
    x=c.fetchall()
    #checks if the id is a valid id in the table
    if(x==[]):
        tk.messagebox.showinfo(title="Error", message="Student id not found")
    else:
        c.execute("DELETE FROM students WHERE student_id =?",[sbox.get(1.0,'end-1c')])
        tk.messagebox.showinfo(title="", message="Student Removed")
    sbox.delete(1.0,'end-1c')
    conn.commit()
    conn.close()
    
def deleteTeacher():
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("Select * from teachers WHERE teacher_id=?",[tbox.get(1.0,'end-1c')])
    x=c.fetchall()
    #checks if the id is a valid id in the table
    if(x==[]):
        tk.messagebox.showinfo(title="Error", message="Teacher id not found")
    else:
        c.execute("DELETE FROM teachers where teacher_id =?",[tbox.get(1.0,'end-1c')])
        tk.messagebox.showinfo(title="", message="Teacher Removed")
    tbox.delete(1.0,'end-1c')
    conn.commit()
    conn.close()

def deleteClass():
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("Select * from classes WHERE class_id=?",[cbox.get(1.0,'end-1c')])
    x=c.fetchall()
    #checks if the id is a valid id in the table
    if(x==[]):
        tk.messagebox.showinfo(title="Error", message="class id not found")
    else:
        c.execute("DELETE FROM classes where class_id =?",[cbox.get(1.0,'end-1c')])
        tk.messagebox.showinfo(title="", message="class Removed")
    cbox.delete(1.0,'end-1c')
    conn.commit()
    conn.close()
    
def deleteSubject():
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("Select * from subjects WHERE subject_id=?",[subbox.get(1.0,'end-1c')])
    x=c.fetchall()
    #checks if the id is a valid id in the table
    if(x==[]):
        tk.messagebox.showinfo(title="Error", message="subject id not found")
    else:
        c.execute("DELETE FROM subjects where subject_id =?",[subbox.get(1.0,'end-1c')])
        tk.messagebox.showinfo(title="", message="subject Removed")
    cbox.delete(1.0,'end-1c')
    conn.commit()
    conn.close()


def newStudentWindow():
    #this code inserts the new student into The database and then Closes the window
    def addNew(first,last,g):
        conn=sqlite3.connect('studentManagment.db')
        c=conn.cursor()
        c.execute("INSERT INTO students(first,last,grade) VALUES(?,?,?)",(first,last,g))
        conn.commit()
        conn.close()
        top.destroy()
    
    #top is a new window that pops up to add a new student to the students table
    top=tk.Toplevel(root)
    tk.Label(top,text="First Name").pack()
    fname=tk.Text(top,width=20,height=1)
    fname.pack()
    tk.Label(top,text="Last Name").pack()
    lname=tk.Text(top,width=20,height=1)
    lname.pack()
    tk.Label(top,text="Grade").pack()
    grade=tk.Text(top,width=20,height=1)
    grade.pack()
    tk.Button(top,text="add",command=lambda: addNew(fname.get(1.0,'end-1c'),lname.get(1.0,'end-1c'),grade.get(1.0,'end-1c') )).pack()
def getStudents():
    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("SELECT * FROM students")
    df=pd.DataFrame(c.fetchall())
   
    df.columns=['student_id','First','Last','Grade']
    df.set_index('student_id',inplace=True)
    obox.insert('end-1c',df)
    conn.close()
    
def getTeachers():
    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Teachers")
    df=pd.DataFrame(c.fetchall())
   
    df.columns=['Teacher_id','First','Last']
    df.set_index('Teacher_id',inplace=True)
    obox.insert('end-1c',df)

def getClasses():
    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("""SELECT classes.class_id,subjects.subject_name,teachers.first,teachers.last,classes.block FROM classes 
              JOIN teachers ON classes.teacher_id=teachers.teacher_id
              JOIN subjects on classes.subject_id=subjects.subject_id""")
    df=pd.DataFrame(c.fetchall())
    df.columns=['class_id','Subject','First','Last','Block']
    df.set_index('class_id',inplace=True)
    obox.insert('end-1c',df)
    
def getSubjects():
    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Subjects")
    df=pd.DataFrame(c.fetchall())
   
    df.columns=['Subject_id','Subject']
    df.set_index('Subject_id',inplace=True)
    obox.insert('end-1c',df)
    conn.close()
    
def newTeacherWindow():
    #this code inserts the new Teacher into The database and then Closes the window
    def addNew(first,last):
        conn=sqlite3.connect('studentManagment.db')
        c=conn.cursor()
        c.execute("INSERT INTO teachers(first,last) VALUES(?,?)",(first,last))
        conn.commit()
        conn.close()
        top.destroy()
    
    #top is a new window that pops up to add a new Teacher to the teachers table
    top=tk.Toplevel(root)
    tk.Label(top,text="First Name").pack()
    fname=tk.Text(top,width=20,height=1)
    fname.pack()
    tk.Label(top,text="Last Name").pack()
    lname=tk.Text(top,width=20,height=1)
    lname.pack()
    tk.Button(top,text="add",command=lambda: addNew(fname.get(1.0,'end-1c'),lname.get(1.0,'end-1c') )).pack()

def newSubjectWindow():
    #this code inserts the new subject into The database and then Closes the window
    def addNew(subject):
        conn=sqlite3.connect('studentManagment.db')
        c=conn.cursor()
        c.execute("INSERT INTO subjects(subject_name) VALUES(?)",([subject]))
        conn.commit()
        conn.close()
        top.destroy()
    
    #top is a new window that pops up to add a new Subject to the subject table
    top=tk.Toplevel(root)
    tk.Label(top,text="Subject").pack()
    subject=tk.Text(top,width=20,height=1)
    subject.pack()
    
    tk.Button(top,text="add",command=lambda: addNew(subject.get(1.0,'end-1c') )).pack()
def newClassWindow():
    #this code inserts the new Class into The database and then Closes the window
    def addNew(s_id,t_id,block):
        conn=sqlite3.connect('studentManagment.db')
        c=conn.cursor()
        c.execute("INSERT INTO classes(subject_id,teacher_id,block) VALUES(?,?,?)",(s_id,t_id,block))
        conn.commit()
        conn.close()
        top.destroy()
    
    #top is a new window that pops up to add a new Class to the classes table
    top=tk.Toplevel(root)
    tk.Label(top,text="Subject_id").pack()
    s_id=tk.Text(top,width=20,height=1)
    s_id.pack()
    tk.Label(top,text="Teacher_id").pack()
    t_id=tk.Text(top,width=20,height=1)
    t_id.pack()
    tk.Label(top,text="Block").pack()
    block=tk.Text(top,width=20,height=1)
    block.pack()
    
    tk.Button(top,text="add",command=lambda: addNew(s_id.get(1.0,'end-1c'),t_id.get(1.0,'end-1c'),block.get(1.0,'end-1c') )).pack()
def getStudents():
    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("SELECT * FROM students")
    df=pd.DataFrame(c.fetchall())
   
    df.columns=['student_id','First','Last','Grade']
    df.set_index('student_id',inplace=True)
    obox.insert('end-1c',df)
    conn.close()
def getTeachers():
    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Teachers")
    df=pd.DataFrame(c.fetchall())
   
    df.columns=['Teacher_id','First','Last']
    df.set_index('Teacher_id',inplace=True)
    obox.insert('end-1c',df)
    
root = tk.Tk()
root.title('Student Manager')
#output box that shows data
obox=tk.Text(root,height=10,width=50)
obox.pack()
#Button to display all students to the output box
b1=tk.Button(root, text="Get Students",command=getStudents)
b1.pack()
#Button to display all teachers to the output box
b2=tk.Button(root, text="Get Teachers",command=getTeachers)
#button to see all classes
b3=tk.Button(root, text="Get Classes",command=getClasses)
#button to see all classes
b4=tk.Button(root, text="Get Subjects",command=getSubjects)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
#Text box to enter student id of the student the user wishes to remove from the stutends table
sbox=tk.Text(root,width=5,height=1)
sbox.pack()
slabel=tk.Label(root,text="Student Id To Delete")
slabel.pack()
#When pressed deletes the student with the id entered in the textbox above
dbutton=tk.Button(root,text="delete",command=deleteStudent)
dbutton.pack()
#Text box to enter teacher id of the teacher the user wishes to remove from the teachers table
tbox=tk.Text(root,width=5,height=1)
tbox.pack()
tlabel=tk.Label(root,text="Teacher Id To Delete")
tlabel.pack()


#When pressed deletes the teacher with the id entered in the textbox above
dbutton2=tk.Button(root,text="delete",command=deleteTeacher)
dbutton2.pack()


cbox=tk.Text(root,width=5,height=1)
cbox.pack()

clabel=tk.Label(root,text="Class Id To Delete")
clabel.pack()

#When pressed deletes the class with the id entered in the textbox above
dbutton3=tk.Button(root,text="delete",command=deleteClass)
dbutton3.pack()


subbox=tk.Text(root,width=5,height=1)
subbox.pack()

sublabel=tk.Label(root,text="Subject Id To Delete")
sublabel.pack()

#When pressed deletes the class with the id entered in the textbox above
dbutton4=tk.Button(root,text="delete",command=deleteSubject)
dbutton4.pack()

#when pressed opens a new window for adding a new student
b5=tk.Button(text="Add New Student",command=newStudentWindow)
b5.pack()

#when pressed opens a new window for adding a new student
b6=tk.Button(text="Add New Teacher",command=newTeacherWindow)
b6.pack()

#when pressed opens a new window for adding a new Class
b7=tk.Button(text="Add New Class",command=newClassWindow)
b7.pack()
#when pressed opens a new window for adding a new Class
b8=tk.Button(text="Add New subject",command=newSubjectWindow)
b8.pack()

root.mainloop()