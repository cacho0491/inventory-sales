from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from controlador import validate_user
from menu import Menu
import hashlib


class Login():
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.config(background="white")
        self.master.geometry("200x108")

        # create a frame container
        frame = LabelFrame(self.master, text="Login", bg="white")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Username & Password entries
        self.username_label = Label(frame, text="Username", bg="white").grid(row=0, column=0)
        self.username_entry = Entry(frame, highlightthickness=0)
        self.username_entry.focus()
        self.username_entry.grid(row=0, column=1)
        self.password_label = Label(frame, text="Password", bg="white").grid(row=1, column=0)
        self.password_entry = Entry(frame, show="*", highlightthickness=0)
        self.password_entry.grid(row=1, column=1)
        # Button
       # ttk.Style().configure("BW.TButton", foreground="red", background="#5C7382", highlighthickness=0)
        btn = Button(frame, text="Login", foreground='white', font=("Times", 10, "bold"), bg="#5C7382", command=self.btn_clicked)
        btn.grid(row=3, columnspan=2, sticky=W + E)

        master.bind('<Return>', lambda event: self.btn_clicked())

    def btn_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        cipher_pass = hashlib.sha3_256(password.encode()).hexdigest()
        user = validate_user(username, cipher_pass)

        if user is not None:
            print("Success")
            root2 = Toplevel(self.master)
            myGui = Menu(root2)
            self.master.withdraw()


        else:
            messagebox.showinfo("Error", "El usuario o contrasena es invalido!")
            print("Retry")


def main():
    master = Tk()
    app = Login(master)
    master.mainloop()
    # mi_app = Login
    # return 0


if __name__ == '__main__':
     main()
