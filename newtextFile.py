from tkinter import *
import tkinter as tk
import webbrowser

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

button1 = tk.Button(text='Enter your text: ', command=lambda:openInBrowser())
canvas1.create_window(200, 180, window=button1)

def openInBrowser():
    f = open('userEntry.html','w')
    text1 = entry1.get()
    message = "<html> <head></head> <body> <h1><p> {} </p></h1> </body> </html>".format(text1)
    f.write(message)
    f.close()
    webbrowser.open('userEntry.html')




root.title("Text Entry Gui")
root.mainloop()
