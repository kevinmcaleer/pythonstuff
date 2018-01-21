# simple GUI
# Demonstrates creating a window

from tkinter import *

root = Tk()
app = Frame(root)

def setupwindow():

    # modify the window
    root.title("Simple Gui")
    root.geometry("200x100")

    # create a frame in the window to hold other widgets
    app.grid()

def addlabels():
    # create a label in the frame
    lbl = Label(app, text = "I'm a label!")
    lbl.grid()


def createbuttons():
    bttn1 = Button(app, text="I do nothing")
    bttn1.grid()

setupwindow()
addlabels()
createbuttons()
# kick off the window's event loop
root.mainloop()
