import tkinter as tk

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "black")
canvas.grid(column = 0, row = 1)

def draw_circle(event):
    if event.x < 250:
        color = "blue"
    else:
        color = "red"
    canvas.create_oval((event.x-50, event.y-50), (event.x+50, event.y+50), fill=color)

def oval(event):
    canvas.create_oval((event.x, event.y),(event.x+1, event.y), fill = "red")
 
canvas.bind("<Button-1>", draw_circle)
canvas.create_line((250, 0), (250, 500), fill = "white")

racine.mainloop()