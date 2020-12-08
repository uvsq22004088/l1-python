import tkinter as tk

racine = tk.Tk()

canvas = tk.Canvas(racine, height=500, width=500, bg="black", bd=10)
canvas.grid(column=0, row=0)

racine.mainloop()