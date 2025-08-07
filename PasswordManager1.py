from tkinter import *
import json
import os
os.chdir("N:/13PRG/st21033-Ciaran/91907CiaranAnderson")

def Return():
    print("not availible")

def ViewPasswords():
    LoginedFrame.pack_forget()
    ViewFrame.pack(fill="both", expand=True)

def AddRemovePasswords():
    print("arf arf")

root = Tk()
root.title("Password Manager")

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

root.mainloop()
