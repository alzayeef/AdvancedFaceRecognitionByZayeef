from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      #first image
      img=Image.open(r"project\campus.jpg")
      img=img.resize((600,150),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=600,height=150)

      #second img

      img1=Image.open(r"project\logo.png")
      img1=img1.resize((300,150),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      f_lbl=Label(self.root,image=self.photoimg1)
      f_lbl.place(x=650,y=0,width=300,height=150)

      #third image

      img2=Image.open(r"project\batch.png")
      img2=img2.resize((510,150),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=1000,y=0,width=510,height=150)

      # bg image
      img0 = Image.open(r"project\single.jpg")
      img0 = img0.resize((1530, 710), Image.ANTIALIAS)
      self.photoimg0 = ImageTk.PhotoImage(img0)

      bg_img = Label(self.root, image=self.photoimg0)
      bg_img.place(x=0, y=160, width=1530, height=710)

      #title

      title_lbl=Label(text="RMSTU Face Recognition Attendance System",font=("times new roman",35,"bold"),fg="red")
      title_lbl.place(x=0,y=150,width=1530,height=55)

       #student button

      img3=Image.open(r"project\rag.jpg")
      img3=img3.resize((220,220),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      b1=Button(image=self.photoimg3,command=self.student_details,cursor="hand2")
      b1.place(x=200,y=220,width=200,height=200)

      b1_1=Button(text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",18,"bold"),bg="yellow",fg="blue")
      b1_1.place(x=200,y=385, width=200, height=35)

      # detect face button

      img5 = Image.open(r"project\face_detection.png")
      img5 = img5.resize((220, 220), Image.ANTIALIAS)
      self.photoimg5= ImageTk.PhotoImage(img5)

      b1 = Button(image=self.photoimg5, cursor="hand2",command=self.face_data)
      b1.place(x=500, y=220, width=200, height=200)

      b1_1 = Button(text="Face Detector", cursor="hand2", font=("times new roman", 18, "bold"), bg="yellow",
                    fg="blue",command=self.face_data)
      b1_1.place(x=500, y=385, width=200, height=35)

      #Attendance

      img6= Image.open(r"project\attendance.jpg")
      img6= img6.resize((220, 220), Image.ANTIALIAS)
      self.photoimg6= ImageTk.PhotoImage(img6)

      b1 = Button(image=self.photoimg6, cursor="hand2",command=self.Attendance_data)
      b1.place(x=800, y=220, width=200, height=200)

      b1_1 = Button(text="Attendance", cursor="hand2",command=self.Attendance_data, font=("times new roman", 18, "bold"), bg="yellow",
                    fg="blue")
      b1_1.place(x=800, y=385, width=200, height=35)

      #help desk

      img7 = Image.open(r"project\help_desk.jpg")
      img7 = img7.resize((220,220), Image.ANTIALIAS)
      self.photoimg7 = ImageTk.PhotoImage(img7)

      b1 = Button(image=self.photoimg7, cursor="hand2",command=self.help_data)
      b1.place(x=1100,y=220, width=200, height=200)

      b1_1 = Button(text="Help Desk", command=self.help_data,cursor="hand2", font=("times new roman", 18, "bold"), bg="yellow",
                    fg="blue")
      b1_1.place(x=1100, y=385, width=200, height=35)

       #Train Data
      img8 = Image.open(r"project\train_data.jpg")
      img8 = img8.resize((220,220), Image.ANTIALIAS)
      self.photoimg8 = ImageTk.PhotoImage(img8)

      b1 = Button(image=self.photoimg8, cursor="hand2",command=self.train_data)
      b1.place(x=200, y=450, width=200, height=200)

      b1_1 = Button(text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman", 18, "bold"), bg="yellow",
                    fg="blue")
      b1_1.place(x=200, y=615, width=200, height=35)



       #photos face button
      img9 = Image.open(r"project\photos.jpg")
      img9 = img9.resize((220, 220), Image.ANTIALIAS)
      self.photoimg9 = ImageTk.PhotoImage(img9)

      b1 = Button(image=self.photoimg9, cursor="hand2",command=self.open_img)
      b1.place(x=500, y=450, width=200, height=200)

      b1_1 = Button(text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 18, "bold"), bg="yellow",
                    fg="blue")
      b1_1.place(x=500, y=615, width=200, height=35)


        #Developer
      img10 = Image.open(r"project\developer.jpg")
      img10= img10.resize((220, 220), Image.ANTIALIAS)
      self.photoimg10= ImageTk.PhotoImage(img10)

      b1 = Button(image=self.photoimg10, cursor="hand2")
      b1.place(x=800, y=450, width=200, height=200)

      b1_1 = Button(text="Developer", cursor="hand2",command=self.Developer_data, font=("times new roman", 18, "bold"), bg="yellow",
                    fg="blue")
      b1_1.place(x=800, y=615, width=200, height=35)

         #Exit
      img11= Image.open(r"project\exit.jpg")
      img11 = img11.resize((220, 220), Image.ANTIALIAS)
      self.photoimg11 = ImageTk.PhotoImage(img11)

      b1 = Button(image=self.photoimg11, cursor="hand2",command=self.iExit)
      b1.place(x=1100, y=450, width=200, height=200)

      b1_1 = Button(text="Exit", command=self.iExit,cursor="hand2", font=("times new roman", 18, "bold"), bg="yellow",
                    fg="blue")
      b1_1.place(x=1100, y=615, width=200, height=35)


   def open_img(self):
      os.startfile("data")
   
   def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you Sure exit this project?",parent=self.root)
      if self.iExit >0:
         self.root.destroy()
      else:
         return


      ##__________function button

   def student_details(self):
      self.new_window = Toplevel(self.root)
      self.app = Student(self.new_window)
   
   def train_data(self):
      self.new_window = Toplevel(self.root)
      self.app =Train(self.new_window)
   
   def face_data(self):
      self.new_window = Toplevel(self.root)
      self.app =Face_Recognition(self.new_window)

   def Attendance_data(self):
      self.new_window = Toplevel(self.root)
      self.app=Attendance(self.new_window)
   

   def Developer_data(self):
      self.new_window = Toplevel(self.root)
      self.app=Developer(self.new_window)

   def help_data(self):
      self.new_window = Toplevel(self.root)
      self.app=Help(self.new_window)



if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition_System(root)
        root.mainloop()

