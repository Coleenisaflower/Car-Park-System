from msilib.schema import SelfReg
from tkinter import *
from tkinter import ttk
import tkinter.font as f
import tkinter as tk
import csv



class Ticket(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configuration:
        self.font = f.Font(family='Bahnschrift', size=10, weight='normal')
        self.frame = Frame(self)
        self.frame.grid(row=0, padx=20, pady=10, sticky='NEWS')
        type_labelframe = LabelFrame(self.frame)
        type_labelframe.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='')

        ticket_type = IntVar()
        self.two_wheelers_type = Radiobutton(type_labelframe, text='Two-wheeler', variable=ticket_type, value=2, command=NONE)
        self.two_wheelers_type.grid(row=0, column=0, padx=20, pady=10)

        self.four_wheelers_type = Radiobutton(type_labelframe, text='Four-wheeler', variable=ticket_type, value=4, command=NONE)
        self.four_wheelers_type.grid(row=0, column=1, padx=20, pady=10)
        
        Label(self.frame, text='#0001', font='Bahnschrift 13 bold').grid(row=0, column=2, padx=30, pady=10, sticky=E)

        # Add attendant form:
        options = ['Plate No. :', 'Vehicle Type :', 'Color :']
        row = 1
        for i in range(3):
            Label(self.frame, text=options[i], font=self.font).grid(row=row, column=0, padx=10, pady=5, sticky=E)
            row += 1

        plate_no_ent = Entry(self.frame, width=30)
        plate_no_ent.grid(row=1, column=1, padx=5, pady=5, sticky='')

        car_type_ent = Entry(self.frame, width=30)
        car_type_ent.grid(row=2, column=1, padx=5, pady=5, sticky='')

        color_ent = Entry(self.frame, width=30)
        color_ent.grid(row=3, column=1, padx=5, pady=5, sticky='')

        self.enter_btn = Button(self.frame, text='Enter',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.enter_btn.grid(row=4, column=2, padx=30, pady=10, sticky=E)



class Counter(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuration:
        self.font = f.Font(family='Bahnschrift', size=10, weight='normal')

        Label(self, text='Spots Left', font='Bahnschrift 15 bold').grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)

        Label(self, text='Two-wheelers :', font='Bahnschrift 10').grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Label(self, text='23', font='Bahnschrift 19 bold').grid(row=1, column=1, padx=10, pady=10, sticky=E)

        Label(self, text='Four-wheelers :', font='Bahnschrift 10').grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Label(self, text='79', font='Bahnschrift 19 bold').grid(row=2, column=1, padx=10, pady=10, sticky=E)

        settings_btn = Button(self, text='SETTINGS',
                command=self.manageSettings,
                font='Bahnschrift 10 bold',
                width=25,
                fg = '#023047', bg='#98C1D9')
        settings_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='NEWS')

    
    def manageSettings(self):
        self.parking_spot_win = Toplevel(self)
        self.parking_spot_win.geometry('300x340')
        self.parking_spot_win.title('System Settings')
        self.parking_spot_win.config(background='#8ECAE6')
        self.parking_spot_win.resizable(width=False, height=False)

        two_wheelers_frame = LabelFrame(self.parking_spot_win, text=' Two-Wheeler ', bg='#8ECAE6')
        two_wheelers_frame.grid(row=0, column=0, padx=25, pady=20, sticky='NEWS')

        four_wheelers_frame = LabelFrame(self.parking_spot_win, text=' Four-Wheeler ', bg='#8ECAE6')
        four_wheelers_frame.grid(row=1, column=0, padx=25, pady=10, sticky='NEWS')

        Label(two_wheelers_frame, text='No. of spots :', font=self.font, bg='#8ECAE6').grid(row=0, column=0, padx=10, pady=10, sticky=E)
        Label(two_wheelers_frame, text='Base Fee :', font=self.font, bg='#8ECAE6').grid(row=1, column=0, padx=10, pady=10, sticky=E)

        self.tw_no_of_spots = Entry(two_wheelers_frame, width=20)
        self.tw_no_of_spots.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.tw_fee = Entry(two_wheelers_frame, width=20)
        self.tw_fee.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        Label(four_wheelers_frame, text='No. of spots :', font=self.font, bg='#8ECAE6').grid(row=0, column=0, padx=10, pady=10, sticky=E)
        Label(four_wheelers_frame, text='Base Fee :', font=self.font, bg='#8ECAE6').grid(row=1, column=0, padx=10, pady=10, sticky=E)

        self.fw_no_of_spots = Entry(four_wheelers_frame, width=20)
        self.fw_no_of_spots.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.fw_fee = Entry(four_wheelers_frame, width=20)
        self.fw_fee.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        self.edit_parking_spot = Button(self.parking_spot_win, text='Save',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.edit_parking_spot.grid(row=3, column=0, pady=10, sticky='')
        # add "You are abt to change parking spot information. Confirm edit" on save button



class View(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        Frame.__init__(self, *args, **kwargs)

        # Configuration:
        self.font = f.Font(family='Bahnschrift', size=10, weight='normal')
        top_frame = Frame(self)
        top_frame.grid(row=1, padx=20, pady=20, sticky='NEWS')
        self.treeview_frame = Frame(self)
        self.treeview_frame.grid(row=2, padx=20, sticky='NEWS')
        bottom_frame = Frame(self)
        bottom_frame.grid(row=3, padx=20, pady=20, sticky='NEWS')

        # Widgets:
        search_ent = Entry(top_frame, width=20)
        search_ent.grid(row=0, column=0, sticky=W)

        self.search_btn = Button(top_frame, text='Search',
                command=NONE,
                font=self.font,
                width=15,
                fg = '#023047', bg='#98C1D9')
        self.search_btn.grid(row=0, column=1, sticky=W)

        self.timeout_btn = Button(top_frame, text='Time Out',
                command=NONE,
                font=self.font,
                width=15,
                fg = '#023047', bg='#98C1D9')
        self.timeout_btn.grid(row=0, column=2, sticky=W)

        # Call treeview table:
        self.treeviewTable()

        self.reload_ticket_btn = Button(bottom_frame, text='Refresh',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.reload_ticket_btn.grid(row=0, column=0, sticky=W)

        self.delete_ticket_btn = Button(bottom_frame, text='Delete',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.delete_ticket_btn.grid(row=0, column=1, sticky=W)
    

    def treeviewTable(self):
        # Scrollbar:
        scrollbar = Scrollbar(self.treeview_frame, orient=VERTICAL)
        scrollbar.grid(row=0, column=1, sticky=N+S)

        # Treeview table declaration:
        self.table = ttk.Treeview(self.treeview_frame)
        #self.table.bind('<Double-1>', self.selectStudent)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.grid(row=0, column=0, sticky='NEWS')

        # Treeview style:
        style = ttk.Style()
        style.configure('Treeview',
            foreground='#023047',
            rowheight=25,
            )
        style.map('Treeview', background=[('selected', '#023047')])

        # Scrollbar config:
        scrollbar.config(command=self.table.yview)

        # Open CSV file:
        path = 'cps.csv'
        file = open(path, newline='')
        reader = csv.reader(file)

        count = 0
        self.id = 0
        for row in reader:

            if count == 0:    # to create the headings:
                # Load column headings:
                self.table['columns'] = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                # Column configure:
                self.table.column('#0', width=0, stretch=NO)
                i = 0
                while i <= 6:
                    if i == 2 or i == 3:    # anchor PLATE NO to west
                        self.table.column(row[i], anchor=W, width=120)
                        i += 1
                    else:
                        self.table.column(row[i], anchor=CENTER, width=90)
                        i += 1
                # Headings:
                self.table.heading('#0', text='', anchor=CENTER) 
                j = 0
                while j <= 6:
                    self.table.heading(row[j], text=row[j], anchor=CENTER)
                    j += 1
            
                count += 1
            else:           # CPS data:
                self.table.insert(parent='', index='end', iid=self.id, text='',
                values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                self.id += 1
        
        file.close()



class Menu(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuration:
        self.font = f.Font(family='Bahnschrift', size=10, weight='normal')
        self.config(background='gray17')

        self.spot_menu = Button(self, text='Settings',
                command=NONE,
                font=self.font,
                width=15,
                fg = '#023047', bg='#98C1D9')
        self.spot_menu.grid(row=0, pady=5, sticky=S)

        self.worker_menu = Button(self, text='Attendants',
                command=self.manageAttendants,
                font=self.font,
                width=15,
                fg = '#023047', bg='#98C1D9')
        self.worker_menu.grid(row=1, pady=5, sticky=S)

        self.change_menu = Button(self, text='Change Attendant',
                command=self.manageChangeAttendant,
                font=self.font,
                width=15,
                fg = '#023047', bg='#98C1D9')
        self.change_menu.grid(row=2, pady=5, sticky=S)


    def manageAttendants(self):
        self.attendants_win = Toplevel(self)
        self.attendants_win.geometry('800x400')
        self.attendants_win.title('Attendants')
        self.attendants_win.config(background='#8ECAE6')
        self.attendants_win.resizable(width=False, height=False)

        top_frame = Frame(self.attendants_win)
        top_frame.grid(row=0, column=0, padx=20, sticky='NEWS')
        treeview_frame = Frame(self.attendants_win)
        treeview_frame.grid(row=1, column=0, padx=20, sticky='NEWS')
        bottom_frame = Frame(self.attendants_win)
        bottom_frame.grid(row=2, column=0, padx=20, sticky='NEWS')
        right_frame = Frame(self.attendants_win)
        right_frame.grid(row=0, rowspan=3, column=1, sticky='NEWS')
        
        # class Font:
        self.font = f.Font(family='Bahnschrift', size=10, weight='normal')

        self.attendant_search_ent = Entry(top_frame, width=20)
        self.attendant_search_ent.grid(row=0, column=0, sticky=W)

        self.search_btn = Button(top_frame, text='Search by name',
                command=NONE,
                font=self.font,
                width=15,
                fg = '#023047', bg='#98C1D9')
        self.search_btn.grid(row=0, column=1, sticky=W)

        self.edit_attendant_btn = Button(top_frame, text='Edit',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.edit_attendant_btn.grid(row=0, column=2, sticky=W)

#  -----TREEVIEW ---------------------------------------------------------------------  #
        # Scrollbar:
        scrollbar = Scrollbar(treeview_frame, orient=VERTICAL)
        scrollbar.grid(row=0, column=1, pady=10, sticky=N+S)

        # Treeview table declaration:
        self.table = ttk.Treeview(treeview_frame)
        #self.table.bind('<Double-1>', self.selectStudent)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.grid(row=0, column=0, pady=10, sticky='NEWS')

        # Treeview style:
        style = ttk.Style()
        style.configure('Treeview',
            foreground='#023047',
            rowheight=25,
            )
        style.map('Treeview', background=[('selected', '#023047')])

        # Scrollbar config:
        scrollbar.config(command=self.table.yview)
      
#----------------------------------------------------------------------------#
#       REPLACE THIS PART WITH QUERIES TO FETCH ATTENDANTS' DATA
        path = 'cps.csv'
        file = open(path, newline='')
        reader = csv.reader(file)

        count = 0
        self.id = 0
        for row in reader:

            if count == 0:    # to create the headings:
                # Load column headings:
                self.table['columns'] = (row[0], row[1], row[2], row[3])
                # Column configure:
                self.table.column('#0', width=0, stretch=NO)
                i = 0
                while i <= 3:
                    if i == 1 or i == 2:    # anchor NAMEs to west
                        self.table.column(row[i], anchor=W, width=120)
                        i += 1
                    else:
                        self.table.column(row[i], anchor=CENTER, width=90)
                        i += 1
                # Headings:
                self.table.heading('#0', text='', anchor=CENTER) 
                j = 0
                while j <= 3:
                    self.table.heading(row[j], text=row[j], anchor=CENTER)
                    j += 1
            
                count += 1
            else:           # Attendants' data:
                self.table.insert(parent='', index='end', iid=self.id, text='',
                values=(row[0], row[1], row[2], row[3]))
                self.id += 1
    
        file.close()
#-------END OF TREEVIEW---------------------------------------------------------------------#

        self.reload_attendant_btn = Button(bottom_frame, text='Refresh',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.reload_attendant_btn.grid(row=0, column=0, sticky=W)

        self.delete_attendant_btn = Button(bottom_frame, text='Delete',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.delete_attendant_btn.grid(row=0, column=1, sticky=W)

#-------START OF RIGHT FRAME---------------------------------------------------------------------#

        Label(right_frame, text='Add Attendant', font='Bahnschrift 15').grid(row=0, columnspan=2, padx=5, pady=10, sticky=W)

        # Add attendant form:
        options = ['Company ID :', 'First Name :', 'Last Name :', 'Contact :']
        row = 1
        for i in range(4):
            Label(right_frame, text=options[i], font=self.font).grid(row=row, column=0, padx=5, pady=5, sticky=E)
            row += 1

        self.attendant_id = Entry(right_frame, width=30)
        self.attendant_id.grid(row=1, column=1, padx=5, pady=5)

        self.attendant_fname = Entry(right_frame, width=30)
        self.attendant_fname.grid(row=2, column=1, padx=5, pady=5)

        self.attendant_lname = Entry(right_frame, width=30)
        self.attendant_lname.grid(row=3, column=1, padx=5, pady=5)

        self.attendant_contact = Entry(right_frame, width=30)
        self.attendant_contact.grid(row=4, column=1, padx=5, pady=5)

        self.add_attendant_btn = Button(right_frame, text='Add',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.add_attendant_btn.grid(row=5, column=1, sticky=E)


    def manageChangeAttendant(self):
        self.change_win = Toplevel(self)
        self.change_win.geometry('300x150')
        self.change_win.title('Change Attendant')
        self.change_win.config(background='#8ECAE6')
        self.change_win.resizable(width=False, height=False)

        # Configuration:
        self.font = f.Font(family='Bahnschrift', size=10, weight='normal')
        self.config(background='gray17')

        Label(self.change_win, text='Select :', font=self.font).grid(row=0, column=0, padx=20, pady=20, sticky=E)

        # Connect to db:
        '''
        connect = sqlite3.connect('ssis_db2.sql')
        c = connect.cursor()
        #Get all course available
        c.execute("SELECT course_CODE FROM course")
        self.codes = [code for code, in c] #list of course code/s
        connect.commit()
        '''
        self.course_drop = ttk.Combobox(self.change_win, values=['Attendant 1', 'Attendant 2', 'Attendant 3'], state='readonly')
        self.course_drop.grid(row=0, column=1, pady=20)
        #connect.close()

        self.replace_attendant_btn = Button(self.change_win, text='Ok',
                command=NONE,
                font=self.font,
                width=10,
                fg = '#023047', bg='#98C1D9')
        self.replace_attendant_btn.grid(row=1, column=1, pady=10, sticky=E)

        




class System(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Main window properties:
        self.title('Car Park System')
        self.geometry('800x730') # WxH
        self.config(background='gray17')
        self.resizable(width=False, height=False)

        # Frames:
        Ticket(self).grid(row=0, column=0, padx=20, pady=30, sticky=W+E)
        Counter(self).grid(row=0, column=1, padx=20, pady=30, sticky=W+E)
        View(self).grid(row=1, column=0, columnspan=2, padx=20, sticky=W+E)
        #Menu(self).grid(row=1, column=1, padx=20, sticky=S)



if __name__ == '__main__':
    app = System()
    app.mainloop()