from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == "vikash@gmail.com" and password == "1234":
        # give a message for that we have to import messagebox from tkinter.
        messagebox.showinfo("Shaadi.com","Login Successfully")

    else:
        messagebox.showerror("Error","Login Failed")

root = Tk()

# to give name into the GUI
root.title("Login Form")

# to change the icon of the windows which is known as the favicon.
root.iconbitmap("favicon.ico")

# for control the size of the windows which is max, min, we used the geometry function
root.geometry('500x500')

# for changing the display color.
root.configure(background="pink")

# Now for open the our pnj file we have to import PIL(pillow)
img = Image.open("Shaadi.png")
resized_imag = img.resize((70,70))
img = ImageTk.PhotoImage(resized_imag)

# for print this png file in our window we have to use the label.
img_label = Label(root,image=img)
# we used the pack function for the show and adjust the png file in our gui windows.
img_label.pack(pady=(10,10))


# Now below of the png we would like to write SHAADI.COM for that we used the label.
text_label = Label(root, text="shaadi.com apni milan",fg="black", bg= "pink")
text_label.pack(pady=(10,10))
text_label.config(font=("verdana",24))

# Now we are going to create a login email id for that we also used the login function.
email_label = Label(root, text="Enter Email",fg="black",bg= "pink")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",14))

email_input = Entry(root,width=50)
# we used the ipady for increase the height of the box.
email_input.pack(ipady=6, pady=(1,15))

password_label = Label(root,text="Enter Password",fg="black",bg="pink")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",14))

password_input = Entry(root,width=50)
password_input.pack(ipady=6, pady=(1,50))

# Now i add the button in windows gui
login_button = Button(root,text="Login Here",bg="Pink",fg="black",width=20,height=2,command=handle_login)
login_button.pack(pady=(10,20))
login_button.config(font=("verdana",10))




# mainloop is used to keep the consistensly Gui In screen.
root.mainloop()
