import math
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()


class MyWindow:
    def __init__(self, window):

        # TextLabel
        self.lbl0 = Label(window, text="Predicted Path Loss", fg='Red',
                          font=("Arial Bold", 18))
        self.lbl1 = Label(window, text="Carrier Frequency(MHz)",
                          font=("Arial Bold", 14))
        self.lbl2 = Label(window, text="Height to Transmitting Antenna",
                          font=("Arial Bold", 14))
        self.lbl3 = Label(
            window, text="Height to Receiving Antenna", font=("Arial Bold", 14))
        self.lbl4 = Label(
            window, text="Propagation Distance Antennas", font=("Arial Bold", 14))
        self.lbl5 = Label(
            window, text="City Size (Small/mediu - 1, Larger-2)", font=("Arial Bold", 13))
        self.lbl6 = Label(
            window, text="Area Type (Urban-1, Suburban-2, Open-3)", font=("Arial Bold", 13))

   # TEXT Box/field Entry
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()
        self.t6 = Entry()
        self.t7 = Entry()

   # Button declaration
        self.btn1 = Button(window, text='Path Loss(dB):')

    # Label Position
        self.lbl0.place(x=280, y=25)
        self.lbl1.place(x=50, y=100)
        self.lbl2.place(x=50, y=150)
        self.lbl3.place(x=50, y=200)
        self.lbl4.place(x=50, y=250)
        self.lbl5.place(x=50, y=300)
        self.lbl6.place(x=50, y=350)

        self.t1.place(x=420, y=100, height=30, width=200)
        self.t2.place(x=420, y=150, height=30, width=200)
        self.t3.place(x=420, y=200, height=30, width=200)
        self.t4.place(x=420, y=250, height=30, width=200)
        self.t5.place(x=420, y=300, height=30, width=200)
        self.t6.place(x=420, y=350, height=30, width=200)
        self.t7.place(x=420, y=410, height=38, width=300)

        self.b1 = Button(window, text='Path Loss(dB):', command=self.pathloss,
                         fg='Blue', font=("Arial Bold", 14))
        self.b1.place(x=250, y=410)

# function of equation
    def pathloss(self):
        self.t7.delete(0, 'end')
        fc = float(self.t1.get())
        ht = float(self.t2.get())
        hr = float(self.t3.get())
        link_distance = float(self.t4.get())
        city = float(self.t5.get())
        area = float(self.t6.get())

        correction_factor = 0.0

        path_loss = 0.0

        if city == 1:
            correction_factor = (0.8 + ((1.1 * math.log10(fc) - 0.7)
                                        * hr) - (1.56 * math.log10(fc)))

        else:
            if (fc >= 150) and (fc <= 200):
                correction_factor = (
                    8.29 * (math.pow(math.log10(1.54 * hr), 2))) - 1.1
            else:
                correction_factor = (
                    3.2 * (math.pow(math.log10(11.75 * hr), 2))) - 4.97

        path_loss = 69.55 + (26.16 * math.log10(fc)) - (13.82 * math.log10(ht)) - \
            correction_factor + \
            ((44.9 - (6.55 * math.log10(ht)))
             * math.log10(link_distance))

        diff_loss = 0.0
        if area == 2:
            diff_loss = 2 * math.pow(math.log10((fc/28)), 2) + 5.4
        elif area == 3:
            diff_loss = 4.78 * \
                math.pow(math.log10(fc), 2) + 18.733 * \
                math.log10(fc) + 40.94

        path_loss -= diff_loss

        self.t7.insert(END, str(path_loss))


# set window color
window['background'] = 'Maroon'

# window
mywin = MyWindow(window)
window.title('Python GUI')
window.geometry("800x500+10+10")
window.mainloop()
