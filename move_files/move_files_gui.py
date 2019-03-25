from tkinter import *
import tkinter as tk

# import other related modules
import move_files_main
import move_files_func


def load_gui(self):
    # label widget (Label)
    self.lbl_srcpath = tk.Label(self.master,text='Source Directory: ', font=("Helvetica", 13), fg='blue', bg='lightgray')
    self.lbl_srcpath.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(30,0),pady=(40,0),sticky=W)
    self.lbl_tgtpath = tk.Label(self.master,text='Target Directory: ', font=("Helvetica", 13), fg='red', bg='lightgray')
    self.lbl_tgtpath.grid(row=3,column=1,rowspan=1,columnspan=1,padx=(30,0),pady=(10,0),sticky=W)
    # textbox widget (Entry)
    self.txt_srcpath = tk.Entry(self.master,width=50,text='')
    self.txt_srcpath.grid(row=1,column=3,rowspan=1,columnspan=3,padx=(30,0),pady=(40,0),sticky=E)
    self.txt_tgtpath = tk.Entry(self.master,width=50,text='')
    self.txt_tgtpath.grid(row=3,column=3,rowspan=1,columnspan=3,padx=(30,0),pady=(10,0),sticky=E)
    # button widget (Button)
    self.btn_srcpath = tk.Button(self.master,width=15,height=2,text='Select a directory...',command=lambda: move_files_func.get_srcpath(self)) # call get_dirname()
    self.btn_srcpath.grid(row=2,column=1,rowspan=1,columnspan=1,padx=(30,10),pady=(10,10),sticky=W)
    self.btn_tgtpath = tk.Button(self.master,width=15,height=2,text='Select a directory...',command=lambda: move_files_func.get_tgtpath(self)) # call get_dirname()
    self.btn_tgtpath.grid(row=4,column=1,rowspan=1,columnspan=1,padx=(30,10),pady=(10,10),sticky=W)
    self.btn_movfiles = tk.Button(self.master,width=15,height=2,text='Move txt files...',command=lambda: move_files_func.move_files(self)) # call get_dirname()
    self.btn_movfiles.grid(row=6,column=1,rowspan=1,columnspan=1,padx=(30,10),pady=(15,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: move_files_func.ask_quit(self)) # call ask_quit()
    self.btn_close.grid(row=6,column=5,rowspan=1,columnspan=1,padx=(30,0),pady=(15,10),sticky=E)


if __name__ == "__main__":
    pass