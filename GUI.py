import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import sqlite3

def deleteStudent():
    conn=sqlite3.connect('studentManagment.db')
    c=conn.cursor()
    c.execute("DELETE FROM students where student_id =?",sbox.get(1.0,'end-1c'))
    conn.commit()
    conn.close

    
    
    
    
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
b1.pack()
b2.pack()
#Text box to enter student id of the student the user wishes to remove from the stutends table
sbox=tk.Text(root,width=5,height=1)
sbox.pack()
slabel=tk.Label(root,text="student Id to delete")
slabel.pack()
#When pressed deletes the student with the id entered in the textbox above
dbutton=tk.Button(root,text="delete",command=deleteStudent)
dbutton.pack()

#when pressed opens a new window for adding a new student
b3=tk.Button(text="add new student",command=newStudentWindow)
b3.pack()
root.mainloop()