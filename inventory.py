from tkinter import *
from tkinter import ttk

import tkinter.messagebox as messagebox
from controlador import *
from menu import Menu


class Inventory():
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory")

        # Option buttons / top frame ###################################################################################
        top_frame = Frame(self.master, width=814, height=54)
        top_frame.grid(row=0, column=0, sticky=E + W + N + S)
        top_frame.config(bg="#F3F0F0")

        self.master.config(background="white")

        self.back_btn = Button(top_frame, text="Menu", foreground='white', bg="#5C7382", width=12, height=1, command=self.back_btn)  # home button
        self.back_btn.place(x=20, y=10)

        self.add_btn = Button(top_frame, text="Agregar", foreground='white', bg="#5C7382", width=12, height=1, command=self.add_btn)  # add item to db button
        self.add_btn.place(x=130, y=10)

        self.update_btn = Button(top_frame, text="Editar", foreground='white', bg="#5C7382", width=12, height=1,
                                 command=self.update_btn)  # edit and update db btn
        self.update_btn.place(x=240, y=10)

        self.delete_btn = Button(top_frame, text="Eliminar", foreground='white', bg="#5C7382", width=12, height=1,
                                 command=self.delete_btn)  # delete from db
        self.delete_btn.place(x=350, y=10)

        self.reloadBtn = Button(top_frame, text="Actualizar", foreground='white', bg="#5C7382", width=12, height=1,
                                 command=self.reload_btn)  # edit and update db btn
        self.reloadBtn.place(x=460, y=10)

        self.search_entry = Entry(top_frame, highlightthickness=0, width=22)  # search product entry box
        self.search_entry.place(x=565, y=13)

        self.search_btn = Button(top_frame, text="Buscar", foreground='white', bg="#5C7382", width=12, height=1, command=self.search_button)  # search item button
        self.search_btn.place(x=710, y=10)

        top_frame.bind('<Return>', lambda event: self.search_button())

        # Data / bottom frame ##########################################################################################

        bottom_frame = LabelFrame(self.master, text="Productos")
        bottom_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky=E + W + N + S)

        bottom_frame.rowconfigure(0, weight=1)
        bottom_frame.columnconfigure(0, weight=1)

        # treeScroll = ttk.Scrollbar(bottom_frame)
        # treeScroll.place(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(bottom_frame, columns=("ID", "nombre", "precio", "cantidad"))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Precio')
        self.tree.heading('#4', text='Cantidad')
        self.tree.column('#3', stretch=YES)
        self.tree.column('#4', stretch=YES)
        self.tree.column('#1', stretch=YES)
        self.tree.column('#2', stretch=YES)
        ysb = ttk.Scrollbar(bottom_frame, orient='vertical', command=self.tree.yview)
        self.tree.grid(row=0, columnspan=4, sticky='nsew')
        ysb.grid(row=0, column=1, sticky='ns')
        self.treeview = self.tree
        self.tree['show'] = 'headings'

        # treeScroll.configure(command=self.tree.yview)
        # self.tree.configure(yscrollcommand=treeScroll.set)

        # Insert data as soon as the inventory window is opened
        Data = get_products()
        for i in Data:
            self.tree.insert("", END, values=(i[0], i[1], i[2], i[3]))

    def add_btn(self):
        self.add_window = Toplevel()
        self.add_window.title("Agregar Producto")
        self.add_window.config(bg="#F3F0F0")
        self.add_window.geometry("300x170")

        self.name = Label(self.add_window, text="Nombre:", width=20, height=2, bg="#F3F0F0").grid(row=1, column=0)
        self.name_entry = Entry(self.add_window, highlightthickness=0)
        self.name_entry.grid(row=1, column=1)

        self.price = Label(self.add_window, text="Precio:", width=20, height=2, bg="#F3F0F0").grid(row=2, column=0)
        self.price_entry = Entry(self.add_window, highlightthickness=0)
        self.price_entry.grid(row=2, column=1)

        self.quantity = Label(self.add_window, text="Cantidad:", width=20, height=2, bg="#F3F0F0").grid(row=3,
                                                                                                            column=0)
        self.quantity_entry = Entry(self.add_window, highlightthickness=0)
        self.quantity_entry.grid(row=3, column=1)

        Button(self.add_window, text="Agregar", foreground='white', bg="#5C7382", width=12, height=1, command=self.add_product_btn).grid(row=4, column=1)

        self.add_window.bind('<Return>', lambda event: self.add_product_btn())


    def add_product_btn(self, *args, **kwargs):

        if self.name == "" or self.price == "" or self.quantity == "":
            messagebox.showinfo("Error", "Por favor inserta la informacion!")
        else:
            name = self.name_entry.get()
            price = self.price_entry.get()
            quantity = self.quantity_entry.get()
            add_product(name, price, quantity)

            messagebox.showinfo("Exito", "El producto se ha guardado exitosamente!")
            self.add_window.destroy()


    def back_btn(self):
        self.master.withdraw()


    def search_button(self):
        self.tree.delete(*self.tree.get_children())

        result = search_products(self.search_entry.get())
        print("resultado consulta")
        print(result)
        if len(result) > 0:
            for row in result:
                self.tree.insert("", END, values=(row[0], row[1], row[2], row[3]))


    def reload_btn(self):
        self.tree.delete(*self.tree.get_children())
        Data = get_products()
        for i in Data:
            self.tree.insert("", END, values=(i[0], i[1], i[2], i[3]))


    # -----------------------------------------Update Window------------------------------------------------------------
    def update_btn(self):
        # self.messagebox.showinfo["text"] = ""
        try:
            self.tree.item(self.tree.selection())["values"][0]
        except IndexError as e:
            messagebox.showinfo("Error", "Por favor selecciona una entrada!")
            return
        id = self.tree.item(self.tree.selection())["values"][0]
        name = self.tree.item(self.tree.selection())["values"][1]
        price = self.tree.item(self.tree.selection())["values"][2]
        quantity = self.tree.item(self.tree.selection())["values"][3]
        self.edit_window = Toplevel()
        self.edit_window.title("Editing")
        self.edit_window.config(bg="#F3F0F0")
        self.edit_window.geometry("200x140")

        id_label = Label(self.edit_window, text="Id :", bg="#F3F0F0").grid(row=0, column=0)
        self.id = Entry(self.edit_window, highlightthickness=0, textvariable=StringVar(self.edit_window, value=id), state="readonly")
        self.id.grid(row=0, column=1)

        name_label = Label(self.edit_window, text="Nombre: ", bg="#F3F0F0").grid(row=1, column=0)
        self.new_name = Entry(self.edit_window, highlightthickness=0, textvariable=StringVar(self.edit_window, value=name))
        self.new_name.grid(row=1, column=1)

        price_label = Label(self.edit_window, text="Precio: ", bg="#F3F0F0").grid(row=2, column=0)
        self.new_price = Entry(self.edit_window, highlightthickness=0, textvariable=StringVar(self.edit_window, value=price))
        self.new_price.grid(row=2, column=1)

        quantity_label = Label(self.edit_window, text="Cantidad: ", bg="#F3F0F0").grid(row=3, column=0)
        self.new_quantity = Entry(self.edit_window,highlightthickness=0, textvariable=StringVar(self.edit_window, value=quantity))
        self.new_quantity.grid(row=3, column=1)

        Button(self.edit_window, text="Guardar Cambios", foreground='white', bg="#5C7382", width=12, height=1, command=self.save_changes_btn).grid(row=4, column=1, sticky=W)

    def save_changes_btn(self, *args, **kwargs):
        result = messagebox.askquestion("Save Changes", "Estas seguro de realizar estos cambios>",
                                                icon="warning")
        if result == "yes":
            id = self.id.get()
            new_name = self.new_name.get()
            new_price = self.new_price.get()
            new_quantity = self.new_quantity.get()
            update_product(id, new_name, new_price, new_quantity)

            messagebox.showinfo("Info", "Informacion actualizada exitosamente!")
            self.edit_window.destroy()

    # ------------------------------------------------------------------------------------------------------------------

    # -----------------------------------------Delete product Window----------------------------------------------------
    def delete_btn(self, *args, **kwargs):
        if not self.tree.selection():
            messagebox.showerror("Error", "Por favor selecciona un producto!")
        else:
            result = messagebox.askquestion("Eliminar", "Estas seguro de eliminar este producto?",
                                                    icon="warning")
            if result == 'yes':
                currentItem = self.tree.focus()
                contents = (self.tree.item(currentItem))
                id = contents['values'][0]
                self.tree.delete(currentItem)
                # Database()
                delete_product(id)
                messagebox.showinfo("Info", "El producto se ha eliminado exitosamente!")
                # self.cursor.close()

