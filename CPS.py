from tkinter import *
from tkinter import PhotoImage


class CarPark:

    def __init__(self, root):
        self.root = root
        self.root.title('Car Park System')
        self.root.geometry('750x500')
        self.root.config(bg='gray17')
        self.root.resizable(False, False)

        self.colors = {'nero': '#252726', 'orange': '#FF8700', 'darkorange': '#FE6101'}

        self.nav_icon = PhotoImage(file="CPS\menu.png")
        self.close_icon = PhotoImage(file="CPS\close.png")

        self.nav_button = Button(self.root, command=self.toggleNav, image=self.nav_icon, border=0,
                                 bg=self.colors['orange'], activebackground=self.colors['orange'])
        self.nav_button.place(x=5, y=10)

    def toggleNav(self):
        self.nav_frame = Frame(self.root,  bg=self.colors['orange'])
        self.nav_frame.place(width=150, height=500)

        self.close_button = Button(self.nav_frame, command=self.closeNav, image=self.close_icon, border=0,
                                   bg=self.colors['orange'], activebackground=self.colors['orange'])
        self.close_button.grid(row=0, column=0, sticky=W)

        # Nav Option Buttons:
        self.home_btn = Button(self.nav_frame, text='Home', font='BahnschriftLight 15', bg=self.colors['orange'], fg='gray17',
                            activebackground=self.colors['orange'], activeforeground='green', bd=0)
        self.home_btn.grid(row=1, column=0, pady=8, padx=40)

        self.ticket_btn = Button(self.nav_frame, text='Tickets', font='BahnschriftLight 15', bg=self.colors['orange'], fg='gray17',
                            activebackground=self.colors['orange'], activeforeground='green', bd=0)
        self.ticket_btn.grid(row=2, column=0, pady=8)

        self.customer_btn = Button(self.nav_frame, text='Customer', font='BahnschriftLight 15', bg=self.colors['orange'], fg='gray17',
                                 activebackground=self.colors['orange'], activeforeground='green', bd=0)
        self.customer_btn.grid(row=3, column=0, pady=8)

        self.car_btn = Button(self.nav_frame, text='Cars', font='BahnschriftLight 15', bg=self.colors['orange'], fg='gray17',
                            activebackground=self.colors['orange'], activeforeground='green', bd=0)
        self.car_btn.grid(row=4, column=0, pady=8)

        self.admin_btn = Button(self.nav_frame, text='Admin', font='BahnschriftLight 15', bg=self.colors['orange'], fg='gray17',
                              activebackground=self.colors['orange'], activeforeground='green', bd=0)
        self.admin_btn.grid(row=5, column=0, pady=8)

    def closeNav(self):
        self.nav_frame.destroy()


    def admin(self):
        self.admin_frame = Frame(self.root)

        admin_lbl = Label(self.admin_frame, text='ID :', font="Bahnschrift 15", bg=self.colors["orange"], fg="gray17", height=2, padx=20)
        admin_lbl.grid(row=0, column=0, sticky=E)

        fname_lbl = Label(self.admin_frame, text='First Name :', font="Bahnschrift 15", bg=self.colors["orange"], fg="gray17", height=2, padx=20)
        fname_lbl.grid(row=1, column=0, sticky=E)

        lname_lbl = Label(self.admin_frame, text='Last Name :', font="Bahnschrift 15", bg=self.colors["orange"], fg="gray17", height=2, padx=20)
        lname_lbl.grid(row=2, column=0, sticky=E)

        contact_lbl = Label(self.admin_frame, text='Contact :', font="Bahnschrift 15", bg=self.colors["orange"], fg="gray17", height=2, padx=20)
        contact_lbl.grid(row=3, column=0, sticky=E)

        self.change_admin_btn = Button(self.admin_frame, text='Change Admin', font='BahnschriftLight 15', bg='gray17', fg=self.colors['orange'],
                              activebackground=self.colors['orange'], activeforeground='green', bd=0)
        self.change_admin_btn.grid(row=5, column=0, pady=8)

root = Tk()
ob = CarPark(root)
root.mainloop()


