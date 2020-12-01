import tkinter as tk
import random as rd

ma_couleur="blue"
HEIGHT = 600
WIDTH = 600

racine = tk.Tk()
racine.title("Mon dessin")

def choisir():
    """Demande une couleur à l'utilisateur dans le terminal"""
    global ma_couleur
    ma_couleur= input("Choisis une couleur")
    


def cercle():
    """cercle de diamètre 100 et de couleur bleu"""
    x = rd.randint(0, 401)
    y = rd.randint(0,401)    
    canvas.create_oval((x, y), (x + 100, y + 100), fill = ma_couleur) in canvas

def carre():
    """affiche un carre rouge de côté 100"""
    x = rd.randint(0,401)
    y = rd.randint(0,401)
    canvas.create_rectangle((x, y), (x+100, y+100), fill= ma_couleur)

def croix():
    """affiche une croix jaune inscrite dans un carre de côté 100"""
    x = rd.randint(0,401)
    y = rd.randint(0,401)
    canvas.create_line((x, y), (x+100, y+100), fill= ma_couleur)
    canvas.create_line ((x+100, y), (x, y+100), fill= ma_couleur)



canvas = tk.Canvas(racine, height=500, width=500, bg="black", bd=10, relief="raised")
canvas.grid(column=1, row=1, rowspan=3)

button1 = tk.Button(text="choisir une couleur", command=choisir, fg="blue", font=("helvetica", "20"))
button1.grid(column=1, row=0)


button2 = tk.Button(text="Cercle", command=cercle, fg="blue", font=("helvetica", "20"))
button2.grid(column=0, row=1)

button3 = tk.Button(text="Carré", command=carre, fg="blue", font=("helvetica", "20"))
button3.grid(column=0, row=2)

button4 = tk.Button(text="Croix", command=croix, fg="blue", font=("helvetica", "20"))
button4.grid(column=0, row=3)

racine.mainloop()