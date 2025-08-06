from tkinter import *

def Login(dict):
    username = UsernameEntry.get()
    password = PasswordEntry.get()
    try:
        if username == dict["Login"]["Username"] and password == dict["Login"]["Password"]:
            print("meow")
            LoginFrame.pack_forget()
            LoginedFrame.pack(fill="both", expand=True)
        else:
            print("woof woof")
    except ValueError:
        print("moo")

def Return():
    LoginedFrame.pack_forget()
    LoginFrame.pack(fill="both", expand=True)

def ViewPasswords():
    print("meow wow")

def AddRemovePasswords():
    print("arf arf")

PasswordDictionary = {
    "Login":{
    "Username":"User",
    "Password":"Pass"}
    }

root = Tk()
root.title("Password Manager")

#login Frame
LoginFrame = Frame(root)
LoginFrame.pack(fill="both", expand=True)
#text at top of login frame
LoginLabel = Label(LoginFrame,text = "Login Form", font = "Arial 20 bold")
LoginLabel.grid(row = 0, column = 0, columnspan = 2)
#enter username text
UsernameLabel = Label(LoginFrame,text = "Enter Username: ", font = "Arial 10")
UsernameLabel.grid(row = 1, column = 0)
#entry to type username into
UsernameEntry = Entry(LoginFrame, justify = CENTER, font = "Arial 15")
UsernameEntry.grid(row = 1, column = 1, sticky = "nsew")
#enter password text
PasswordLabel = Label(LoginFrame,text = "Enter Password: ", font = "Arial 10")
PasswordLabel.grid(row = 2, column = 0)
#entry to type password into
PasswordEntry = Entry(LoginFrame, justify = CENTER, font = "Arial 15", show = "*")
PasswordEntry.grid(row = 2, column = 1, sticky = "nsew")
#button to confirm username and password
LoginButton = Button(LoginFrame, text = "Login", width = 10, height = 2,
                          command = lambda: Login(PasswordDictionary), bg = "grey")
LoginButton.grid(row = 3, column = 0, sticky = "nsew", padx = 5, pady = 5, columnspan = 2)

#Frame which will appear upon successful login
LoginedFrame = Frame(root)
SuccessLabel = Label(LoginedFrame,text = "Main Menu", font = "Arial 20 bold")
SuccessLabel.grid(row = 0, column = 0, columnspan = 2)
#Access password button
AccessButton = Button(LoginedFrame, text = "View Passwords", width = 18, height = 3,
                          command = ViewPasswords)
AccessButton.grid(row = 1, column = 0)
#Add/remove password button
AddRemoveButton = Button(LoginedFrame, text = "Add/Remove Passwords", width = 18, height = 3,
                          command = AddRemovePasswords)
AddRemoveButton.grid(row = 1, column = 1)
#Back to login button
BackButton = Button(LoginedFrame, text = "Back To Login", width = 10, height = 2,
                          command = Return)
BackButton.grid(row = 2, column = 0, columnspan = 2)

root.mainloop()
