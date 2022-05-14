from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      # -----------variables______
      self.var_dept = StringVar()
      self.var_course = StringVar()
      self.var_year = StringVar()
      self.var_semester = StringVar()
      self.var_name = StringVar()
      self.var_reg = StringVar()
      self.var_roll = StringVar()
      self.var_gender = StringVar()
      self.var_email = StringVar()
      self.var_phone = StringVar()
      self.var_address = StringVar()
      self.var_dob = StringVar()

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

      # bg image
      img0 = Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\single.jpg")
      img0 = img0.resize((1530, 710), Image.ANTIALIAS)
      self.photoimg0 = ImageTk.PhotoImage(img0)

      bg_img = Label(self.root, image=self.photoimg0)
      bg_img.place(x=0, y=160, width=1530, height=710)


      title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",30,"bold"),bg="green",fg="white")
      title_lbl.place(x=0,y=0,width=1530,height=50)

      main_frame=Frame(bg_img,bd=2,bg="white")
      main_frame.place(x=0,y=51,width=1530,height=650)

      #left label frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
      Left_frame.place(x=10,y=10,width=750,height=570)

      img_left=Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\batch1.jpg")
      img_left=img_left.resize((730,120),Image.ANTIALIAS)
      self.photoimg_left=ImageTk.PhotoImage(img_left)

      f_lbl=Label(Left_frame,image=self.photoimg_left)
      f_lbl.place(x=5,y=0,width=730,height=120)

        #current course

      current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
      current_course_frame.place(x=10,y=120,width=735,height=150)

      #department
      dep_label=Label(current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
      dep_label.grid(row=0,column=0,padx=10,sticky=W)

      dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roman",13,"bold"),state="read only")
      dep_combo["values"]=("Select Department","Computer Science and Engineering","Management","Forestry & Environmental Science","Tourism and Hospitality Mangement")
      dep_combo.current(0)

      dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


      #course
      course_label=Label(current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
      course_label.grid(row=0,column=2,padx=10,sticky=W)

      course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="read only")
      course_combo["values"]=("Select Course","Machine Learning","Algorithm","Digital Image Processing","Computer Networking")
      course_combo.current(0)

      course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


      #year
      year_label=Label(current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
      year_label.grid(row=1,column=0,padx=10,sticky=W)

      year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="read only")
      year_combo["values"]=("Select Year","2014-15","2015-16","2016-17","2017-18","2018-19","2019-20","2021-22")
      year_combo.current(0)

      year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

      #semester

      semester_label=Label(current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
      semester_label.grid(row=1,column=2,padx=10,sticky=W)

      semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="read only")
      semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
      semester_combo.current(0)

      semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


      #Class Student Information


      class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",15,"bold"))
      class_student_frame.place(x=10,y=240,width=735,height=290)


       #student Name
      studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",15,"bold"),bg="white")
      studentName_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)


      studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",15,"bold"))
      studentName_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)


      #Student Id

      studentId_label=Label(class_student_frame,text="Reg. No:",font=("times new roman",15,"bold"),bg="white")
      studentId_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)


      studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_reg,width=20,font=("times new roman",15,"bold"))
      studentId_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

       #Roll No
      RollNo_label=Label(class_student_frame,text="Roll No:",font=("times new roman",15,"bold"),bg="white")
      RollNo_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)


      RollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",15,"bold"))
      RollNo_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)


      #gender

      gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",15,"bold"),bg="white")
      gender_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)


      #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",15,"bold"))
      #gender_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

      gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="read only")
      gender_combo["values"]=("Male","Female","Other")
      gender_combo.current(0)

      gender_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


      #Email

      email_label=Label(class_student_frame,text="Email:",font=("times new roman",15,"bold"),bg="white")
      email_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)


      email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",15,"bold"))
      email_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

      #Phone No

      phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",15,"bold"),bg="white")
      phone_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)


      phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",15,"bold"))
      phone_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)


      #Address
      address_label=Label(class_student_frame,text="Address:",font=("times new roman",15,"bold"),bg="white")
      address_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)


      address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",15,"bold"))
      address_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)


      # Date of Birth

      dob_label=Label(class_student_frame,text="Date of Birth:",font=("times new roman",15,"bold"),bg="white")
      dob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)


      dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",15,"bold"))
      dob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)



      #radio button
      self.var_radio1=StringVar()
      radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")

      radiobutton1.grid(row=5,column=0)

      radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")

      radiobutton2.grid(row=5,column=1)

      # button frame
      btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame.place(x=0,y=180, width=725, height=35)

      save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
      save_btn.grid(row=0, column=0)
      update_btn = Button(btn_frame, width=17,command=self.update_data,text="Update", font=("times new roman", 13, "bold"), bg="blue", fg="white")
      update_btn.grid(row=0, column=1)

      delete_btn = Button(btn_frame, width=17, text="Delete",command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
      delete_btn.grid(row=0, column=2)

      reset_btn = Button(btn_frame, width=17, text="Reset",command=self.reset_data,font=("times new roman", 13, "bold"), bg="blue", fg="white")
      reset_btn.grid(row=0, column=3)


      #buttonframe1
      btn_frame1= Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame1.place(x=0, y=215, width=725, height=35)

      take_photo_btn = Button(btn_frame1, width=35,command=self.generate_dataset, text="Take Photo Sample", font=("times new roman", 13, "bold"), bg="blue", fg="white")
      take_photo_btn.grid(row=1,column=0)

      update_photo_btn = Button(btn_frame1, width=35, text="Update Photo Sample", font=("times new roman", 13, "bold"),bg="blue", fg="white")
      update_photo_btn.grid(row=1, column=1)


      #Right label frame
      Right_frame = LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE, text="Student Details",font=("times new roman", 15, "bold"),fg="white")
      Right_frame.place(x=770, y=10, width=740, height=550)

      img_Right = Image.open(r"C:\Users\DELL\PycharmProjects\AdvancedFaceRecognition\project\batch1.jpg")
      img_Right = img_Right.resize((730, 120), Image.ANTIALIAS)
      self.photoimg_Right = ImageTk.PhotoImage(img_Right)

      f_lbl = Label(Right_frame, image=self.photoimg_Right)
      f_lbl.place(x=5, y=0, width=730, height=120)



      #-------search system-------
      search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
      search_frame.place(x=10,y=125,width=720,height=70)

      search_label = Label(search_frame, text="Searched by", font=("times new roman", 13, "bold"), bg="red",fg="white")
      search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)


      search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="read only",width=15)
      search_combo["values"] = ("Select", "Reg. No", "Phone No",)
      search_combo.current(0)
      search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

      search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"))
      search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

      search_btn = Button(search_frame, width=13, text="Search", font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
      search_btn.grid(row=0, column=3,padx=4)

      showAll_btn = Button(search_frame, width=13, text="Show All", font=("times new roman", 13, "bold"), bg="blue", fg="white")
      showAll_btn.grid(row=0, column=4,padx=4)

      # ----table frame_______
      table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
      table_frame.place(x=10, y=210, width=710, height=317)

      scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
      scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
      self.student_table = ttk.Treeview(table_frame, column=("dept", "course", "year", "semester", "name", "reg", "roll", "gender", "email", "phone",
      "address", "dob", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_x.config(command=self.student_table.xview)
      scroll_y.config(command=self.student_table.yview)

      self.student_table.heading("dept", text="Department")
      self.student_table.heading("course", text="Course")
      self.student_table.heading("year", text="Year")
      self.student_table.heading("semester", text="Semester")
      self.student_table.heading("name", text="Student Name")
      self.student_table.heading("reg", text="Reg.No")
      self.student_table.heading("roll", text="Roll No")
      self.student_table.heading("gender", text="Gender")
      self.student_table.heading("email", text="Email")
      self.student_table.heading("phone", text="Phone")
      self.student_table.heading("address", text="Address")
      self.student_table.heading("dob", text="Date of Birth")
      self.student_table.heading("photo", text="Photo Sample Status")
      self.student_table["show"] = "headings"

      self.student_table.column("dept", width=100)
      self.student_table.column("course", width=100)
      self.student_table.column("year", width=100)
      self.student_table.column("semester", width=100)
      self.student_table.column("name", width=100)
      self.student_table.column("reg", width=100)
      self.student_table.column("roll", width=100)
      self.student_table.column("gender", width=100)
      self.student_table.column("email", width=100)
      self.student_table.column("phone", width=100)
      self.student_table.column("address", width=100)
      self.student_table.column("dob", width=100)
      self.student_table.column("photo", width=100)

      self.student_table.pack(fill=BOTH, expand=1)
      self.student_table.bind("<ButtonRelease>",self.get_cursor)
      self.fetch_data()


   #  ======function declaration=====
   def add_data(self):
      if self.var_dept.get() == "Select Department" or self.var_name.get()=="" or self.var_reg.get()=="":
         messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
         try:
            conn=mysql.connector.connect(host="localhost",username="root",password="654321",database="advance")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.var_dept.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_reg.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_radio1.get()

                                                                                                      ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
         except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#=============================fetch data==========================
   def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="654321",database="advance")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from student")
    data=my_cursor.fetchall()

    if len(data)!=0:
       self.student_table.delete(*self.student_table.get_children())
       for i in data:
           self.student_table.insert("",END,values=i)
       conn.commit()
    conn.close()

    #============get cursor=================

   def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content= self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dept.set(data[0]),
       self.var_course.set(data[1]),
       self.var_year.set(data[2]),
       self.var_semester.set(data[3]),
       self.var_name.set(data[4]),
       self.var_reg.set(data[5]),
       self.var_roll.set(data[6]),
       self.var_gender.set(data[7]),
       self.var_email.set(data[8]),
       self.var_phone.set(data[9]),
       self.var_address.set(data[10]),
       self.var_dob.set(data[11]),
       self.var_radio1.set(data[12])

   #=====update function======

   def update_data(self):

      if self.var_dept.get() == "Select Department" or self.var_name.get()=="" or self.var_reg.get()=="":
         messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
         try:
            Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
            if Update>0:
                conn = mysql.connector.connect(host="localhost", username="root", password="654321", database="advance")
                my_cursor = conn.cursor()
                my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,roll=%s,gender=%s,email=%s,phone=%s,address=%s,dob=%s,photo=%s where reg=%s",(

                                                                                                                                                                     self.var_dept.get(),
                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                     self.var_reg.get()
                                                                                                                                                                  ))
            else:
               if not Update:
                   return
            
            messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
            
         except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         

