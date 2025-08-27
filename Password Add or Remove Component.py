from tkinter import *
from tkinter import ttk
import json

def Return():
    print("You can't")

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
    RemoveOptions['values'] = list(data.keys())
    RemoveChosen.set("")

#Sets up root and name of program
root = Tk()
root.title("Password Manager")

#Opens the json file containing the saved passwords and usernames for use
with open("Passwords.json") as f:
    data = json.load(f)

#Menu frame which appears when Add/Remove Passwords is selected on the menu
MenuFrame = Frame(root)
MenuFrame.pack(fill="both", expand=True)
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