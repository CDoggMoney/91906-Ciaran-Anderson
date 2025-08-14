from tkinter import *
from tkinter import ttk
import json

def Return():
    ViewFrame.pack_forget()
    LoginedFrame.pack(fill="both", expand=True)

def ReturnToView():
    ViewPassFrame.pack_forget()
    ViewFrame.pack(fill="both", expand=True)

def ViewPasswordSwitch():
    Choice = ViewChosen.get()
    if Choice != "          ":
        ViewFrame.pack_forget()
        ViewPassFrame.pack(fill="both", expand=True)
        #Edits label for top text
        ViewPassLabel.config(text=f"Username and Password for {Choice}")
        #Edits Label for Username/Email
        ViewUser.config(text = f"Username/Email: {data[Choice]['Email']}")
        #Edits Label for Password
        ViewPass.config(text = f"Password: {data[Choice]['Password']}")
    else:
        ElseLabel = Label(ViewFrame, font = "Arial 8", text = "You need to select something for the select button to work.")
        ElseLabel.grid(row = 4, column = 0)

def ViewPasswords():
    LoginedFrame.pack_forget()
    ViewFrame.pack(fill="both", expand=True)

def AddRemovePasswords():
    print("To be included in v3")
#Sets up root and name of program
root = Tk()
root.title("Password Manager")
#Opens the json file containing the saved passwords and usernames
with open("Passwords.json") as f:
    data = json.load(f)

#Frame which will appear upon successful login
LoginedFrame = Frame(root)
LoginedFrame.pack(fill="both", expand=True)
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
                          command = Return)
BackButton.grid(row = 2, column = 0, columnspan = 2)

#Frame which appears when view password button is pressed
ViewFrame = Frame(root)
ViewLabel = Label(ViewFrame ,text = "Passwords", font = "Arial 20 bold")
ViewLabel.grid(row = 0, column = 0)
#Makes the choices for the drop down menu the keys to the dictionary json file which are the account names
ViewChoices = data
ViewDefault = "          "
ViewChosen = StringVar()
ViewOptions = ttk.OptionMenu(ViewFrame, ViewChosen, ViewDefault, *ViewChoices)
ViewOptions.grid(row = 1, column = 0)
#Button for confirming the selected account
ViewSelectButton = Button(ViewFrame, text = "Select", width = 10, height = 2,
                          command = ViewPasswordSwitch)
ViewSelectButton.grid(row = 2, column = 0)
#Back button
ViewBackButton = Button(ViewFrame, text = "Back", width = 10, height = 2,
                          command = Return)
ViewBackButton.grid(row = 3, column = 0)
#Text which will appear when user does not select anything before pressing the select button

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


root.mainloop()
