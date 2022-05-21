from tkinter import *
import tkinter as tk
import sqlite3

class Body(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame = Frame(self)

        # dictionary of colors:
        self.color = {'nero': '#252726', 'orange': '#FF8700', 'darkorange': '#FE6101'}

        # loading Navbar icon image:
        nav_icon = PhotoImage(file="CPS\menu.png")
        close_icon = PhotoImage(file="CPS\close.png")

        # top Navigation bar:
        self.top_frame = tk.Frame(self, bg=self.color['orange'])
        self.top_frame.pack(side='top', fill=tk.X)

        # Nav button:
        burger_btn = tk.Button(self.top_frame, image=nav_icon, bg=self.color['orange'], activebackground=self.color["orange"], bd=0, padx=20, command=self.Switch)
        burger_btn.place(x=10, y=10)

        # Header label text:
        self.title = tk.Label(self.top_frame, text='CPS', font='Bahnschrift 15', bg=self.color['orange'], fg='gray17', height=2, padx=20)
        self.title.place(x=30, y=10)

        # setting Nav frame:
        self.nav_frame = tk.Frame(self, bg="gray17", height=1000, width=300)
        self.nav_frame.place(x=-300, y=0)

        # Nav Option Buttons:
        admin_btn = tk.Button(self.nav_frame, text='Admin', font='BahnschriftLight 15', bg='gray17', fg=self.color['orange'], activebackground='gray17', activeforeground='green', bd=0)
        admin_btn.place(x=25, y=80)

        ticket_btn = tk.Button(self.nav_frame, text='Tickets', font='BahnschriftLight 15', bg='gray17', fg=self.color['orange'], activebackground='gray17', activeforeground='green', bd=0)
        ticket_btn.place(x=25, y=120)

        customer_btn = tk.Button(self.nav_frame, text='Customer', font='BahnschriftLight 15', bg='gray17', fg=self.color['orange'], activebackground='gray17', activeforeground='green', bd=0)
        customer_btn.place(x=25, y=160)

        car_btn = tk.Button(self.nav_frame, text='Car', font='BahnschriftLight 15', bg='gray17', fg=self.color['orange'], activebackground='gray17', activeforeground='green', bd=0)
        car_btn.place(x=25, y=200)

        # Nav Close Button:
        close_btn = tk.Button(self.nav_frame, image=close_icon, bg=self.color["orange"], activebackground=self.color["orange"], bd=0, command=self.Switch)
        close_btn.place(x=250, y=10)

    
    # setting switch function:
    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                self.nav_frame.place(x=-x, y=0)
                self.top_frame.update()

            # resetting widget colors:
            self.title.config(bg=self.color["orange"])
            self.top_frame.config(bg=self.color["orange"])
            self.config(bg="gray17")

            # turning button OFF:
            btnState = False
        else:
            # make root dim:
            self.title.config(bg=self.color["nero"])
            self.top_frame.config(bg=self.color["nero"])
            self.config(bg=self.color["nero"])

            # created animated Navbar opening:
            for x in range(-300, 0):
                self.nav_frame.place(x=x, y=0)
                self.top_frame.update()

            # turing button ON:
            btnState = True


class CPS(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #window properties
        self.title('Car Park System')
        self.geometry('750x500') # WxH
        self.config(bg='gray17')
        #self.resizable(width=False, height=False)

        #Run database
        #db.Database()

        #UI
        Body(self).pack(side="top", fill="both", expand=TRUE)



if __name__ == '__main__':
    app = CPS()
    app.mainloop()