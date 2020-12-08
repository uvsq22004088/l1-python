import tkinter as tk

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "black")
canvas.grid(column = 0, row = 1)

nb_clic = 0
point = (0,0)

def draw_line(event):
    global nb_clic, point
    if nb_clic ==0:
        nb_clic = 1
        point = (event.x, event.y)
    else:
        nb_clic = 0
        if (250 - event.x)*(250-point[0]) >= 0:
            color = "blue"
        else:
            color = "red"
        canvas.create_line(point, (event.x, event.y), fill = color)

 
canvas.bind("<Button-1>", draw_line)
canvas.create_line((250, 0), (250, 500), fill = "white")

racine.mainloop()