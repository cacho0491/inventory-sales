import os
from tkinter import *
from tkinter import ttk
from controlador import get_products_quantity


class Alerts:

    def __init__(self, master):
        self.master = master
        self.master.title("Alerts")
        self.master.geometry("680x650")
        self.master.config(bg="#F3F0F0")

        title = Label(master, text="Alerts", bg="#F3F0F0", font=("Times", 37, "bold"))
        title.place(x=270, y=10)

        self.back_btn = Button(master, text="Menu", foreground='white', bg="#5C7382", width="8",
                               command=self.back_btn)  # home button
        self.back_btn.place(x=20, y=10)

        legend = Label(master, text="*Solo se mostraran los productos con menos o igual a 15 unidades*").place(x=160, y=80)

        registros = get_products_quantity()

        style = ttk.Style(self.master)
        style.configure('Treeview', rowheight=40)
        self.tree = ttk.Treeview(master, columns=("ID", "nombre", "precio", "cantidad"))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Precio')
        self.tree.heading('#4', text='Cantidad')

        self.tree.column('#1', minwidth=30, width=40, stretch=NO)
        self.tree.column('#2', minwidth=30, width=180, stretch=YES)
        self.tree.column('#3', minwidth=30, width=60, stretch=NO)
        self.tree.column('#4', minwidth=30, width=60, stretch=NO)
        self.tree.place(x=150, y=150)
        self.tree['show'] = 'headings'

        for registro in registros:
            self.tree.insert("", END, values=registro)

    def back_btn(self):
        self.master.withdraw()