# Python 3.7.2
#
# Scenario
# Create a python script to creates a GUI
# to move only .txt files from a source directory to a target directory in GUI
# save the qualified txt files with corresponding modified time-stamps to a database
# read the records from the database to a console
#
# Tested OS: Windows 10

from tkinter import *
import tkinter as tk

# import other related modules
import move_files_gui
import move_files_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(550,300)
        self.master.maxsize(550,300)
        # center app on the user's screen
        move_files_func.center_window(self,550,300)
        self.master.title("Text Files Migration Tool")
        self.master.configure(bg="lightgray")
        # delete x button
        self.master.protocol("WM_DELETE_WINDOW", lambda: move_files_func.ask_quit(self))
        # load GUI
        move_files_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
