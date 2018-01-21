from tkinter import *

class Application(Frame):
    """ A GUI Application with three buttons """

    def __init__(self, master):
        """ Initialize the frame """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.bttn1 = Button(self, text = "I do nothing!")
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Me too!")

# main
root = Tk()
root.title("Lazy buttons")
root.geometry("200x85")

app = Application(root)

root.mainloop()

