import tkinter

myScreen = tkinter.Tk()
myScreen.minsize(width=100, height=100)
def buttonClicked():
    print("Clicked")


newButton = tkinter.Button(text="Click me", command=buttonClicked)
newButton.grid(column=0, row=0)

myScreen.mainloop()