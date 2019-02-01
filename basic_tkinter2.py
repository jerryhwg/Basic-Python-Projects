import tkinter
from tkinter import * # * means all widgets


class ParentWindow(Frame): # ParentWindow(child) inherits from Frame(parent class within tkinter)
    def __init__ (self, master): # class(ParentWindow) as self, Frame as master
         Frame.__init__ (self) # the 3 lines are typical(common)

         # a blue print to create a tkinter window
         self.master = master # primary window to pop up
         self.master.resizable(width=False, height=False) # disable the window resize option
         self.master.geometry('{}x{}'.format(700, 400)) # specific size of the main window
         self.master.title('Learning Tkinter!') # window title
         self.master.config(bg='lightgray') # window background color

         self.varFName = StringVar() # StringVar class: instantiate and pass over to a variable name(varFName)
         self.varLName = StringVar()
        
         # this section is for a test(debug) purpose
         #self.varFName.set('Bob')
         #self.varLName.set('Smith')
         #print(self.varFName.get())
         #print(self.varLName.get())

         ## Textbox label name
         self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
         self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

         self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
         self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

         ## Text display from the textbox and submit   
         self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
         self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
         
         ## Textbox(Entry)
         self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue') # Entry is a widget for textbox # self.master is the main window
         self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0)) # use grid as geometry manager (use either pack or grid)

         self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
         self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))
         
         ## Button
         self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) # command to call for a function
         self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

         self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
         self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get() # get a text(for firstname) input and stored it as fn
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln)) # display fn, ln together

    def cancel(self):
        self.master.destroy() # close the main(tkinter) window


if __name__ == "__main__":
    root = Tk() # instantiate Tk class, and root as a new instance(name)
    App = ParentWindow(root) # passing in to the class program, App
    root.mainloop() # a function to keep the window open(alive)
