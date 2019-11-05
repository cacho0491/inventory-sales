import os
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from controlador import get_date_records
from create_report import create_report


class Reports:

    def __init__(self, master):
        self.master = master
        self.master.title("Reports")
        self.master.geometry("460x600")
        self.master.config(bg="#F3F0F0")

        self.back_btn = Button(master, text="Menu", foreground='white', bg="#5C7382", width="8",
                               command=self.back_btn)  # home button
        self.back_btn.place(x=20, y=5)

        self.start_date = Label(master, text="Desde: ").place(x=20, y=40)
        self.start_date_entry = DateEntry(master, width=12, background='#F3F0F0',
                 foreground='black', borderwidth=2)

        self.start_date_entry.place(x=86, y=40)

        self.end_date = Label(master, text="Hasta: ").place(x=20, y=70)
        self.end_date_entry = DateEntry(master, width=12, background='#F3F0F0',
                           foreground='black', borderwidth=2)

        self.end_date_entry.place(x=86, y=70)

        self.search = Button(master, text="Buscar", foreground='white', bg="#5C7382", width="8", command=self.search_btn).place(x=90, y=95)

        self.print = Button(master, text="Imprimir", foreground='white', bg="#5C7382", width="8", command=self.print_report)
        self.print.place(x=320, y=95)

    def back_btn(self):
        self.master.withdraw()

    def search_btn(self):
        start_date = self.start_date_entry.get_date()
        end_date = self.end_date_entry.get_date()
        registros = get_date_records(start_date, end_date)

        self.tree = ttk.Treeview(self.master, columns=("ID", "nombre", "precio", "cantidad", "total"))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Precio')
        self.tree.heading('#4', text='Cantidad')
        self.tree.heading('#5', text='Total')

        self.tree.column('#1', minwidth=40, width=40, stretch=NO)
        self.tree.column('#2', minwidth=100, width=200, stretch=YES)
        self.tree.column('#3', minwidth=40, width=40, stretch=NO)
        self.tree.column('#4', minwidth=40, width=50, stretch=NO)
        self.tree.column('#5', minwidth=40, width=50, stretch=YES)
        self.tree.place(x=20, y=150)
        self.tree['show'] = 'headings'

        for registro in registros:
            self.tree.insert("", END, values=registro)

    def print_report(self):
        start_date = self.start_date_entry.get_date()
        end_date = self.end_date_entry.get_date()
        create_report(start_date, end_date)


