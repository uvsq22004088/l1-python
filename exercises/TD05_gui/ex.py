import tkinter as tk

HEIGHT = 500
WIDTH = 500

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
canvas.grid()
canvas.create_line((0, 0), (WIDTH/2, HEIGHT/2), (WIDTH, 0), fill="blue", width=5)
racine.mainloop() # Lancement de la boucle principale