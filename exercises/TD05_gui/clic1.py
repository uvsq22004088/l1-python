import tkinter as tk

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "black")
canvas.grid(column = 0, row = 1)

def oval(event):
    canvas.create_oval((event.x, event.y),(event.x+1, event.y), fill = "red")
 
racine.bind("<Button-1>", oval)

racine.mainloop()