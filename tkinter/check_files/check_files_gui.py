from tkinter import *
import tkinter as tk

# import other related modules
import check_files_main
import check_files_func


def load_gui(self):
    # textbox widget (Entry)
    self.txt_source_dir = tk.Entry(self.master,width=55,text='')
    self.txt_source_dir.grid(row=1,column=3,rowspan=1,columnspan=3,padx=(20,0),pady=(40,10),sticky=E)
    self.txt_dest_dir = tk.Entry(self.master,width=55,text='')
    self.txt_dest_dir.grid(row=2,column=3,rowspan=1,columnspan=3,padx=(20,0),pady=(0,10),sticky=E)
    # button widget
    self.btn_source_dir = tk.Button(self.master,width=12,height=1,text='Browse')
    self.btn_source_dir.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(20,10),pady=(40,10),sticky=W)
    self.btn_dest_dir = tk.Button(self.master,width=12,height=1,text='Browse')
    self.btn_dest_dir.grid(row=2,column=1,rowspan=1,columnspan=1,padx=(20,10),pady=(0,10),sticky=W)
    self.btn_check_files = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_check_files.grid(row=3,column=1,rowspan=1,columnspan=1,padx=(20,10),pady=(0,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=3,column=5,rowspan=1,columnspan=1,padx=(20,0),pady=(0,10),sticky=E)


if __name__ == "__main__":
    pass