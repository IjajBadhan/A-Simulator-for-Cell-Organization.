from tkinter import *
from tkinter.ttk import Combobox
import math

window = Tk()


class MyWindow:
    def __init__(self, window):

        # TextLabel
        self.lbl0 = Label(
            window, text="A simulator of cell organization", fg='Red', font=("Arial Bold", 18))
        self.lbl1 = Label(window, text="Total Coverd Area",
                          font=("Arial Bold", 12))
        self.lbl2 = Label(window, text="Radious of Each Cell",
                          font=("Arial Bold", 12))
        self.lbl3 = Label(
            window, text="Frequency Reuse Factor ", font=("Arial Bold", 12))
        self.lbl4 = Label(
            window, text="Total Number of Frequencies", font=("Arial Bold", 12))
        self.lbl5 = Label(window, text="Result:", font=("Arial Bold", 12))
        self.lbl6 = Label(window, text="Cell Size", font=("Arial Bold", 12))

   # TEXT Box/field Entry
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()

   # Button declaration
        self.btn1 = Button(window, text='Number Of Cells')
        self.btn2 = Button(window, text='Channels Per Cell')
        self.btn3 = Button(window, text='Total Channel Capacity')
        self.btn4 = Button(window, text='Concurrent cell')

    # Label Position
        self.lbl0.place(x=230, y=25)
        self.lbl1.place(x=100, y=100)
        self.lbl2.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.lbl4.place(x=100, y=250)
        self.lbl6.place(x=100, y=300)
        self.lbl5.place(x=160, y=405)

        self.t1.place(x=350, y=100, height=28, width=200)
        self.t2.place(x=350, y=150, height=28, width=200)
        self.t3.place(x=350, y=200, height=28, width=200)
        self.t4.place(x=350, y=250, height=28, width=200)
        self.t5.place(x=250, y=400, height=35, width=300)

        self.b1 = Button(window, text='Number Of Cells', fg='Blue', font=("Arial Bold", 12),
                         command=self.NumberOfCells)
        self.b2 = Button(window, text='Channels per Cell', fg='Blue',
                         font=("Arial Bold", 12))
        self.b3 = Button(window, text='Total Channel Capacity', fg='Blue',
                         font=("Arial Bold", 12))
        self.b4 = Button(window, text='Concurrent Cell', fg='Blue',
                         font=("Arial Bold", 12))
        self.b2.bind('<Button-1>', self.ChannelPerCell)
        self.b3.bind('<Button-1>', self.TotalChannelCapacity)
        self.b4.bind('<Button-1>', self.ConcurrentCell)

    # Button Position
        self.b1.place(x=80, y=350)
        self.b2.place(x=230, y=350)
        self.b3.place(x=390, y=350)
        self.b4.place(x=590, y=350)

    # ComboBox
        var = StringVar()
        var.set("one")
        data = ("Macro Cell", "Micro Cell")  # "Pico Cell", "Femto Cell")
        cb = Combobox(window, values=data)
        cb.place(x=220, y=300)

    # Button Action
    def NumberOfCells(self):
        self.t5.delete(0, 'end')
        Total_area = float(self.t1.get())
        radius = float(self.t2.get())
        A1 = (2.6*radius*radius)
        result = (Total_area / A1)
        self.t5.insert(END, int(result))

    def ChannelPerCell(self, event):
        self.t5.delete(0, 'end')
        Total_Channel = int(self.t4.get())
        Frequency_Reuse_Factor = int(self.t3.get())
        result = (Total_Channel / Frequency_Reuse_Factor)
        self.t5.insert(END, int(result))

    def TotalChannelCapacity(self, event):
        self.t5.delete(0, 'end')
        Total_area = float(self.t1.get())
        radius = float(self.t2.get())
        A1 = (2.6*radius*radius)
        result = (Total_area / A1)
        Total_Channel = int(self.t4.get())
        Frequency_Reuse_Factor = int(self.t3.get())
        result1 = (Total_Channel / Frequency_Reuse_Factor)
        channel_capacity = (result*result1)
        self.t5.insert(END, str(channel_capacity))

    def ConcurrentCell(self, event):
        self.t5.delete(0, 'end')
        Total_area = float(self.t1.get())
        radius = float(self.t2.get())
        A1 = (2.6*radius*radius)
        result = (Total_area / A1)
        Total_Channel = int(self.t4.get())
        Frequency_Reuse_Factor = int(self.t3.get())
        result1 = (Total_Channel / Frequency_Reuse_Factor)
        toatl_calls = math.floor(result*result1)
        self.t5.insert(END, str(toatl_calls))


# set window color
window['background'] = 'Maroon'

mywin = MyWindow(window)
window.title('Python GUI')
window.geometry("800x500+10+10")
window.mainloop()
