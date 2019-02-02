import os
import tkinter as tk
from tkinter import *
import sqlite3


# import other related modules
import phonebook_main
import phonebook_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height for windows user
    screen_width = self.master.winfo_screenwidth() # self.master = tkinter primary window
    screen_height = self.master.winfo_screenheight() # winfo_screenheight(): method from tkinter module to get user's height
    # store the user's height(or width) in our own variable name(screen_height)
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2)) # screen_width: user's width, w: our specified value from main
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y)) # method: geometry, () returns the position value
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"): # tkinter confirmation messagebox
        # askokcancel: method to confirm yes or no to proceed the following action
        # This closes app
        self.master.destroy() # if yes, close the dialog window
        os._exit(0) # _exit method: once close, release the occupied memory from the system


#==================================================================================================
def create_db(self): # called from phonebook_gui module
    conn = sqlite3.connect('phonebook.db') # connect to a db(phonebook.db) in the built-in sqlite3 database engine
    with conn: # if database connection successful
        cur = conn.cursor() # with sqlite db connection, you can create a cursor object and call its execute() method to perform SQL commands
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # must commit() to save chnages & close the database connection
        conn.commit()
    conn.close() # db connection close, always can reopen with conn:
    first_run(self) # call first_run function below and 'self' to allow to access everything in the class


def first_run(self): # only for the first run with an empty database
    #data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com') # tuple, 'John' as index 0
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur) # function, cur: connection, count from database returned
        if count < 1: # if no rows in database
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com'))
            conn.commit()
    conn.close()


def count_records(cur):
    count=""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0] # fetchone: retrieve a single matching row, [0]: first index of tuple
    return cur,count


# select item in ListBox
def onSelect(self,event):
    # calling the event is the self.lstList1 widget
    varList = event.widget