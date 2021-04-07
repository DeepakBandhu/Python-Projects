from tkinter import *
import tkinter as tk
import webbrowser

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

f = open('userEntry.html','w')

entry = input("enter text: ")

message = "<html> <head></head> <body> <h1><p> {} </p></h1> </body> </html>".format(entry)

f.write(message)
f.close()

    
button1 = tk.Button(text='Enter your text: ',)
canvas1.create_window(200, 180, window=button1)
webbrowser.open_new_tab('userEntry.html')



root.title("Text Entry Gui")
root.mainloop()
