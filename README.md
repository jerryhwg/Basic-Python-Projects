# Basic-Python-Projects

## move_files app

* moving files from a source directory to a target directory in GUI
* class, function, modules
* module: os, tkinter, shutil
* askdirectory(), listdir(), path.join(), getmtime(), move()
* widget: label, entry, button
* loop
* sqlite3 database

## phonebook app

* phonebook app
* python tkinter module
* sqlite3 database
* separate modules

## game_nice_mean.py

* passing in variables
* function with variable and return variable
* while loop
* if, elif, else
* dunder method
* comment

## Python Basics

#### basic_class.py

* parent, child class
* class attribute, behavior(action)
* inherit, instantiation, constructor
* return to a calling method
* dunder method

#### basic_db_init.py

* work with database (sqlite3)
* create database
* add, read data

    ```SQL
    conn = sqlite3.connect('test.db')
    with conn:
    cur = conn.cursor()
    cur.execute(SQL statement)
    conn.commit()
    conn.close()
    ```

#### basic_error_handle1.py

* try, except, finally

#### basic_file_io.py

* import os module
* read, write

### basic_function.py

* a function call from a main
* return to the calling main
* global, local variable
* declare an empty variable
* for loop, append()

#### basic_loop.py

* for loop
* while loop
* a function call from a main
* return to the calling main

#### basic_tkinter2.py

* tkinter module for GUI
* form, submit, display
* grid(), pack()
* StringVar()

#### check_files

* simple GUI for checking files
* tkinter module
* class, function
* 3 modules
* label, entry, button widget
* grid()

#### list_directory

* simple GUI for listing a selected directory
* tkinter module
* class, function
* label, entry, button widget
* askdirectory()

#### drill_db_init_ops.py

* create database
* add data from a tuple
* read data with files with ".txt"

#### drill_txt_file_check.py

* for loop
* os module: listdir(), path.join(), path.getmtime()
* check file extension