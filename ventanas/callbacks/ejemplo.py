import tkinter as tk



ventana = tk.Tk()
ventana.title("Ejemplo de Label")
ventana.geometry("400x600")
ventana.configure(bg="#eeeeee")

etiqueta = tk.Label(ventana, text="")
etiqueta2 = tk.Label(ventana, text="")


def onClick (event): #importaante que tenga "event"
    etiqueta.config(text="Boton presionado")

def onClickKey (event): #importaante que tenga "event"
    global count #global se usa para una variable fuera del alcance de la funcion declarada
    if event.char == 'a' or event.char == 'A':
        count +=1
        etiqueta2.config(text=f"Boton 'a' presionado {count} veces")
count = 0



boton = tk.Button(ventana, text="Click")
boton.bind("<Button-2>", onClick)#siendo "<Button-2>" el boton a escuchar de las entradas de la pc se puede usar para cualquier boton siendo "{1}{btnIzquierdo},{2}{btnCentral},{3}{btnDerecho}" del mouse

ventana.bind("<KeyPress>", onClickKey)




etiqueta.pack()
etiqueta2.pack()
boton.pack()




ventana.mainloop()