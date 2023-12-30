from tkinter import *
from tkcalendar import *

root = Tk()
root.geometry("600x400")
root.configure(bg="#8000ff")

def pick(event):
    global cal

    master = Toplevel(bg="aqua")
    master.grab_set()
    master.title("Calender Digital")
    master.geometry("350x240+290+270")
    cal = Calendar(master, selecmode="day", date_pattern="mm/dd/yyyy")
    cal.grid(padx=10, pady=10)

    btn = Button(master, text="Submit", bg="#8000ff", fg="white", command=date)
    btn.grid(padx=10, pady=10)
    

def date():
    entry.delete(0, END)
    entry.insert(0, cal.get_date()) 
    
judul1 = Label(root, text="Membuat Jadwal Pada Colom Calendar", bg="#8000ff", fg="white", font=("yu gothiq ui", 20, "bold"))
judul1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=W)

judul2 = Label(root, text="Membuat Acara di Tanggal:", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
judul2.grid(row=1, column=0, padx=10, pady=10, sticky=W)

entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="black", font=("yu gothiq ui", 12))
entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)
entry.insert(0, "Pilih Tanggal")
entry.bind("<1>", pick)

keterangan1 = Label(root, text="Keterangan Acara :", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
keterangan1.grid(row=2, column=0, padx=10, pady=10, sticky=W)

keterangan2 = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="black", font=("yu gothiq ui", 13))
keterangan2.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky=W)
keterangan2.insert(0, "Ketik Keterangan")

keterangan3 = Label(root, text="Kelompok 7 :", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
keterangan3.grid(row=4, column=0, padx=10, pady=10, sticky=W)

keterangan4 = Label(root, text="Muhamad Aldi Perdiyatna", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
keterangan4.grid(row=4, column=1, padx=10, pady=10, sticky=W)

keterangan5 = Label(root, text="Angga nugraha darmawan", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
keterangan5.grid(row=5, column=1, padx=10, pady=10, sticky=W)

keterangan6 = Label(root, text="Azhar Nurul Fikri", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
keterangan6.grid(row=6, column=1, padx=10, pady=10, sticky=W)

keterangan7 = Label(root, text="Ades Qosasih Tamubolon", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
keterangan7.grid(row=7, column=1, padx=10, pady=10, sticky=W)

keterangan4 = Label(root, text="Tema : Project 1 Membuat Aplikasi Calendar Digital", bg="#8000ff", fg="white", font=("yu gothiq ui", 14, "bold"))
keterangan4.grid(row=8, column=0, padx=10, pady=10, sticky=W)


root.mainloop()
