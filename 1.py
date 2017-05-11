from tkinter import *
from tkinter import ttk
import random


menu = Tk() 
menu.title("Road Fighter")
menu.geometry("1450x800")

titulo = Label(menu,text="ROAD FIGHTER")

imagen = PhotoImage(file="imagen_principal.PNG")

fondo = Label(menu,image=imagen).pack(padx=0,pady=0)

def Jugar ():

        menu.destroy()
        nombres = Tk()
        nombres.title("Road Fighter")
        nombres.geometry("700x400")


        etiqueta1 = Label(nombres,text="Jugador 1:").place(x=100,y=70)
                           
        usuario1 = StringVar()

        ctx1 = Entry(nombres,textvariable=usuario1, width=50).place(x=100,y=100)

        etiqueta2 = Label(nombres,text="Jugador 2:").place(x=100,y=190)

        usuario2 = StringVar()

        ctx2 = Entry(nombres,textvariable=usuario2, width=50).place(x=100,y=220)

        def Nivel1():

                nombres.destroy()
                Nivel1 = Tk()
                Nivel1.title("NIVEL 1")
                Nivel1.geometry("1450x800")

                imagen2 = PhotoImage(file="carretera2.PNG")
                fondo2 = Label(Nivel1,image=imagen2).pack(padx=0,pady=0)
                
                auto1 = PhotoImage(file="coche-jugador1.PNG")
                etiq_auto = Label(Nivel1,image=auto1).place(x=300,y=590)
                

                Nivel1.mainloop()
                

        def Nivel2():

                nombres.destroy()
                Nivel2 = Tk()
                Nivel2.title("NIVEL 2")
                Nivel2.geometry("1450x800")
                

        def Nivel3():

                nombres.destroy()
                Nivel3 = Tk()
                Nivel3.title("NIVEL 3")
                Nivel3.geometry("1450x800")

        def Nivel4():

                nombres.destroy()
                Nivel4 = Tk()
                Nivel4.title("NIVEL 4")
                Nivel4.geometry("1450x800")

        def Nivel5():

                nombres.destroy()
                Nivel5 = Tk()
                Nivel5.title("NIVEL 5")
                Nivel5.geometry("1450x800")
        
        nivel1 = Button(nombres,text="NIVEL 1",command=Nivel1,height=3,width=7).place(x=100,y=300)
        nivel2 = Button(nombres,text="NIVEL 2",command=Nivel2,height=3,width=7).place(x=200,y=300)
        nivel3 = Button(nombres,text="NIVEL 3",command=Nivel3,height=3,width=7).place(x=300,y=300)
        nivel4 = Button(nombres,text="NIVEL 4",command=Nivel4,height=3,width=7).place(x=400,y=300)
        nivel5 = Button(nombres,text="NIVEL 5",command=Nivel5,height=3,width=7).place(x=500,y=300)

        
        nombres.mainloop()



boton1 = Button(menu,text="JUGAR",command=Jugar,height=3,width=8).place(x=100, y=600)

boton2 = Button(menu,text="SALIR",command=menu.destroy,height=3,width=8).place(x=1100, y=600)

titulo.pack(side=TOP, fill=BOTH, expand=True,padx=10,pady=10)

 
menu.mainloop()


            

      
        

        

        
        
    

    
    
