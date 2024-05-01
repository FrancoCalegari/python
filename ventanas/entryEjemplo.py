import tkinter as tk
import time
ventana = tk.Tk()
ventana.title("Ejemplo de Label")
ventana.geometry("400x600")
ventana.configure(bg="#eeeeee")

etiqueta1 = tk.Label(ventana, text="Hola gente de youtube")
etiqueta1.config(fg="black", bg="#dddddd", font=("arial", 16, "bold"))
etiqueta1.pack()



def actualizarHOra (): #creamos un reloj
    etiqueta1.config(text=time.strftime("%H-%M-%S"))
    ventana.after(1080, actualizarHOra) #sirve para ejecutar una funcion cada cierto tiempo

actualizarHOra()

etiqueta2 = tk.Label(ventana, text="")
etiqueta2.pack()

def clickBtn ():
    etiqueta2.config(text="Boton Presionado", bg="#dddddd", fg="black")

boton = tk.Button(ventana, text="click")
boton.config(command=clickBtn)
boton.pack()

entry = tk.Entry(ventana, text="Entrada:")
# entry.insert(0, "Inserta algo loco: ") #al ejecutar esto se muestra en el print y se muestra en consola

etiqueta3 = tk.Label(ventana, text="")

def printNomb ():
    entradat = entry.get()
    etiqueta3.config(text=entradat)

boton2 = tk.Button(ventana, text="print nombre", command=printNomb)#mucho mas comodo que "boton2.config(command=printNomb)" por separado

etiqueta3.pack()
entry.pack()
boton2.pack()




ventana.mainloop()