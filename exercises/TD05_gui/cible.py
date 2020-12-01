import tkinter as tk
COTE= 500
colors = ["blue", "green", "black", "yellow", "magenta", "red"]
nb_cercles = 30

racine = tk.Tk()
canvas = tk.Canvas(racine, width=COTE, height=COTE, bg ="black")
canvas.grid()

epaisseur = (COTE // 2) // nb_cercles

for i in range(nb_cercles):
    canvas.create_oval((epaisseur*i, epaisseur*i), (COTE-epaisseur*i, COTE-epaisseur*i),  fill=colors[i % len(colors)], outline=colors[i % len(colors)])

racine.mainloop()