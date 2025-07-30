from tkinter import *

def Login(dict):
    username = float(UsernameEntry.get())
    password = float(PasswordEntry.get())
    try:
        if username == dict["Login"]["Username"] and password == dict["Login"]["Password"]:
            print("meow")
        else:
            print("woof woof")
    except ValueError:
        print("moo")



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
PasswordEntry = Entry(LoginFrame, justify = CENTER, font = "Arial 15")
PasswordEntry.grid(row = 2, column = 1, sticky = "nsew")
#button to confirm username and password
LoginButton = Button(LoginFrame, text = "Login", width = 10, height = 2,
                          command = Login(PasswordDictionary), bg = "grey")
LoginButton.grid(row = 3, column = 0, sticky = "nsew", padx = 5, pady = 5, columnspan = 2)


root.mainloop()