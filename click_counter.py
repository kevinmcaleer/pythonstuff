# click counter

from tkinter import *

class Application(Frame):
    """ A GUI Application with three buttons """

    def __init__(self, master):
        """ Initialize the frame """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.bttn_clicks = 0

    def create_widgets(self):
        self.bttn = Button(self)
        self.bttn["text"]= "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """ increase the clicks and display new total """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()