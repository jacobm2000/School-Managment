import tkinter as tk
from tkinter import StringVar
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


def editStudentWindow():
   
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
     #this code updates student entry
    def update(first,last,g,ID):
        c.execute("UPDATE students SET first=?,last=?,grade=? WHERE student_id=?",(first,last,g,ID))
        conn.commit()
        conn.close()
        top.destroy()
    #checks to see if the student Id box is empty and if it is an error will display
    if(sbox.get(1.0,'end-1c')==''):
        tk.messagebox.showinfo(title="Error", message="Student Id box is empty")
    else:
        c.execute("SELECT * FROM students WHERE student_id=?",[sbox.get(1.0,'end-1c')])
        x=c.fetchall()
    #checks to see if the student id exists and if it dosn't an error will popup
    if(x==[]):
        tk.messagebox.showinfo(title="Error", message="Student id not found")

    else:
        df=pd.DataFrame(x)
        df.columns=['student_id','First','Last','Grade']
       
        #top is a new window that pops up to edit an existing student
        top=tk.Toplevel(root)
        tk.Label(top,text="First Name").pack()
        fname=tk.Text(top,width=20,height=1)
        fname.insert('end-1c',df['First'][0])
        fname.pack()
        tk.Label(top,text="Last Name").pack()
        lname=tk.Text(top,width=20,height=1)
        lname.insert('end-1c',df['Last'][0])
        lname.pack()
        tk.Label(top,text="Grade").pack()
        grade=tk.Text(top,width=20,height=1)
        grade.insert('end-1c',df["Grade"][0])
        grade.pack()
        ub=tk.Button(top,text="Update",command=lambda: update(fname.get(1.0,'end-1c'),lname.get(1.0,'end-1c'),grade.get(1.0,'end-1c'),sbox.get(1.0,'end-1c')))
        ub.pack()
        
def editTeacherWindow():
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
        #this code updates teacher entry
    def update(first,last,ID):
        c.execute("UPDATE teachers SET first=?,last=? WHERE teacher_id=?",(first,last,ID))
        conn.commit()
        conn.close()
        top.destroy()
    #checks to see if the teacher Id box is empty and if it is an error will display
    if(tbox.get(1.0,'end-1c')==''):
        tk.messagebox.showinfo(title="Error", message="Teacher Id box is empty")
    else:
        c.execute("SELECT * FROM teachers WHERE teacher_id=?",[tbox.get(1.0,'end-1c')])
        x=c.fetchall()
    #checks to see if the teacher id exists and if it dosn't an error will popup
    if(x==[]):
        tk.messagebox.showinfo(title="Error", message="Teacher id not found")

    else:
        df=pd.DataFrame(x)
        df.columns=['teacher_id','First','Last']
       
        #top is a new window that pops up to edit an existing teacher
        top=tk.Toplevel(root)
        tk.Label(top,text="First Name").pack()
        fname=tk.Text(top,width=20,height=1)
        fname.insert('end-1c',df['First'][0])
        fname.pack()
        tk.Label(top,text="Last Name").pack()
        lname=tk.Text(top,width=20,height=1)
        lname.insert('end-1c',df['Last'][0])
        lname.pack()
        tk.Label(top,text="Grade").pack()
        ub=tk.Button(top,text="Update",command=lambda: update(fname.get(1.0,'end-1c'),lname.get(1.0,'end-1c'),tbox.get(1.0,'end-1c')))
        ub.pack()

def editClassWindow():
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
        #this code updates teacher entry
    def update(subject_id,teacher_id,block,ID):
        c.execute("UPDATE classes SET subject_id=?,teacher_id=?,block=? WHERE class_id=?",(subject_id,teacher_id,block,ID))
        conn.commit()
        conn.close()
        top.destroy()
    #checks to see if the teacher Id box is empty and if it is an error will display
    if(cbox.get(1.0,'end-1c')==''):
        tk.messagebox.showinfo(title="Error", message="Class Id box is empty")
    else:
        c.execute("SELECT * FROM classes WHERE class_id=?",[cbox.get(1.0,'end-1c')])
        x=c.fetchall()
    #checks to see if the teacher id exists and if it dosn't an error will popup
    if(x==[]):
        tk.messagebox.showinfo(title="Error", message="Class id not found")

    else:
        df=pd.DataFrame(x)
        df.columns=['class_id','subject_id','teacher_id','block']
       
        #top is a new window that pops up to edit an existing teacher
        top=tk.Toplevel(root)
        tk.Label(top,text="Subject Id").pack()
        subID=tk.Text(top,width=20,height=1)
        subID.insert('end-1c',df['subject_id'][0])
        subID.pack()
        tk.Label(top,text="Teacher_id").pack()
        tID=tk.Text(top,width=20,height=1)
        tID.insert('end-1c',df['teacher_id'][0])
        tID.pack()
        tk.Label(top,text="Block").pack()
        block=tk.Text(top,width=20,height=1)
        block.insert('end-1c',df['block'][0])
        block.pack()
        tk.Label(top,text="Grade").pack()
        ub=tk.Button(top,text="Update",command=lambda: update(subID.get(1.0,'end-1c'),tID.get(1.0,'end-1c'),block.get(1.0,'end-1c'),cbox.get(1.0,'end-1c')))
        ub.pack()


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
    
