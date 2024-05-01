import tkinter as tk

ventana = tk.Tk()

ventana.title("Primer ventana")
ventana.geometry("800x600+100+300")
ventana.minsize(400, 200)
ventana.maxsize(1020,768)
# ventana.iconbitmap("icono.ico")
ventana.configure(bg="#D3D3D3")
# ventana.resizable(False,True)
# ventana.attributes("-alpha",0.2) #supuestamente en windows la ventana se hace algo transparente


frame1 = tk.Frame(ventana)
frame1.configure(width=200, height=200, bg="red", bd=5)

labelframe = tk.LabelFrame(ventana, text="hola mundo", bg="blue", padx=10,pady=10)
labelframe.configure(width=400, height=800)

frame2 = tk.Frame(frame1)
frame2.configure(width=250, height=250, bg="blue", bd=5)

boton = tk.Button(frame1, text="Click")


frame1.pack()
frame2.pack()
boton.pack()
labelframe.pack()


ventana.mainloop()