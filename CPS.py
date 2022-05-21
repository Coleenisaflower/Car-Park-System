from tkinter import *
import tkinter as tk
import sqlite3
#from turtle import color

# Dictionary of colors:
global colors
colors = {'nero': '#252726', 'orange': '#FF8700', 'darkorange': '#FE6101'}

class Body(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Frame setup:
        self.frame = Frame(self)
        self.config(bg='gray17')

        # Header label text:
        self.title = tk.Label(self, text='Car Park System', font='Bahnschrift 15', bg=colors['orange'], fg='gray17', height=2, padx=20)
        self.title.grid(sticky=E+W)
 


class Navbar(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Frame setup:
        self.frame = Frame(self)
        self.config(bg='gray17', width='150', height='500')

        # Nav Option Buttons:
        home_btn = tk.Button(self, text='Home', font='BahnschriftLight 15', bg='gray17', fg=colors['orange'], activebackground='gray17', activeforeground='green', bd=0)
        home_btn.grid(row=0, column=0)

        ticket_btn = tk.Button(self, text='Tickets', font='BahnschriftLight 15', bg='gray17', fg=colors['orange'], activebackground='gray17', activeforeground='green', bd=0)
        ticket_btn.grid(row=1, column=0)

        customer_btn = tk.Button(self, text='Customer', font='BahnschriftLight 15', bg='gray17', fg=colors['orange'], activebackground='gray17', activeforeground='green', bd=0)
        customer_btn.grid(row=2, column=0)

        car_btn = tk.Button(self, text='Cars', font='BahnschriftLight 15', bg='gray17', fg=colors['orange'], activebackground='gray17', activeforeground='green', bd=0)
        car_btn.grid(row=3, column=0)

        admin_btn = tk.Button(self, text='Admin', font='BahnschriftLight 15', bg='gray17', fg=colors['orange'], activebackground='gray17', activeforeground='green', bd=0)
        admin_btn.grid(row=4, column=0)



class CPS(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Main window properties:
        self.title('Car Park System')
        self.geometry('750x500') # WxH
        self.config(bg='gray17')
        #self.resizable(width=False, height=False)

        # Run database:
        #db.Database()

        # Left frame:
        Navbar(self).grid(row=0, column=0, sticky='NSWE')
        Navbar.grid_rowconfigure(self, 0, weight=1)
        Navbar.grid_rowconfigure(self, 0, weight=1)
        Navbar.grid_rowconfigure(self, 0, weight=1)
        Navbar.grid_rowconfigure(self, 0, weight=1)
        Navbar.grid_rowconfigure(self, 0, weight=1)
        # Right frame:
        Body(self).grid(row=0, column=1, sticky='NSWE')
        Body.grid_rowconfigure(self, 0, weight=5)



if __name__ == '__main__':
    app = CPS()
    app.mainloop()