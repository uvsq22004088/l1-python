import tkinter as tk

racine = tk.Tk() 
label1 = tk.Label(racine, text="Un texte long dans ma fenêtre", font = ("helvetica", "30")) 
label2 = tk.Label(racine, text="toto", font = ("helvetica", "30")) 
label1.grid(column=0, row=0)
label2.grid(row=1, column=0) 
racine.mainloop() 