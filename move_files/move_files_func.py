import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import tkinter as tk
import sqlite3

# import other related modules
import move_files_main
import move_files_gui


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


def get_srcpath(self):
        # function call from list_directory.gui to use askdirectory() from tkinter.filedialog module
        Tk().withdraw()
        print("Initializing Dialogue...\nPlease select a directory.")
        dirname = askdirectory(initialdir=os.getcwd(),title='Please select a directory') # main 'askdirectory' code
        if len(dirname) > 0: # a directory is selected
                print("You chose {} as a source directory".format(dirname)) # console output for debug purpose
                var = StringVar() # define var as string
                var.set(dirname) # set var from dirname output
                self.txt_srcpath.config(text='{}'.format(var)) # formatting 'text' in txt_fpath (Entry) widget
        else:
                dirname = os.getcwd()
                print("\nNo directory selected - Initializing with %s \n" % os.getcwd())
                return dirname
        

def get_tgtpath(self):
        # function call from list_directory.gui to use askdirectory() from tkinter.filedialog module
        Tk().withdraw()
        print("Initializing Dialogue...\nPlease select a directory.")
        dirname = askdirectory(initialdir=os.getcwd(),title='Please select a directory') # main 'askdirectory' code
        if len(dirname) > 0: # a directory is selected
                print("You chose {} as a target directory".format(dirname)) # console output for debug purpose
                var = StringVar() # define var as string
                var.set(dirname) # set var from dirname output
                self.txt_tgtpath.config(text='{}'.format(var)) # formatting 'text' in txt_fpath (Entry) widget
        else:
                dirname = os.getcwd()
                print("\nNo directory selected - Initializing with %s \n" % os.getcwd())
                return dirname


if __name__ == "__main__":
    pass # this module run only from main