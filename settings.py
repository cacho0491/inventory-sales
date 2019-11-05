from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox

from controlador import validate_user, update_password
from menu import Menu
import hashlib

class Settings:
    def __init__(self, master):
        self.master = master
        self.master.title("Settings")
        self.master.config(background="#F3F0F0")
        self.master.geometry("220x180")

        self.update_password = Button(master, text="Update Password",  font=("Al Nile", 10, "bold"),
                                      foreground='white', bg="#5C7382", width=13, height=2, command=self.update_pass_btn).place(x=50, y=50)
    def update_pass_btn(self):
            self.password_window = Toplevel()
            self.password_window.title("Cambiar la contrasena")
            self.password_window.config(bg="#F3F0F0")
            # create a frame container
            frame = LabelFrame(self.password_window, bg="#F3F0F0")
            frame.grid(row=0, column=0, columnspan=3, pady=20)

            # Username & Password entries
            self.current_password = Label(frame, text="Contrasena Actual", bg="#F3F0F0").grid(row=1, column=0)
            self.current_password_entry = Entry(frame, highlightthickness=0)
            self.current_password_entry.focus()
            self.current_password_entry.grid(row=1, column=1)

            self.new_password = Label(frame, text="Nueva Contrasena", bg="#F3F0F0").grid(row=2, column=0)
            self.new_password_entry = Entry(frame, show="*", highlightthickness=0)
            self.new_password_entry.grid(row=2, column=1)

            self.confirm_new_password = Label(frame, text="Confirmar Contrasena", bg="#F3F0F0").grid(row=3, column=0)
            self.confirm_new_password_entry = Entry(frame, show="*", highlightthickness=0)
            self.confirm_new_password_entry.grid(row=3, column=1)
            # Button

            btn = Button(frame, text="Guardar", foreground='white', bg="#5C7382", width=12, height=1, command=self.save)
            btn.grid(row=4, columnspan=2, sticky=W + E)

    def save(self):
        currentPassword = self.current_password_entry.get()
        cipher_current = hashlib.sha3_256(currentPassword.encode()).hexdigest()

        user = validate_user("Admin", cipher_current)

        if user is not None:
            newPassword = self.new_password_entry.get()
            confirmPassword = self.confirm_new_password_entry.get()

            if newPassword == confirmPassword:
                cipher_pass = hashlib.sha3_256(newPassword.encode()).hexdigest()
                print(cipher_pass)
                update_password(cipher_pass)
                messagebox.showinfo("Info", "La Contrasena se a actualizado correctamente!")
            else:
                messagebox.showinfo("Error", "La contrasena no coincide")
        else:
            messagebox.showinfo("Error", "La Clave actual es incorrecta!")

