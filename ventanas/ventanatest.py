import tkinter as tk
from tkinter import messagebox

def mostrar_frase():
    frase = entrada.get()
    lfrase = len(frase)
    if lfrase <= 15:
        messagebox.showinfo("Frase demasiado corta", "La frase no tiene más de 15 caracteres.")
    else:
        messagebox.showinfo("Frase con más de 15 caracteres", frase)
        if frase == "Aguante la programcion":
            messagebox.showinfo("¡Felicidades!", "¡Aguante terminaste rey!")
            ventana.quit()

def salir():
    respuesta = messagebox.askquestion("Salir", "¿Estás seguro/a de que quieres salir?")
    if respuesta == "yes":
        ventana.quit()

ventana = tk.Tk()
ventana.title("Contador de caracteres")

etiqueta = tk.Label(ventana, text="Ingresa una frase:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton_mostrar = tk.Button(ventana, text="Mostrar frase", command=mostrar_frase)
boton_mostrar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=5)

ventana.mainloop()

print("¡Que tengas un buen día!")
