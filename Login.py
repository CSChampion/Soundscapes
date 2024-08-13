import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#https://www.geeksforgeeks.org/run-one-python-script-from-another-in-python/
import Temp5
import Temp6
import Temp7

users = {"":["", 1], "A":["B",2]}

def login():
    def validate_login():
        userid = username_entry.get()
        password = password_entry.get()

        # You can add your own validation logic here
        if userid in users.keys():
            if users[userid.strip()][0] == password.strip():
                messagebox.showinfo("Login Successful", "Welcome, User {}!".format(users[userid.strip()][1]))
                parent.destroy()
                y = Temp7.input_return()
                
                if y == 1:
                    Temp5.main_play_note()
                else:
                    x = Temp7.file_return()
                    Temp6.main_play_file(users[userid.strip()][1], x)
                
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


    # Create the main window
    parent = Tk()
    parent.geometry("750x240")
    parent.title("Login Form")
    parent.resizable = (False, False)
    
    #https://www.reddit.com/r/learnpython/comments/sgibdr/tkinter_error_couldnt_recognize_data_in_image/
    #https://www.geeksforgeeks.org/how-to-resize-image-in-python-tkinter/
    #https://www.geeksforgeeks.org/how-to-add-a-border-color-to-a-button-in-tkinter/
    

    bg = ImageTk.PhotoImage(Image.open("T2.png"))
    label1 = Label(parent, image = bg)
    label1.place(x = -1, y = -1)

    # Create and place the username label and entry

    username_label = tk.Label(parent, text="Username", fg = "black", bg = "#ff7683", font=(("Segoe UI"), 11))
    username_label.place(relx = 0.5, y = 30, anchor=CENTER)

    username_entry = tk.Entry(parent, width= 40)
    username_entry.place(relx = 0.5, y = 50, anchor=CENTER)

    # Create and place the password label and entry
    password_label = tk.Label(parent, text="Password", fg = "black", bg = "#ff7683", font=(("Segoe UI"), 11))
    password_label.place(relx = 0.5, y = 85, anchor=CENTER)
    password_entry = tk.Entry(parent, show="*", width= 40)  # Show asterisks for password
    password_entry.place(relx = 0.5, y = 105, anchor=CENTER)

    # Create and place the login button
    login_button = tk.Button(parent, text="Login", command=validate_login, fg = "white", bg = "#046169")
    login_button.place(relx = 0.5, y = 155, anchor=CENTER)

    parent.mainloop()

    #NEED TO ADD PADDING B/W TEXT INPUT BOXES
    
