# Python 3.7.2
#
# Scenario: phonebook application with tkinter gui module and sqlite3 database
#
# OS environment: Windows 10

from tkinter import *
import tkinter as tk

# Importing other related modules
import phonebook_gui
import phonebook_func

# Frame is the tkinter frame class as parent that our main window class(ParentWindow) will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs): # init is a reserved method to initialize the attributes of a class
        Frame.__init__(self, master, *args, **kwargs) # self allows to access the attributes and methods of the class

        # define master frame configuration
        self.master = master # master = Frame, self = ParentWindow
        self.master.minsize(500,300) # 500 height, 300 width
        self.master.maxsize(500,300)
        # This CenterWindow method will center app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self)) # protocol: rule, lambda: call lambda function(anonymous function)
        # self: key to access everyting within the class
        arg = self.master
        
        # load in the GUI widgets from a separate module
        phonebook_gui.load_gui(self) # call for a load_gui function in phonebook_gui module


if __name__ == "__main__":
    root = tk.Tk() # tkinter module to be root (create a window from tkinter module)
    App = ParentWindow(root) # ParentWindow(App) attach root(Window)
    root.mainloop() # keep the main window open
