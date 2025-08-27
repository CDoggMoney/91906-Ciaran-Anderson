from tkinter import *
from tkinter import ttk
import json

def Login(dict):
    username = UsernameEntry.get()
    password = PasswordEntry.get()
    try:
        if username == dict["Login"]["Username"] and password == dict["Login"]["Password"]:
            LoginFrame.pack_forget()
            LoginedFrame.pack(fill="both", expand=True)
        else:
            LoginFrame.pack_forget()
            UnloginedFrame.pack(fill="both", expand=True)
    except ValueError:
        print("moo")

def ReturnLogin():
    LoginedFrame.pack_forget()
    UnloginedFrame.pack_forget()
    LoginFrame.pack(fill="both", expand=True)

def Return():
    ViewFrame.pack_forget()
    MenuFrame.pack_forget()
    LoginedFrame.pack(fill="both", expand=True)

def ReturnToView():
    ViewPassFrame.pack_forget()
    ViewFrame.pack(fill="both", expand=True)    

def ViewPasswordSwitch():
    Choice = ViewChosen.get()
    if Choice:
        ViewFrame.pack_forget()
        ViewPassFrame.pack(fill="both", expand=True)
        ViewPassLabel.config(text=f"Username and Password for {Choice}")
        ViewUser.config(text = f"Username/Email: {data[Choice]['Email']}")
        ViewPass.config(text = f"Password: {data[Choice]['Password']}")
    else:
        ElseLabel = Label(ViewFrame, font = "Arial 8", 
                          text = "You need to select something for the select button to work.")
        ElseLabel.grid(row = 4, column = 0)

def ConfirmPassword():
    Username = AddUsernameEntry.get()
    Password = AddPasswordEntry.get()
    Account  = AddAccountEntry.get()
    if not Account:
        return
    data[Account] = {"Email": Username, "Password": Password}
    refresh_dropdowns()

def ConfirmRemoval():
    Choice = RemoveChosen.get()
    if Choice:
        data.pop(Choice, None)
        refresh_dropdowns()
        IfLabel = Label(RemovePassFrame, font = "Arial 8", 
                        text = "Account Information Deleted Successfully")
        IfLabel.grid(row = 5, column = 0)
    else:
        ElseLabel = Label(RemovePassFrame, font = "Arial 8", 
                          text = "You need to select something for the confirm button to work.")
        ElseLabel.grid(row = 4, column = 0)

def ViewPasswords():
    refresh_dropdowns()
    LoginedFrame.pack_forget()
    ViewFrame.pack(fill="both", expand=True)

def AddRemovePasswords():
    LoginedFrame.pack_forget()
    MenuFrame.pack(fill="both", expand=True)

def AddPassword():
    MenuFrame.pack_forget()
    AddPassFrame.pack(fill="both", expand=True)

def RemovePassword():
    refresh_dropdowns()
    MenuFrame.pack_forget()
    RemovePassFrame.pack(fill="both", expand=True)

def ReturnToMenu():
    AddPassFrame.pack_forget()
    RemovePassFrame.pack_forget()
    MenuFrame.pack(fill="both", expand=True)

def refresh_dropdowns():
    ViewOptions['values'] = list(data.keys())
    RemoveOptions['values'] = list(data.keys())
    ViewChosen.set("")
    RemoveChosen.set("")

#Dictionary for login component
PasswordDictionary = {
    "Login":{
    "Username":"User",
    "Password":"Pass"}
    }

#Sets up root and name of program
root = Tk()
root.title("Password Manager")

#Opens the json file containing the saved passwords and usernames for use
with open("Passwords.json") as f:
    data = json.load(f)

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

#Frame which appears on unsuccessful login
UnloginedFrame = Frame(root)
UnsuccessLabel = Label(UnloginedFrame,text = "Incorrect Username and/or Password", font = "Arial 20 bold")
UnsuccessLabel.grid(row = 0, column = 0, columnspan = 2)
UnbackButton = Button(UnloginedFrame, text = "Try Again", width = 10, height = 2,
                          command = ReturnLogin)
UnbackButton.grid(row = 2, column = 0, columnspan = 2)

#Frame which will appear upon successful login
LoginedFrame = Frame(root)
MenuLabel = Label(LoginedFrame,text = "Main Menu", font = "Arial 20 bold")
MenuLabel.grid(row = 0, column = 0, columnspan = 2)
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
                          command = ReturnLogin)
BackButton.grid(row = 2, column = 0, columnspan = 2)

#Frame which appears when view password button is pressed
ViewFrame = Frame(root)
ViewLabel = Label(ViewFrame ,text = "Passwords", font = "Arial 20 bold")
ViewLabel.grid(row = 0, column = 0)

#Replaced the previous drop down box with a cmbobox as it works better
ViewChosen = StringVar()
ViewOptions = ttk.Combobox(ViewFrame, textvariable=ViewChosen, state="readonly")
ViewOptions['values'] = list(data.keys())
ViewOptions.grid(row = 1, column = 0)
#Button for confirming the selected account
ViewSelectButton = Button(ViewFrame, text = "Select", width = 10, height = 2,
                          command = ViewPasswordSwitch)
