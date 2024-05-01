import tkinter as tk


#///////////////
#se crean las ventanas o root en ingles y se les da una configuracion inicial
ventana = tk.Tk()
ventana.title("Ejemplo de Callback")
ventana.geometry("400x600")
ventana.configure(bg="#eeeeee")
#///////////////
#se crean las etiquetas o label en ingles
etiqueta = tk.Label(ventana, text="")
etiqueta2 = tk.Label(ventana, text="")
etiqueta3 = tk.Label(ventana, text="test")

#///////////////
def onClick (event): #importaante que tenga "event"
    etiqueta.config(text="Boton presionado")
#///////////////
def onClickKey (event): #importaante que tenga "event"
    global count #global se usa para una variable fuera del alcance de la funcion declarada
    if event.char == 'a' or event.char == 'A':
        count +=1
        etiqueta2.config(text=f"Boton 'a' presionado {count} veces")
count = 0
#///////////////
def onResize(event): #importaante que tenga "event"
        initial_width = ventana.winfo_width() #extraer resolucion de ventana actual
        initial_height = ventana.winfo_height()
        etiqueta3.config(text=f"Resolución actual: {initial_width}x{initial_height}")

initial_width = ventana.winfo_width()
initial_height = ventana.winfo_height()
etiqueta3.config(text=f"Resolución actual: {initial_width}x{initial_height}")
#///////////////
boton = tk.Button(ventana, text="Click")

#///////////////
boton.bind("<Button-2>", onClick)#siendo "<Button-2>" el boton a escuchar de las entradas de la pc se puede usar para cualquier boton siendo "{1}{btnIzquierdo},{2}{btnCentral},{3}{btnDerecho}" del mouse

ventana.bind("<KeyPress>", onClickKey) #cada vez que se detecta una tecla espesifica del teclado se llama a la funcion y se ejecuta

ventana.bind("<Configure>", onResize) #cada vez que se cambie la resolucion se llama a la funcion y se ejecuta
#///////////////
#se empaquetan y ordenan de arriba hacia abajo los item que se muestran en ventana
etiqueta.pack()
etiqueta2.pack()
etiqueta3.pack()
boton.pack()



#///////////////
ventana.mainloop()