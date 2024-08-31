import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

def on_button_click():
     print("Alguien presiono el boton")

button = tk.Button(root, text="Haz click pe", command=on_button_click)
button.pack()

def entered_value(event):
     print("Alguien presiono el texto")

label = tk.Label(root, text="Soy el texto")
label.pack()
label.bind("<Button-1>", entered_value)

options = {"Pyhton", "Javascript", "Java"}
combobox = ttk.Combobox(root, values=options)
combobox.pack()

entry = tk.Entry(root)
entry.pack()

checkbutton = tk.Checkbutton(root, text="Acepto los terminos y condiciones")
checkbutton.pack()

radio1 = tk.Radiobutton(root, value="Opcion 1")
radio1.pack()
radio2 = tk.Radiobutton(root, value="Opcion 2")
radio2.pack()
radio3 = tk.Radiobutton(root, value="Opcion 3")
radio3.pack()

spinbox = ttk.Spinbox(root, from_=0, to=100)
spinbox.pack()

frame = tk.Frame(root, width=200, height=100, bg="lightblue")
frame.pack()

root.mainloop()