def studentSearch():

    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("SELECT * FROM students WHERE last=?",[searchbox.get(1.0,'end-1c')])
    x=c.fetchall()
    if(x==[]):
        obox.insert('end-1c','No Students Found')
    else:
        df=pd.DataFrame(x)
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

def teacherSearch():

    obox.delete(1.0,'end-1c')
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("SELECT * FROM teachers WHERE last=?",[searchbox2.get(1.0,'end-1c')])
    x=c.fetchall()
    if(x==[]):
        obox.insert('end-1c','No teacher Found')
    else:
        df=pd.DataFrame(x)
        df.columns=['teacher_id','First','Last']
        df.set_index('teacher_id',inplace=True)
        obox.insert('end-1c',df)
        conn.close()


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



root = tk.Tk()
root.title('Student Manager')
root.geometry("500x500")
root.resizable(False,False)
#output box that shows data
obox=tk.Text(root,height=10,width=50)
obox.pack()

#Button to display all students to the output box
b1=tk.Button(root, text="Get Students",command=getStudents)
b1.place(x=0,y=165)
#Button to display all teachers to the output box
b2=tk.Button(root, text="Get Teachers",command=getTeachers)
b2.place(x=0,y=240)
#button to see all classes
b3=tk.Button(root, text="Get Classes",command=getClasses)
b3.place(x=0,y=320)
#button to see all classes
b4=tk.Button(root, text="Get Subjects",command=getSubjects)
b4.place(x=0,y=400)


#Text box to enter student id of the student the user wishes to remove from the stutends table
sbox=tk.Text(root,width=5,height=1)
sbox.place(x=200,y=165)
slabel=tk.Label(root,text="Student Id To Delete")
slabel.place(x=80,y=165)

searchLabel=tk.Label(root,text="Last Name")
searchLabel.place(x=0,y=200)
searchbox=tk.Text(root,width=9,height=1)
searchbox.place(x=70,y=200)
searchButton=tk.Button(root,text="search",command=studentSearch)
searchButton.place(x=150,y=195)

searchLabel2=tk.Label(root,text="Last Name")
searchLabel2.place(x=0,y=275)
searchbox2=tk.Text(root,width=9,height=1)
searchbox2.place(x=70,y=275)
searchButton2=tk.Button(root,text="search",command=teacherSearch)
searchButton2.place(x=150,y=270)


#When pressed deletes the student with the id entered in the textbox above
dbutton=tk.Button(root,text="delete",command=deleteStudent)
dbutton.place(x=250,y=165)
editStudent=tk.Button(root,text="edit",command=editStudentWindow)
editStudent.place(x=405,y=165)
editTeacher=tk.Button(root,text="edit",command=editTeacherWindow)
editTeacher.place(x=405,y=240)
editTeacher=tk.Button(root,text="edit",command=editTeacherWindow)
editClass=tk.Button(root,text="edit",command=editClassWindow)
editClass.place(x=390,y=320)
#Text box to enter teacher id of the teacher the user wishes to remove from the teachers table
tbox=tk.Text(root,width=5,height=1)
tbox.place(x=200,y=240)
tlabel=tk.Label(root,text="Teacher Id To Delete")
tlabel.place(x=80,y=240)


#When pressed deletes the teacher with the id entered in the textbox above
dbutton2=tk.Button(root,text="delete",command=deleteTeacher)
dbutton2.place(x=250,y=240)


cbox=tk.Text(root,width=5,height=1)
cbox.place(x=200,y=320)

clabel=tk.Label(root,text="Class Id To Delete")
clabel.place(x=80,y=320)

#When pressed deletes the class with the id entered in the textbox above
dbutton3=tk.Button(root,text="delete",command=deleteClass)
dbutton3.place(x=250,y=320)


subbox=tk.Text(root,width=5,height=1)
subbox.place(x=200,y=400)

sublabel=tk.Label(root,text="Subject Id To Delete")
sublabel.place(x=80,y=400)

#When pressed deletes the class with the id entered in the textbox above
dbutton4=tk.Button(root,text="delete",command=deleteSubject)
dbutton4.place(x=250,y=400)

#when pressed opens a new window for adding a new student
b5=tk.Button(text="Add New Student",command=newStudentWindow)
b5.place(x=300,y=165)

#when pressed opens a new window for adding a new student
b6=tk.Button(text="Add New Teacher",command=newTeacherWindow)
b6.place(x=300,y=240)

#when pressed opens a new window for adding a new Class
b7=tk.Button(text="Add New Class",command=newClassWindow)
b7.place(x=300,y=320)
#when pressed opens a new window for adding a new Class
b8=tk.Button(text="Add New subject",command=newSubjectWindow)
b8.place(x=300,y=400)

root.mainloop()