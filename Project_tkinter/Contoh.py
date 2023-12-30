from tkinter import *
master = Tk()
# master.config(background="light blue")

judul = Label(text="perhitungan")
judul.grid(row=0, column=0)

teks1 =Label(master, text="masukan nilai 1: ")
teks1.grid(row=1, column=0)

nilai1 = Entry(master,bd=5)
nilai1.grid(row=1, column=1)


teks2 =Label(master, text="masukan nilai 2: ")
teks2.grid(row=2, column=0)

nilai2 = Entry(master,bd=5)
nilai2.grid(row=2, column=1)

teks3 =Label(master, text="hasil: ")
teks3.grid(row=3, column=0)

hasil = Label(master, text="0")
hasil.grid(row=3, column=1)

def tambah():
     hasil.configure(text=(int(nilai1.get()))+(int(nilai2.get())))
     print(hasil.get())
    

btn = Button(master, text="check",command=tambah)
btn.grid(row=4, column=0)


master.mainloop()