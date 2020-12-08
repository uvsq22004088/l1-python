
import tkinter as tk

racine = tk.Tk()

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
def draw_pixel(i, j, color):
    canvas.create_line((i,j), (i+1, j), fill = color)

def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            color = get_color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
            draw_pixel(i, j, color)

def degrade_gris():
    for i in range(256):
        color = get_color(i, i, i)
        for j in range(256):
            draw_pixel(i, j, color)


def degrade_2D():
    for i in range(256):
        for j in range(256):
            color = get_color(i, 0, j)
            draw_pixel(i, j, color)


canvas= tk.Canvas(racine, height=256, width=256, bg='black')
canvas.grid(column=1, row=1, rowspan=3)

button1 = tk.Button(racine, text="Aléatoire", font = ("helvetica", "20"), fg= 'blue', padx = 20, command = ecran_aleatoire)
button1.grid(column=0, row=1)


button2 = tk.Button(racine, text="Dégradé gris", font = ("helvetica", "20"), fg='blue', padx = 20,  command = degrade_gris)
button2.grid(column=0, row=2)

button3 = tk.Button(racine, text="Dégradé 2D", font = ("helvetica", "20"), fg='blue', padx = 20, command = degrade_2D)
button3.grid(column=0, row=3)

racine.mainloop()
