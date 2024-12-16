from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#setting up the main window
root=Tk()
root.title("Denomination Calculator")
root.configure(bg='light blue')
root.geometry("650X500")

#addd image
upload=Image.open("Butterfly.png")

#resize image
uplaod=upload.resize(300,300)
image=ImageTk.PhotoImage(upload)
label=Label(root, image=image, bg='light blue')
label.place(x=180,y=20)


label1=Label(root, text="Welcome to the Denomination Calculator", bg="light blue")

label1.place(relx=0.5,y=340, anchor=CENTER)

#funtion display

def msg():
    MsgBox=messagebox.showinfo("Alert. Would you liek to count...")
    if MsgBox == "ok":
        topwin()

button1=Button(root, text="Let's Get Started!", commad=msg, bg="light brown", fg="purple")
button1.place(x=260, y=360)

#funtion for topwin
def topwin():
    top=Toplevel()
    top.title("Denomination")
    top.configure(bg="grey")
    top.geometry("600X350+50+50")

    label=Label(top, text="Enter Total Amount")
    entry=Entry(top)

    lb1=Label(top, text="Here are the number of notes")
    
    l1=Label(top, text="2000", bg="light grey")
    l2=Label(top, text="500", bg="light grey")
    l3=Label(top, text="100", bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000=amount//2000
            amount%2000
            note500=amount//500
            amount%500
            note100=amount//100
            amount%100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))

        except ValueError:
            messagebox.showerror("Error","Invalid input", "Enter A Valid Number")

    label.place(x=230,y=50)
    entry.place(x=200,y=80)

    button1.place(x=200,y=120)
    lb1.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)

    top.mainloop()

root.mainloop()