import tkinter
from datetime import datetime
dt = datetime.now()

def ventana_balance():
    main_window = tkinter.Tk()
    
    balance = tkinter.Label(main_window, text = 'Balance')
    tkinter.mainloop()