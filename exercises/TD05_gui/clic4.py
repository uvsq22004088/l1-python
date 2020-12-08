import tkinter as tk

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "black")
canvas.grid(column = 0, row = 1)

cpt = 0
def alterne(event):
    global cpt
    if cpt % 2 == 0:
        color = "white"
    else:
        color="black"
    cpt += 1
    canvas.itemconfigure(rectangle, fill = color)
    if cpt > 9:
        racine.destroy()
 
rectangle = canvas.create_rectangle((100, 100), (400, 400), outline = "white", fill = "black")
canvas.bind("<Button-1>", alterne)

racine.mainloop()