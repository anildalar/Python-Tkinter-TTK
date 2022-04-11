from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

ws = Tk()
ws.title('Python Guides')
ws.geometry('250x200')
style = ThemedStyle(ws)
style.set_theme("plastik")

frame1 = Frame(ws, padx=5, pady=5)
frame1.grid(row=0, column=1)

ttk.Label(frame1, text='Name').pack()
ttk.Label(frame1, text='Email').pack()
ttk.Label(frame1, text='Password').pack()
 

frame2 = Frame(ws, padx=5, pady=5)
frame2.grid(row=0, column=2)

ttk.Entry(frame2).pack(padx=5, pady=5)
ttk.Entry(frame2).pack(padx=5, pady=5)
ttk.Entry(frame2).pack(padx=5, pady=5)


ttk.Button(ws, text='Submit').grid(row=1, columnspan=5, pady=5)


ws.mainloop()