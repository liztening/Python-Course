
from cgitb import text
from email import message
from tkinter import *
from tkinter import ttk, messagebox

from setuptools import Command

GUI = Tk()
GUI.title('โปรแกรมคำนวนVAT')
GUI.geometry('500x600')

bg = PhotoImage(file='coin.png')
BG = Label(GUI, image=bg)
BG.pack()

L1 = Label(GUI,text='คำนวนราคาก่อน VAT',font=(None,20))
L1.pack()

total1 = StringVar()
E1 = ttk.Entry(GUI, textvariable=total1, font=(None,20))
E1.pack()

def Cal1():
    try:
        pricebefore = float(total1.get())
        calbefore = (pricebefore*100)/107
        messagebox.showinfo('ราคาก่อน VAT','ราคาก่อน VAT {:.2f}'.format(calbefore))
        total1.set('')
        E1.focus()
    except:
        GUI.title('กรอกผิด')
        messagebox.showwarning('กรอกผิด','กรุณากรอกตัวเลขเท่านั้น')
        total1.set('0')
        E1.focus()

B1 = ttk.Button(GUI, text='คำนวณก่อน VAT',command=Cal1)
B1.pack(ipadx=30,ipady=20,)




L2 = Label(GUI,text='คำนวนราคารวม VAT',font=(None,20))
L2.pack()

total2 = StringVar()
E2 = ttk.Entry(GUI, textvariable=total2, font=(None,20))
E2.pack()

def Cal2():
    try:
        priceafter = float(total2.get())
        calafter = (priceafter*1.07)
        messagebox.showinfo('ราคาก่อน VAT','ราคาหลัง VAT {:.2f}'.format(calafter))
        total2.set('')
        E2.focus()
    except:
        GUI.title('กรอกผิด')
        messagebox.showwarning('กรอกผิด','กรุณากรอกตัวเลขเท่านั้น')
        total2.set('0')
        E2.focus()




B2 = ttk.Button(GUI, text='คำนวณราคารวม VAT',command=Cal2)
B2.pack(ipadx=30,ipady=20)

GUI.mainloop()