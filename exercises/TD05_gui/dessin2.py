import tkinter as tk
import random as rd

ma_couleur="blue"
HEIGHT = 600
WIDTH = 600

objets = []

racine = tk.Tk()
racine.title("Mon dessin")

def choisir():
    """Demande une couleur à l'utilisateur dans le terminal"""
    global ma_couleur
    ma_couleur= input("Choisis une couleur")
    
def cercle():
    """cercle de diamètre 100 et de couleur bleu"""
    global objets
    x = rd.randint(0, 401)
    y = rd.randint(0,401)    
    objets.append(canvas.create_oval((x, y), (x + 100, y + 100), fill = ma_couleur))

def carre():
    """affiche un carre rouge de côté 100"""
    global objets
    x = rd.randint(0,401)
    y = rd.randint(0,401)
    objets.append(canvas.create_rectangle((x, y), (x+100, y+100), fill= ma_couleur))

def croix():
    """affiche une croix jaune inscrite dans un carre de côté 100"""
    global objets
    x = rd.randint(0,401)
    y = rd.randint(0,401)
    objets.append(canvas.create_line((x, y), (x+100, y+100), fill= ma_couleur))
    objets.append(canvas.create_line ((x+100, y), (x, y+100), fill= ma_couleur))


def undo():
    if canvas.type(objets[-1]) == "line":
        canvas.delete(objets[-1])
        del (objets[-1])
        canvas.delete(objets[-1])
        del (objets[-1])
    else :
        canvas.delete(objets[-1])
        del (objets[-1])
        





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

button5 = tk.Button(text="Undo", fg="blue", font=("helvetica", "20"), command = undo)
button5.grid(column=2, row=0)
racine.mainloop()