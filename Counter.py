# from msilib.schema import SelfReg
from msilib.schema import Error
from multiprocessing.dummy import freeze_support
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from datetime import timedelta
import tkinter.font as f
import tkinter as tk
import sqlite3
import datetime
import time as tm
from xml.dom.expatbuilder import theDOMImplementation


class System(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Main window properties:
        self.title('Car Park System')
        self.geometry('810x690')  # WxH
        self.config(background='#051b33')
        self.resizable(width=False, height=False)

        Body(self).grid(row=0, column=0, sticky=W+E)


class Body(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.top_left = Frame(self, bg='red')
        self.top_left.grid(row=0, column=0, padx=20, pady=20, sticky=W + E)

        self.top_right = Frame(self, bg='red')
        self.top_right.grid(row=0, column=1, padx=20, pady=20, sticky=W + E)

        self.top_frame = Frame(self)
        self.top_frame.config(background='#002b3c')
        self.top_frame.grid(row=1, column=0, columnspan=2, sticky='NEWS')
        self.treeview_frame = Frame(self)
        self.treeview_frame.config(background='#002b3c')
        self.treeview_frame.grid(row=2, column=0, columnspan=2, sticky='NEWS')
        self.bottom_frame = Frame(self)
        self.bottom_frame.config(background='#002b3c')
        self.bottom_frame.grid(row=3, column=0, columnspan=2,  sticky='NEWS')

        self.font = f.Font(family='Bahnschrift', size=10, weight='normal')

        self.widget = Label(self.bottom_frame, text='CARPARK')
        self.widget.grid(row=0, column=0)

        # Ticket type:
        self.radiobutton_value = IntVar()
        self.two_wheelers_type = Radiobutton(self.top_left, text='Two-wheeler',
                                             fg='#ecb365',
                                             font=('CenturyGothic', 10, 'bold'),
                                             variable=self.radiobutton_value,
                                             value=2,
                                             command=lambda: self.selectTicket(self.radiobutton_value.get()))
        self.two_wheelers_type.config(bg='#002b3c')
        self.two_wheelers_type.grid(row=0, column=0, padx=20, pady=10)

        self.four_wheelers_type = Radiobutton(self.top_left, text='Four-wheeler',
                                              variable=self.radiobutton_value,
                                              value=4,
                                              command=lambda: self.selectTicket(self.radiobutton_value.get()),
                                              fg='#ecb365',
                                              font=('CenturyGothic', 10, 'bold'))
        self.four_wheelers_type.config(bg='#002b3c')
        self.four_wheelers_type.grid(row=0, column=1, padx=20, pady=10)

        self.ticket = Label(self.top_left, text='16', font='Bahnschrift 20 bold', bg='#002b3c', fg='white')
        self.ticket.grid(row=0, column=2, padx=0, pady=10, sticky=S)

        # Add ticket form:
        options = ['Plate No. :', 'Vehicle Model', 'Color :']
        row = 1
        for i in range(3):
            Label(self.top_left, text=options[i], font=self.font, background='#002b3c', fg='white').grid(row=row, column=0,
                                                                                                      padx=10, pady=8,
                                                                                                      sticky=E)
            row += 1

        self.plate_no_ent = Entry(self.top_left, width=30)
        self.plate_no_ent.grid(row=1, column=1, padx=5, pady=0, sticky='')

        self.vehicle_desc = Entry(self.top_left, width=30)
        self.vehicle_desc.grid(row=2, column=1, padx=5, pady=0, sticky='')

        self.color_ent = Entry(self.top_left, width=30)
        self.color_ent.grid(row=3, column=1, padx=5, pady=0, sticky='')

        self.enter_btn = Button(self.top_left, text='Enter',
                                command=lambda: self.on_clickEnter(),
                                font=self.font,
                                width=10,
                                fg='#023047', bg='#ecb365')
        self.enter_btn.grid(row=3, column=2, padx=30, pady=10, sticky=W)

        # WIDGETS:

        self.spots = Label(self.top_right, text='Spots Left', font='Bahnschrift 15 bold', background='#002b3c', fg='white')
        self.spots.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)

        self.no_spots = Label(self.top_right, text='', font='Bahnschrift 19 bold', background='#002b3c', fg='white')
        self.no_spots.grid(row=0, column=1, padx=10, pady=10, sticky=E)

        self.tw = Label(self.top_right, text='Two-wheeler :', font='CenturyGothic 10 bold', background='#002b3c', fg='white')
        self.tw.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        connect = sqlite3.connect('cps.db')
        c = connect.cursor()
        c.execute("SELECT fw_spots, tw_spots FROM SYSTEM_SETTINGS")
        spots = c.fetchone()
        connect.commit()

        self.no_tw = Label(self.top_right, text=spots[1], font='Bahnschrift 19 bold', background='#002b3c', fg='white')
        self.no_tw.grid(row=1, column=1, padx=10, pady=10, sticky=E)

        self.fw = Label(self.top_right, text='Four-wheeler :', font='CenturyGothic 10 bold', background='#002b3c', fg='white')
        self.fw.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.no_fw = Label(self.top_right, text=spots[0], font='Bahnschrift 19 bold', background='#002b3c', fg='white')
        self.no_fw.grid(row=2, column=1, padx=10, pady=10, sticky=E)

        settings_btn = Button(self.top_right, text='SETTINGS',
                              command=self.manageSettings,
                              font='Bahnschrift 10 bold',
                              width=25,
                              fg='#023047', bg='#ecb365')
        settings_btn.grid(row=3, column=0,columnspan=2, padx=10, pady=10, sticky='NEWS')

        connect.close()

    def manageSettings(self):
        self.update_spots('FOUR')
        global row
        self.settings_clear()
        self.parking_spot_win = Toplevel(self)
        self.parking_spot_win.geometry('300x420')
        self.parking_spot_win.title('System Settings')
        self.parking_spot_win.config(background='#051b33')
        self.parking_spot_win.resizable(width=False, height=False)

        two_wheelers_frame = LabelFrame(self.parking_spot_win, text=' Two-Wheeler ',
                                        font=('Century Gothic', 11, 'bold'), bg='#051b33', fg='white')
        two_wheelers_frame.grid(row=0, column=0, padx=25, pady=20, sticky='NEWS')

        four_wheelers_frame = LabelFrame(self.parking_spot_win, text=' Four-Wheeler ',
                                         font=('Century Gothic', 11, 'bold'), bg='#051b33', fg='white')
        four_wheelers_frame.grid(row=1, column=0, padx=25, pady=10, sticky='NEWS')

        Label(two_wheelers_frame, text='No. of spots :', font=self.font, bg='#051b33', fg='white').grid(row=0, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky=E)
        Label(two_wheelers_frame, text='Base Fee :', font=self.font, bg='#051b33', fg='white').grid(row=1, column=0,
                                                                                                    padx=10,
                                                                                                    pady=10, sticky=E)
        Label(two_wheelers_frame, text='Added Fee/hr :', font=self.font, bg='#051b33', fg='white').grid(row=2, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky=E)
        connect = sqlite3.connect('cps.db')
        c = connect.cursor()
        c.execute(
            "SELECT fw_spots, tw_spots, fw_base_fee, tw_base_fee, fw_added_fee, tw_added_fee FROM SYSTEM_SETTINGS")
        table = c.fetchall()

        data = []

        for row in table:
            data.append(row)

        connect.commit()
        connect.close()

        self.tw_no_of_spots = Entry(two_wheelers_frame, textvariable=self.no_of_spots_tw, width=20)
        self.tw_no_of_spots.insert(0, row[1])
        self.tw_no_of_spots.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.tw_fee = Entry(two_wheelers_frame, textvariable=self.base_fee_tw, width=20)
        self.tw_fee.insert(0, row[3])
        self.tw_fee.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        self.tw_added_fee = Entry(two_wheelers_frame, textvariable=self.added_fee_tw, width=20)
        self.tw_added_fee.insert(0, row[5])
        self.tw_added_fee.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        Label(four_wheelers_frame, text='No. of spots :', font=self.font, bg='#051b33', fg='white').grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=10,
                                                                                                         sticky=E)
        Label(four_wheelers_frame, text='Base Fee :', font=self.font, bg='#051b33', fg='white').grid(row=1, column=0,
                                                                                                     padx=10,
                                                                                                     pady=10, sticky=E)
        Label(four_wheelers_frame, text='Added Fee/hr :', font=self.font, bg='#051b33', fg='white').grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=10,
                                                                                                         sticky=E)

        self.fw_no_of_spots = Entry(four_wheelers_frame, textvariable=self.no_of_spots_fw, width=20)
        self.fw_no_of_spots.insert(0, row[0])
        self.fw_no_of_spots.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.fw_fee = Entry(four_wheelers_frame, textvariable=self.base_fee_fw, width=20)
        self.fw_fee.insert(0, row[2])
        self.fw_fee.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        self.fw_added_fee = Entry(four_wheelers_frame, textvariable=self.added_fee_fw, width=20)
        self.fw_added_fee.insert(0, row[4])
        self.fw_added_fee.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        self.edit_parking_spot = Button(self.parking_spot_win, text='Save',
                                        command=self.save,
                                        font=self.font,
                                        width=10,
                                        fg='#023047', bg='#ecb365')
        self.edit_parking_spot.grid(row=3, column=0, pady=10, sticky='')

        # WIDGETS:

        self.search_ent = Entry(self.top_frame, width=20)
        self.search_ent.grid(row=0, column=0, sticky=W)

        self.search_btn = Button(self.top_frame, text='Search',
                                 command=self.search,
                                 font=self.font,
                                 width=15,
                                 fg='#023047', bg='#ecb365')
        self.search_btn.grid(row=0, column=1, sticky=W)

        self.timeout_btn = Button(self.top_frame, text='Time Out',
                                  command=self.timeOut,
                                  font=self.font,
                                  width=15,
                                  fg='#023047', bg='#ecb365')
        self.timeout_btn.grid(row=0, column=2, sticky=W)

        self.clock = Label(self.top_frame,
                           font=('System', 20),
                           width=15, relief=FLAT,
                           fg='#ecb365', bg='#002b3c')
        self.clock.grid(row=0, column=3, sticky=W)

        # Call clock:
        self.current_time()

        # Call treeview table:
        self.treeviewTable()

        self.reload_ticket_btn = Button(self.bottom_frame, text='Refresh',
                                        command=self.reload,
                                        font=self.font,
                                        width=10,
                                        fg='#023047', bg='#ecb365')
        self.reload_ticket_btn.grid(row=0, column=0, sticky=W)

        self.delete_ticket_btn = Button(self.bottom_frame, text='Delete',
                                        command=self.delete,
                                        font=self.font,
                                        width=10,
                                        fg='#023047', bg='#ecb365')
        self.delete_ticket_btn.grid(row=0, column=1, sticky=W)

    def treeviewTable(self):
        # Scrollbar:
        scrollbar = Scrollbar(self.treeview_frame, orient=VERTICAL)
        scrollbar.grid(row=0, column=1, sticky=N + S)

        # Treeview table declaration:
        self.table = ttk.Treeview(self.treeview_frame)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.grid(row=0, column=0, sticky='NEWS')

        # Treeview style:
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('Treeview',
                        background="white",
                        foreground='#023047',
                        rowheight=25,
                        fieldbackground="white"
                        )
        style.map('Treeview', background=[('selected', '#023047')])

        # Scrollbar config:
        scrollbar.config(command=self.table.yview)

        # Column declaration:
        self.table['columns'] = ('Ticket #', 'Wheels', 'Plate No.', 'Desc', 'Time In', 'Time Out', 'Fee')
        # Column configure:
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('Ticket #', anchor=CENTER, width=70)
        self.table.column('Wheels', anchor=CENTER, width=90)
        self.table.column('Plate No.', anchor=W, width=100)
        self.table.column('Desc', anchor=W, width=120)
        self.table.column('Time In', anchor=CENTER, width=130)
        self.table.column('Time Out', anchor=CENTER, width=130)
        self.table.column('Fee', anchor=E, width=70)
        # Assign headings:
        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('Ticket #', text='Ticket #', anchor=CENTER)
        self.table.heading('Wheels', text='Wheels', anchor=CENTER)
        self.table.heading('Plate No.', text='Plate No.', anchor=CENTER)
        self.table.heading('Desc', text='Desc', anchor=CENTER)
        self.table.heading('Time In', text='Time In', anchor=CENTER)
        self.table.heading('Time Out', text='Time Out', anchor=CENTER)
        self.table.heading('Fee', text='Fee', anchor=CENTER)

        # Get data from db:
        connect = sqlite3.connect('cps.db')
        c = connect.cursor()
        c.execute(
            "SELECT ticket_no, ticket_type, plate_no, color, vehicle_type, datetime_issued, datetime_checkout, total_fee FROM TICKET INNER JOIN VEHICLE on VEHICLE.v_plate_no = TICKET.plate_no LEFT JOIN PAYS on PAYS.p_ticket_no = TICKET.ticket_no ORDER BY ticket_no DESC")
        table = c.fetchall()

        # Commit our query:
        connect.commit()

        # Insert data from db:
        self.id = 0
        for row in table:
            self.table.insert(parent='', index='end', iid=self.id, text='',
                              values=(row[0], row[1], row[2], row[3] + ' ' + row[4], row[5], row[6], row[7]))
            self.id += 1

        connect.close()

if __name__ == '__main__':
    app = System()
    app.mainloop()