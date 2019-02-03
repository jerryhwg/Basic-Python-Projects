# Python 3.7.2
#
# Scenario
# Create a python script to creates a GUI
# Use Python 3 and Tkinter module
# Create the same GUI as supplied
#
# Tested OS: Windows 10

from tkinter import *
import tkinter as tk

# import other related modules
import list_directory_gui
import list_directory_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(550,170)
        self.master.maxsize(550,170)
        # center app on the user's screen
        list_directory_func.center_window(self,550,200)
        self.master.title("List Directory")
        self.master.configure(bg="lightgray")
        # delete x button
        self.master.protocol("WM_DELETE_WINDOW", lambda: list_directory_func.ask_quit(self))
        # load GUI
        list_directory_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