ViewSelectButton.grid(row = 2, column = 0)
#Back button
ViewBackButton = Button(ViewFrame, text = "Back", width = 10, height = 2,
                          command = Return)
ViewBackButton.grid(row = 3, column = 0)

#Frame which appears to show selected password and username
ViewPassFrame = Frame(root)
ViewPassLabel = Label(ViewPassFrame, font = "Arial 20 bold")
ViewPassLabel.grid(row = 0, column = 0)
#Label setup for the username/email
ViewUser = Label(ViewPassFrame, font = "Arial 15")
ViewUser.grid(row = 1, column = 0)
#Label setup for the password
ViewPass = Label(ViewPassFrame, font = "Arial 15")
ViewPass.grid(row = 2, column = 0)
#Back Button
ViewPassBackButton = Button(ViewPassFrame, text = "Back", width = 10, height = 2,
                          command = ReturnToView)
ViewPassBackButton.grid(row = 3, column = 0)

#Menu frame which appears when Add/Remove Passwords is selected on the menu
MenuFrame = Frame(root)
MenuLabel = Label(MenuFrame, text = "Menu Menu", font = "Arial 20 bold")
MenuLabel.grid(row = 0, column = 0, columnspan = 2)
#Button to add passwords
AddPasswordButton = Button(MenuFrame, text = "Add Password", width = 18, height = 3,
                           command = AddPassword)
AddPasswordButton.grid(row = 1, column = 0)
#Button to remove passwords
RemovePasswordButton = Button(MenuFrame, text = "Remove Password", width = 18, height = 3,
                           command = RemovePassword)
RemovePasswordButton.grid(row = 1, column = 1)
#Back button
MenuBackButton = Button(MenuFrame, text = "Back", width = 10, height = 2,
                          command = Return)
MenuBackButton.grid(row = 2, column = 0, columnspan = 2)

#Frame which appears when add password is selected
AddPassFrame = Frame(root)
AddPassLabel = Label(AddPassFrame, text = "Add Password", font = "Arial 20 bold")
AddPassLabel.grid(row = 0, column = 0, columnspan = 2)
#Account name entry
AddAccountLabel = Label(AddPassFrame, text = "What is this account for: ", font = "Arial 10")
AddAccountLabel.grid(row = 1, column = 0)
AddAccountEntry = Entry(AddPassFrame, justify = CENTER, font = "Arial 15")
AddAccountEntry.grid(row = 1, column = 1, sticky = "nsew")
#Label and Entry for Username or email
AddUsernameLabel = Label(AddPassFrame, text = "Email/Username: ", font = "Arial 10")
AddUsernameLabel.grid(row = 2, column = 0)
AddUsernameEntry = Entry(AddPassFrame, justify = CENTER, font = "Arial 15")
AddUsernameEntry.grid(row = 2, column = 1, sticky = "nsew")
#Label and Entry for Password
AddPasswordLabel = Label(AddPassFrame, text = "Password: ", font = "Arial 10")
AddPasswordLabel.grid(row = 3, column = 0)
AddPasswordEntry = Entry(AddPassFrame, justify = CENTER, font = "Arial 15")
AddPasswordEntry.grid(row = 3, column = 1, sticky = "nsew")
#Button to confirm username and password entry
ConfirmPasswordButton = Button(AddPassFrame, text = "Confirm selections", width = 15, height = 2,
                               command = ConfirmPassword)
ConfirmPasswordButton.grid(row = 4, column = 0, columnspan = 2)
#Back Button
AddBackButton = Button(AddPassFrame, text = "Go Back", width = 15, height = 2,
                               command = ReturnToMenu)
AddBackButton.grid(row = 5, column = 0, columnspan = 2)

#Frame which appears when remove password is selected
RemovePassFrame = Frame(root)
RemovePassLabel = Label(RemovePassFrame, text = "Remove Password", font = "Arial 20 bold")
RemovePassLabel.grid(row = 0, column = 0)

#Combobox instead of optionmenu
RemoveChosen = StringVar()
RemoveOptions = ttk.Combobox(RemovePassFrame, textvariable=RemoveChosen, state="readonly")
RemoveOptions['values'] = list(data.keys())
RemoveOptions.grid(row = 1, column = 0)
#Button for confirming the account to remove
ViewSelectButton = Button(RemovePassFrame, text = "Confirm", width = 10, height = 2,
                          command = ConfirmRemoval)
ViewSelectButton.grid(row = 2, column = 0)
#Back button
RemoveBackButton = Button(RemovePassFrame, text = "Go Back", width = 10, height = 2,
                               command = ReturnToMenu)
RemoveBackButton.grid(row = 3, column = 0, columnspan = 2)

root.mainloop()

with open("Passwords.json", "w") as f:
    json.dump(data,f,indent=4)
