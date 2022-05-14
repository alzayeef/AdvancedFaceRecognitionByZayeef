from os import stat
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      #=================variable=============
      self.var_atten_id=StringVar()
      self.var_atten_roll=StringVar()
      self.var_atten_name=StringVar()
      self.var_atten_dept=StringVar()
      self.var_atten_time=StringVar()
      self.var_atten_date=StringVar()
      self.var_atten_attendance=StringVar()


      #first image
      img=Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\campus.jpg")
      img=img.resize((600,150),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=600,height=150)

      #second img

      img1=Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\logo.png")
      img1=img1.resize((300,150),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      f_lbl=Label(self.root,image=self.photoimg1)
      f_lbl.place(x=650,y=0,width=300,height=150)
      
      #third image

      img2=Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\campus1.jpg")
      img2=img2.resize((510,150),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=1000,y=0,width=510,height=150)
      
      #background image
      img0 = Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\single.jpg")
      img0 = img0.resize((1530, 710), Image.ANTIALIAS)
      self.photoimg0 = ImageTk.PhotoImage(img0)

      bg_img = Label(self.root, image=self.photoimg0)
      bg_img.place(x=0, y=150, width=1530, height=710)

      title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",30,"bold"),bg="green",fg="white")
      title_lbl.place(x=0,y=0,width=1530,height=50)

      main_frame=Frame(bg_img,bd=2,bg="white")
      main_frame.place(x=0,y=51,width=1530,height=650)
      
      #==========left frame==================
      Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",15,"bold"))
      Left_frame.place(x=10,y=10,width=750,height=550)

      img_left=Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\batch1.jpg")
      img_left=img_left.resize((730,120),Image.ANTIALIAS)
      self.photoimg_left=ImageTk.PhotoImage(img_left)

      f_lbl=Label(Left_frame,image=self.photoimg_left)
      f_lbl.place(x=5,y=0,width=730,height=120)

      
      left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
      left_inside_frame.place(x=0,y=125,width=720,height=370)

      #Labeland entry

#==============attendance id=================

      attendanceId_label=Label(left_inside_frame,text="Reg. NO:",font=("times new roman",12,"bold"),bg="white")
      attendanceId_label.grid(row=0,column=0,padx=5,pady=2,sticky=W)


      attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",15,"bold"))
      attendanceId_entry.grid(row=0,column=1,padx=5,pady=2,sticky=W)
      

      #=====================Roll===================================


      rollLabel=Label(left_inside_frame,text="Roll",font=("times new roman",12,"bold"),bg="white")
      rollLabel.grid(row=0,column=2,padx=5,pady=5)


      atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
      atten_roll.grid(row=0,column=3,pady=5)

   #==================name=============================
      nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
      nameLabel.grid(row=1,column=0,padx=5,pady=5)


      atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font="comicsansns 11 bold")
      atten_name.grid(row=1,column=1,padx=5,pady=5)

    
     
 #======================department===================================


      depLabel=Label(left_inside_frame,text="Department:",font="comicsansns 11 bold",bg="white")
      depLabel.grid(row=1,column=2,padx=5,pady=5)


      atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dept,font="comicsansns 11 bold")
      atten_dep.grid(row=1,column=3,padx=5,pady=5)



#======================time===================================


      timeLabel=Label(left_inside_frame,text="Time:",font="comicsansns 11 bold",bg="white")
      timeLabel.grid(row=2,column=0,padx=5,pady=5,sticky=W)


      atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font="comicsansns 11 bold")
      atten_time.grid(row=2,column=1,padx=5,pady=5,sticky=W)


        
#======================date===================================


      dateLabel=Label(left_inside_frame,text="Dete:",font="comicsansns 11 bold",bg="white")
      dateLabel.grid(row=2,column=2,padx=5,pady=5,sticky=W)


      atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font="comicsansns 11 bold")
      atten_date.grid(row=2,column=3,padx=5,pady=5,sticky=W)


      #===========attendence=====================
      
      AttendanceLabel=Label(left_inside_frame,text="Attendance Status",font="comicsansns 11 bold",bg="white")
      AttendanceLabel.grid(row=3,column=0,padx=5,pady=5,sticky=W)


      self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
      self.atten_status["values"]=("Status","Present","Absent")
      self.atten_status.grid(row=3,column=1,pady=8)
      self.atten_status.current(0)
       
       #buttonsframe
      btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame.place(x=0,y=300, width=725, height=35)

      save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,
      width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
      save_btn.grid(row=0, column=0)
      update_btn = Button(btn_frame, width=17,text="Export CSV", command=self.exportCsv,font=("times new roman", 13, "bold"), bg="blue", fg="white")
      update_btn.grid(row=0, column=1)

      delete_btn = Button(btn_frame, width=17, text="Update", font=("times new roman", 13, "bold"), bg="blue", fg="white")
      delete_btn.grid(row=0, column=2)

      reset_btn = Button(btn_frame, width=17, text="Reset",command=self.reset_data,font=("times new roman", 13, "bold"), bg="blue", fg="white")
      reset_btn.grid(row=0, column=3)

  #=============Right Frame======================
      Right_frame = LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE, text="Attendance Details",font=("times new roman", 15, "bold"),fg="black")
      Right_frame.place(x=770, y=10, width=740, height=550)

      table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
      table_frame.place(x=5,y=5, width=720, height=445)


      #=========Score bar table===========
      
      
      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

      self.AttendanceReportTable=ttk.Treeview(table_frame,column=("reg","roll","name","dept","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      
      scroll_x.config(command=self.AttendanceReportTable.xview)
      scroll_y.config(command=self.AttendanceReportTable.yview)
      
      self.AttendanceReportTable.heading("reg",text="Reg. No")
      self.AttendanceReportTable.heading("roll",text="Roll")
      self.AttendanceReportTable.heading("name",text="Name")
      self.AttendanceReportTable.heading("dept",text="Department")
      self.AttendanceReportTable.heading("time",text="Time")

      self.AttendanceReportTable.heading("date",text="Date")
      self.AttendanceReportTable.heading("attendance",text="Attendance")
       
      
      self.AttendanceReportTable["show"]="headings"

      self.AttendanceReportTable.column("reg",width=100)
      self.AttendanceReportTable.column("roll",width=100)
      self.AttendanceReportTable.column("name",width=100)
      self.AttendanceReportTable.column("dept",width=100)
      self.AttendanceReportTable.column("time",width=100)
      self.AttendanceReportTable.column("date",width=100)
      self.AttendanceReportTable.column("attendance",width=100)
    
         
      
      self.AttendanceReportTable.pack(fill=BOTH,expand=1)

      self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


      #=====================fetch data===============

   def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
             self.AttendanceReportTable.insert("",END,values=i)
#=============import csv

   def importCsv(self):
         global mydata
         mydata.clear()
         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
         with open(fln) as myfile:
               csvread=csv.reader(myfile,delimiter=",")
               for i in csvread:
                  mydata.append(i)
               self.fetchData(mydata)
   

   #=================export==============

   def exportCsv(self):
      try:
         if len(mydata)<1:
          messagebox.showerror("No Data","No Data found to export",parent=self.root)
          return False
         fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
         with open(fln,mode="w",newline="") as myfile:
            exp_write=csv.writer(myfile,delimiter=",")
            for i in mydata:
               exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
      except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
      
   def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content['values']
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dept.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])

   def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dept.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")
            
            


if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()