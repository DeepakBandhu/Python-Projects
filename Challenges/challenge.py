import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 300))
        self.master.title('Learning Tkinter!')
        self.master.config(bg ='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.btnBrowseOne = Button(self.master,text='Browse...', font=("Helvetica", 12), fg='black')
        self.btnBrowseOne.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowseTwo = Button(self.master,text='Browse...', font=("Helvetica", 12), fg='black')
        self.btnBrowseTwo.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.btncheck = Button(self.master,text='Check for files...', font=("Helvetica", 12), fg='black')
        self.btncheck.grid(row=2, column=0, padx=(30,0), pady=(10,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Close Program", width = 10, height = 2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(30,0), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
