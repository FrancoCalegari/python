import tkinter as tk

# Creamos una función que se ejecutará al hacer clic en el botón
def saludar():
    label_saludo.config(text="¡Hola, Mundo!")

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Mi Ventana")

# Creamos una etiqueta en la ventana
label_saludo = tk.Label(ventana, text="¡Hola!")
label_saludo.pack(pady=10)

# Creamos un botón en la ventana
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Ejecutamos el bucle principal de la ventana
ventana.mainloop()


#en caso de que no se ejecute en linux ubuntu probar instalar "sudo apt-get install python3-tk"