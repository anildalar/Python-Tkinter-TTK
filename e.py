from tkinter import ttk
from ttkthemes import ThemedTk
 
window = ThemedTk(theme="breeze-dark")
ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()