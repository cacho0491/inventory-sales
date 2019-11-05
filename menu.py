from tkinter import *
from tkinter import ttk
from inventory import Inventory
from sales import Sales
from reports import Reports
from alerts import Alerts
from settings import Settings
import tkinter.messagebox as messagebox

class Menu():
    def __init__(self, master):
        self.master = master
        self.master.title("Menu")
        self.master.geometry("653x370")
        self.master.config(bg="white")
        self.title = Label(master, text="Menu", bg="white", font=("Times", 37, "bold")).place(x=70, y=10)#grid(row=0, column=0, columnspan=3,pady=20)

        self.inventory = Button(master, text="Inventory", foreground='white', font=("Al Nile", 10, "bold"), bg="#5C7382", width=12, height=5, command=self.inventory_btn).place(x=70, y=83)
            #grid(row=2,
                                                                  #column=0)
        self.sales = Button(master, text="Sales", foreground='white', font=("Al Nile", 10, "bold"), bg="#5C7382", width=12, height=5, command=self.sales_btn).place(x=267, y=83)#grid(row=2, column=1, padx=10, pady=10)
        self.reports = Button(master, text="Reports", foreground='white', font=("Al Nile", 10, "bold"), bg="#5C7382", width=12, height=5, command=self.reports_btn).place(x=464, y=83)#grid(row=2,column=2, padx=10, pady=10)
        self.alerts = Button(master, text="Alerts", foreground='white', font=("Al Nile", 10, "bold"), bg="#5C7382", width=12, height=5, command=self.alerts_btn).place(x=70, y=224)#grid(row=2, column=3)
        self.settings = Button(master, text="Settings", foreground='white', font=("Al Nile", 10, "bold"), bg="#5C7382", width=12, height=5, command=self.settings_btn).place(x=267, y=224)#grid(row=2, column=4)

        self.logout = Button(master, text="Logout", foreground='white', font=("Al Nile", 10, "bold"), bg="#5C7382", command=self.logout_button).place(x=488, y=245) #grid(row=3)

    def inventory_btn(self):
        root2 = Toplevel(self.master)
        myGui = Inventory(root2)

    def sales_btn(self):
        root2 = Toplevel(self.master)
        myGui = Sales(root2)


    def reports_btn(self):
        root2 = Toplevel(self.master)
        myGui = Reports(root2)

    def alerts_btn(self):
        root2 = Toplevel(self.master)
        myGui = Alerts(root2)

    def settings_btn(self):
        root2 = Toplevel(self.master)
        myGui = Settings(root2)

    def main(self):
        master = Tk()
        app = Menu(master)
        master.mainloop()

    def logout_button(self):
        result = messagebox.askquestion('Alert', 'Estas seguro de cerra sesion?')
        if result == 'yes':
            self.master.destroy()
