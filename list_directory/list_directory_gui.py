from tkinter import *
import tkinter as tk

# import other related modules
import list_directory_main
import list_directory_func


def load_gui(self):
    # label widget (Label)
    self.lbl_fpath = tk.Label(self.master,text='Directory Path: ', font=("Helvetica", 13), fg='black', bg='lightgray')
    self.lbl_fpath.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(30,0),pady=(40,10),sticky=W)
    # textbox widget (Entry)
    self.txt_fpath = tk.Entry(self.master,width=45,text='')
    self.txt_fpath.grid(row=1,column=3,rowspan=1,columnspan=3,padx=(30,0),pady=(40,10),sticky=E)
    # button widget (Button)
    self.btn_select_dir = tk.Button(self.master,width=15,height=2,text='Select a directory...',command=lambda: list_directory_func.get_dirname(self)) # call get_dirname()
    self.btn_select_dir.grid(row=3,column=1,rowspan=1,columnspan=1,padx=(30,10),pady=(15,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: list_directory_func.ask_quit(self)) # call ask_quit()
    self.btn_close.grid(row=3,column=5,rowspan=1,columnspan=1,padx=(30,0),pady=(15,10),sticky=E)


if __name__ == "__main__":
    pass