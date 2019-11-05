from doctest import master
from tkinter import *
from tkinter import ttk
from menu import Menu
import tkinter.messagebox as messagebox
from invoice_creator import create_invoice

from controlador import *


class Sales:
    my_cart = []
    id_cliente = 0

    def __init__(self, master):
        self.master = master
        self.master.title("Ventas")
        self.master.geometry("980x650")

        # Left frame / Inventory #######################################################################################

        self.left_frame = Frame(master, width=400, height=768)
        self.left_frame.pack(side=LEFT)
        self.left_frame.config(bg="#F3F0F0")
        style = ttk.Style(self.left_frame)
        style.configure('Treeview', rowheight=40)
        self.left_tree = ttk.Treeview(self.left_frame, columns=("ID", "nombre", "precio"))
        self.left_tree.heading('#1', text='ID')
        self.left_tree.heading('#2', text='Nombre')
        self.left_tree.heading('#3', text='Precio')
        self.left_tree.column('#3', minwidth=0, width=50, stretch=NO)
        self.left_tree.column('#1', minwidth=0, width=40, stretch=NO)
        self.left_tree.column('#2', minwidth=0, width=290, stretch=YES)
        ysb = ttk.Scrollbar(self.left_tree, orient='vertical', command=self.left_tree.yview)
        self.left_tree.place(x=4, y=105)
        ysb.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.left_tree['show'] = 'headings'

        self.home_btn = Button(self.left_frame, text="Menu", foreground='white', bg="#5C7382", width=12, height=1, command=self.back_btn)
        self.home_btn.place(x=4, y=4)

        self.search_entry = Entry(self.left_frame, highlightthickness=0)  # search product entry box
        self.search_entry.place(x=170, y=62)

        self.search_btn = Button(self.left_frame, text="Buscar", foreground='white', bg="#5C7382", width=12, height=1, command=self.search_btn)  # search item button
        self.search_btn.place(x=300, y=60)

        self.reload_btn = Button(self.left_frame, text="Actualizar", foreground='white', bg="#5C7382", width=12, height=1, command=self.reload_btn)
        self.reload_btn.place(x=300, y=4)

        self.add_btn = Button(self.left_frame, text="Agregar al carrito", foreground='white', bg="#5C7382", width=14, height=2, command=self.add_to_cart)
        self.add_btn.place(x=140, y=600)

        Data = get_products()
        for i in Data:
            self.left_tree.insert("", END, values=(i[0], i[1], "%.2f" % i[2]))

        # Right frame / Basket  ########################################################################################

        self.right_frame = Frame(master, width=800, height=768, bg="lightblue")
        self.right_frame.pack(side=RIGHT)
        self.right_frame.config(bg="#E4E4E4")
        title = Label(self.right_frame, text="Basket", bg="#E4E4E4", font=("Times", 30, "bold")).place(x=200, y=10)

        style = ttk.Style(self.right_frame)
        style.configure('Treeview', rowheight=40)
        self.right_tree = ttk.Treeview(self.right_frame, columns=("ID", "nombre", "precio", "cantidad", "total"))
        self.right_tree.heading('#1', text='ID')
        self.right_tree.heading('#2', text='Nombre')
        self.right_tree.heading('#3', text='Precio')
        self.right_tree.heading('#4', text='Cant')
        self.right_tree.heading('#5', text='Total')
        self.right_tree.column('#3', minwidth=0, width=40, stretch=NO)
        self.right_tree.column('#4', minwidth=0, width=40, stretch=NO)
        self.right_tree.column('#1', minwidth=0, width=40, stretch=NO)
        self.right_tree.column('#5', minwidth=0, width=50, stretch=NO)
        self.right_tree.column('#2', width=200, stretch=YES)
        ysb = ttk.Scrollbar(self.right_tree, orient='vertical', command=self.right_tree.yview)
        self.right_tree.place(x=17, y=105)
        ysb.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.right_tree['show'] = 'headings'

        self.delete_item = Button(self.right_frame, text="Eliminar", foreground='white', bg="#5C7382", width=12, height=1, command=self.delete_from_cart)
        self.delete_item.place(x=150, y=70)

        # Total to pay frame  ##########################################################################################
        self.toPay_frame = Frame(self.right_frame)
        self.toPay_frame.place(x=410, y=105)
        self.toPay_frame.config(bg="#F3F0F0")

        self.subtotal = Label(self.toPay_frame, text="Subtotal: ", font=("Times", 20, "bold"), bg="#F3F0F0")
        self.subtotal.grid(row=0, column=0)
        self.sub_total = StringVar()
        self.sub_total.set('0.00')
        self.subtotal_entry = Label(self.toPay_frame, font=("Times", 20, "bold"), textvariable=self.sub_total,
                                    bg="#F3F0F0")
        self.subtotal_entry.grid(row=1, column=0)

        self.iva = Label(self.toPay_frame, text="IVA: ", font=("Times", 20, "bold"), bg="#F3F0F0")
        self.iva.grid(row=2, column=0)
        self.iva_entry = Label(self.toPay_frame, text=" % 12", font=("Times", 20, "bold"), bg="#F3F0F0")
        self.iva_entry.grid(row=3, column=0)

        self.total_to_pay = Label(self.toPay_frame, text="Total: ", font=("Times", 20, "bold"), bg="#F3F0F0")
        self.total_to_pay.grid(row=4, column=0)
        self.total_after_vat = StringVar()
        self.total_after_vat.set("0.00")
        self.total_to_pay_entry = Label(self.toPay_frame, font=("Times", 20, "bold"), textvariable=self.total_after_vat,
                                        bg="#F3F0F0")
        self.total_to_pay_entry.grid(row=5, column=0)

        self.pay_btn = Button(self.toPay_frame, text="Pagar", foreground='white', bg="#5C7382", width=12, height=1, command=self.pay_btn_win)
        self.pay_btn.grid(row=6, column=0)

    # Buttons functions ################################################################################################

    def back_btn(self):  # Back to Menu button
        self.master.withdraw()

    def search_btn(self):  # Search button
        self.left_tree.delete(*self.left_tree.get_children())
        result = search_products(self.search_entry.get())
        if len(result) > 0:
            for row in result:
                self.left_tree.insert("", END, values=(row[0], row[1], row[2], row[3]))

    def reload_btn(self):  # Reload inventory / left tree
        self.reload_left_tree()

    def reload_left_tree(self):
        self.left_tree.delete(*self.left_tree.get_children())
        Data = get_products()
        for i in Data:
            self.left_tree.insert("", END, values=(i[0], i[1], i[2]))

    def add_to_cart(self):

        try:
            self.left_tree.item(self.left_tree.selection())["values"][0]
        except IndexError as e:
            messagebox.showerror("Error", "Por favor selecciona una entrada!")
            return

        # New window to enter the quantity needed ######################################################################

        id = self.left_tree.item(self.left_tree.selection())["values"][0]
        name = self.left_tree.item(self.left_tree.selection())["values"][1]
        price = self.left_tree.item(self.left_tree.selection())["values"][2]


        self.add_to_cart_window = Toplevel()
        self.add_to_cart_window.title("Agregar al carrito")

        Label(self.add_to_cart_window, text="Id :").grid(row=0, column=0)
        self.item_id = Entry(self.add_to_cart_window, textvariable=StringVar(self.add_to_cart_window, value=id),
                         state="readonly")
        self.item_id.grid(row=0, column=1)

        Label(self.add_to_cart_window, text="Nombre: ").grid(row=1, column=0)
        self.name = Entry(self.add_to_cart_window, textvariable=StringVar(self.add_to_cart_window, value=name),
                          state="readonly")
        self.name.grid(row=1, column=1)

        self.price = Label(self.add_to_cart_window, text="Precio: ")
        self.price.grid(row=2, column=0)
        self.price_entry = Entry(self.add_to_cart_window, textvariable=StringVar(self.add_to_cart_window, value=price),
                                 state="readonly")
        self.price_entry.grid(row=2, column=1)

        self.quantity_required = Label(self.add_to_cart_window, text="Cantidad: ")
        self.quantity_required.grid(row=3, column=0)
        self.quantity_required_entry = Entry(self.add_to_cart_window, textvariable=StringVar(self.add_to_cart_window))
        self.quantity_required_entry.grid(row=3, column=1)

        self.add = Button(self.add_to_cart_window, text="Agregar a carrito", foreground='white', bg="#5C7382", width=12, height=1, command=self.add_to_cart_btn)
        self.add.grid(row=4, column=1, sticky=W)

        self.add_to_cart_window.bind('<Return>', lambda event: self.add_to_cart_btn())

    def add_to_cart_btn(self, *args, **kwargs):
        price = self.price_entry.get()
        quantity_required = self.quantity_required_entry.get()
        id = self.item_id.get()
        product = search_product_id(id)  # find information about an specific product
        current_quantity = product[3]  # current stock in the inventory
        unit_price = product[2]  # price
        if quantity_required == "" or quantity_required == "0":
            messagebox.showerror("Error", "La cantidad es necesaria!!")  # quantity is required

        elif int(quantity_required) > current_quantity:
            messagebox.showinfo("Error", "No tenemos productos suficientes!")  # not enough products

        else:
            self.total_before_vat = float(price) * float(quantity_required)
            self.right_tree.insert("", END, values=(
                self.item_id.get(), self.name.get(), price, self.quantity_required_entry.get(),
                "%.2f" % self.total_before_vat))
            self.current_subtotal = float(self.sub_total.get()) + self.total_before_vat
            self.sub_total.set(str("%.2f" % self.current_subtotal))  # subtotal calculation

            self.total_price = self.current_subtotal * 1.12
            self.total_after_vat.set(str("%.2f" % self.total_price))  # total after vat
            item = (id, current_quantity, int(quantity_required), unit_price)
            self.my_cart.append(item)  # append items in the basket to an array
            print(self.my_cart)
            self.add_to_cart_window.destroy()  # after adding to basket, close the window

    def delete_from_cart(self):  # delete an item from baskter
        if not self.right_tree.selection():
            messagebox.showerror("Error", "Por favor selecciona un producto!")  # choose an item
        else:
            result = messagebox.askquestion("Eliminar", "Estas seguro de eliminar este producto?",
                                            icon="warning")   # sure about removing this item?
            if result == 'yes':
                #  self.right_t_id = self.right_tree.item(self.right_tree.selection())["values"][0]
                price = self.right_tree.item(self.right_tree.selection())["values"][4]
                selected_item = self.right_tree.focus()
                # contents = (self.right_tree.item(selected_item))

                update_subtotal = float(self.sub_total.get()) - float(price)
                update_total = float(self.total_after_vat.get()) - float(price) * 1.12
                self.sub_total.set("%.2f" % update_subtotal)
                self.total_after_vat.set("%.2f" % update_total)
                self.right_tree.delete(selected_item)  # delete selected item

    def enable_search_field(self):
        if self.state.get() == 1:
            self.search_client.config(state=NORMAL)
        else:
            self.search_client.config(state=DISABLED)


    def pay_btn_win(self):  # window when pay button is clicked
        item = self.total_after_vat.get()
        if item == "0.00":
            messagebox.showinfo("Error", "Por favor anade algo al carrito!")
        else:
            self.pay_window = Toplevel()
            self.pay_window.title("Pagar")

            self.checkbox = Label(self.pay_window, text="Factura?")
            self.checkbox.grid(row=0, column=0)

            self.state = IntVar()
            self.cbox = Checkbutton(self.pay_window, variable=self.state, command=self.enable_search_field)
            self.cbox.grid(row=0, column=1)

            self.search_client = Entry(self.pay_window)
            self.search_client.grid(row=1, column=0)
            self.search_client.config(state=DISABLED)

            self.search_btn = Button(self.pay_window, text="Buscar", foreground='white', bg="#5C7382", width=12, height=1, command=self.buscar_btn)
            self.search_btn.grid(row=1, column=1)

            self.client_fname = Label(self.pay_window, text="Nombre del cliente: ")
            self.client_fname.grid(row=2, column=0)

            self.fname_entry = Entry(self.pay_window)
            self.fname_entry.grid(row=2, column=1)
            self.fname_entry.config(state=DISABLED)

            self.client_lname = Label(self.pay_window, text="Apellido del cliente: ")
            self.client_lname.grid(row=3, column=0)

            self.lname_entry = Entry(self.pay_window)
            self.lname_entry.grid(row=3, column=1)
            self.lname_entry.config(state=DISABLED)

            self.client_address = Label(self.pay_window, text="Dir. del cliente: ")
            self.client_address.grid(row=4, column=0)

            self.client_address_entry = Entry(self.pay_window)
            self.client_address_entry.grid(row=4, column=1)
            self.client_address_entry.config(state=DISABLED)

            self.client_tnumber = Label(self.pay_window, text="Telefono del cliente: ")
            self.client_tnumber.grid(row=5, column=0)

            self.tnumber_entry = Entry(self.pay_window)
            self.tnumber_entry.grid(row=5, column=1)
            self.tnumber_entry.config(state=DISABLED)

            self.total_label = Label(self.pay_window, text="Total: $")
            self.total_label.grid(row=6, column=0)

            self.total_entry = Label(self.pay_window, textvariable=self.total_after_vat)
            self.total_entry.grid(row=6, column=1)

            # amount given by the client
            self.amount_given = Label(self.pay_window, text="Pagado: $")
            self.amount_given.grid(row=7, column=0)
            self.amount_given_entry = Entry(self.pay_window)
            self.amount_given_entry.grid(row=7, column=1)

            # calculating the change
            self.change = Label(self.pay_window, text="Cambio: $")
            self.change.grid(row=8, column=0)
            self.change_amount = StringVar()
            self.change_amount.set('0')
            self.change_entry = Label(self.pay_window, textvariable=self.change_amount)
            self.change_entry.grid(row=8, column=1)

            self.pay = Button(self.pay_window, text="Pagar", foreground='white', bg="#5C7382", width=12, height=1, command=self.paybtn)
            self.pay.grid(row=9, column=0)



            self.pay_window.bind('<Return>', lambda event: self.paybtn())

    def buscar_btn(self):
        documento = self.search_client.get()
        cliente = search_client(documento)

        self.fname_entry.config(state=NORMAL)
        self.lname_entry.config(state=NORMAL)
        self.client_address_entry.config(state=NORMAL)
        self.tnumber_entry.config(state=NORMAL)

        if cliente is not None:
            self.fname_entry.insert(0, cliente[1])
            self.lname_entry.insert(0, cliente[2])
            self.client_address_entry.insert(0, cliente[5])
            self.tnumber_entry.insert(0, cliente[4])
            self.id_cliente = cliente[0]

        else:
            messagebox.showerror("Error", "No se ha encontrado el cliente, Por favor rellena los datos")
            self.id_cliente = 0


    def paybtn(self, *args, **kwargs):
        amount_given = float(self.amount_given_entry.get())
        total_to_pay = float(self.total_after_vat.get())
        if amount_given < total_to_pay:
            messagebox.showerror("Error", "El valor tiene que ser superior")
        else:
            if self.state.get() == 1:

                if self.id_cliente == 0:
                    if self.fname_entry.get() != "" and self.lname_entry.get() != "" and self.search_client.get() != "":
                        id_client = insert_client(self.fname_entry.get(), self.lname_entry.get(), self.search_client.get(), self.tnumber_entry.get(), self.client_address_entry.get())
                        self.create_invoice(id_client)
                    else:
                        messagebox.showerror("Error", "Debe ingresar los datos del cliente")
                else:
                    self.create_invoice(self.id_cliente)
            else:
                self.create_invoice(None)




    def create_invoice(self, id_client):
        print("client id {0}".format(id_client))
        amount_given = float(self.amount_given_entry.get())
        total_to_pay = float(self.total_after_vat.get())

        invoice_id = insert_invoice(float(self.total_after_vat.get()),
                                    float(self.sub_total.get()),
                                    float(self.current_subtotal) * 0.12, id_client)

        print("factura id {0}".format(invoice_id))
        for product in self.my_cart:
            new_stock = product[1] - product[2]  # new_stock = current_stock - quantity_required
            update_stock(product[0], new_stock)  # update stock
            insert_record(product[2], product[2] * product[3], invoice_id, product[0])
        # insert into transacciones
        self.my_cart = []  # make my_cart empty again
        self.reload_left_tree()
        print("bajoo!")

        self.sub_total.set('0')
        self.total_after_vat.set('0')
        self.right_tree.delete(*self.right_tree.get_children())
        create_invoice(invoice_id)
        self.id_cliente = 0
        change = amount_given - total_to_pay
        self.change_amount.set(str("%.2f" % change))

