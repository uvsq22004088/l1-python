def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
import tkinter as tk

racine = tk.Tk()

canvas= tk.Canvas(racine, height=256, width=256, bg='black')
canvas.grid(column=1, row=1, rowspan=3)

button1 = tk.Button(text="Aléatoire", font=("helvetica", "20"), fg= 'blue')
button1.grid(column=0, row=1)


button2 = tk.Button(text="Dégradé gris", font=("helvetica", "20"), fg='blue')
button2.grid(column=0, row=2)

button3 = tk.Button(text="Dégradé 2D", font=("helvetica", "20"), fg='blue')
button3.grid(column=0, row=3)

racine.mainloop()

def draw_pixel(i, j, color):
    color = "white"
    return 

