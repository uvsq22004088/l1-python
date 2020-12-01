import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
x = CANVAS_WUDTH // 2
y1 = 100
y2 = CANVAS_HEIGHT - 100
canvas.create_line((x, y1), (x,y2))
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50) #(250, 150), (350, 50)
canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50) #(250, 350), (350, 250)
canvas.create_oval(x - 50, (y1 + y2) // 2 + 50, x + 50, (y1 + y2) // 2 - 50)

canvas.grid()
root.mainloop()
