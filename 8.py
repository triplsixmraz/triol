from tkinter import *

def draw_scene():
    canvas.delete('all')
    canvas.create_rectangle(50, 150, 150, 250, fill='gray')
    canvas.create_polygon(50, 150, 150, 150, 100, 100, fill='black')
    canvas.create_rectangle(100, 200, 120, 250, fill='black')
    canvas.create_rectangle(130, 200, 150, 250, fill='black')
    canvas.create_oval(100, 100, 150, 150, fill='gray')
    canvas.create_line(100, 125, 150, 125, fill='gray')

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()
draw_scene()
root.mainloop()