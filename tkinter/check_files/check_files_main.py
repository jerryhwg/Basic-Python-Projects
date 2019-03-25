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
import check_files_gui
import check_files_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,170)
        self.master.maxsize(500,170)
        # center app on the user's screen
        check_files_func.center_window(self,500,200)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")
        # delete x button
        self.master.protocol("WM_DELETE_WINDOW", lambda: check_files_func.ask_quit(self))
        # load GUI
        check_files_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