#=====delete function======
   def delete_data(self):
      if self.var_reg.get()=="":
         messagebox.showerror("Error","Reg No must be required",parent=self.root)
      else:
         try:
            delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
            if delete>0:
               conn = mysql.connector.connect(host="localhost", username="root", password="654321", database="advance")
               my_cursor = conn.cursor()
               sql="delete from student where reg=%s"
               val=(self.var_reg.get(),)
               my_cursor.execute(sql,val)
            else:
               if not delete:
                    return

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

         except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

         #==============reset========
   def reset_data(self):
      self.var_dept.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_name.set("")
      self.var_reg.set("")
      self.var_roll.set("")
      self.var_gender.set("Male")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_dob.set("")
      self.var_radio1.set("")


   #============generate data set or take photo sample========
   def generate_dataset(self):
      if self.var_dept.get() == "Select Department" or self.var_name.get()=="" or self.var_reg.get()=="":
         messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
         try:
            
            conn = mysql.connector.connect(host="localhost", username="root", password="654321", database="advance")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
               id+=1
            
            my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,roll=%s,gender=%s,email=%s,phone=%s,address=%s,dob=%s,photo=%s where reg=%s",(

                                                                                                                                                                     self.var_dept.get(),
                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                     self.var_reg.get()==id+1
                                                                                                                                                                  ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()


#=====================Load Pre defined data on facefrontals from opencv=================
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
               gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
               faces=face_classifier.detectMultiScale(gray,1.3,5)
               #scaling factor=1.3
               #Minimum Neighbor=5

               for(x,y,w,h) in faces:
                  face_cropped=img[y:y+h,x:x+w]
                  return face_cropped

            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
               ret,my_frame=cap.read()
               if face_cropped(my_frame) is not None:
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(450,450))
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                  cv2.imshow("Cropped Face",face)

               if cv2.waitKey(1)==13 or int(img_id)==100:
                  break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets completed successfully")
         except Exception as es:
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)











if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()
