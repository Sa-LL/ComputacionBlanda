from tkinter import *
from pyDatalog import pyDatalog
import Conector

#ventanas

v0 = Tk() # Tk() Es la ventana principal
v1=Toplevel(v0) # Crea una ventana hija

enf1=Toplevel(v1)
enf2=Toplevel(v1)
enf3=Toplevel(v1)
enf4=Toplevel(v1)
enf5=Toplevel(v1)
enf6=Toplevel(v1)
enf7=Toplevel(v1)
enf8=Toplevel(v1)
enf9=Toplevel(v1)
noenf=Toplevel(v1)

v0.protocol("WM_DELETE_WINDOW", "onexit") #deshabilita cerrar
v0.resizable(0,0) #deshabilita el re escalado de la ventana
v1.resizable(0,0)



#Funciones entorno grafico

def mostrar(ventana): ventana.deiconify() # Muestra una ventana
def ocultar(ventana):ventana.withdraw() # Oculta una ventana
def ejecutar(f): v0.after(200,f)# Una forma de ejecutar las funciones
def cerrar(ventana): ventana.quit(), ventana.withdraw()
def mostrarenfermedad():
    S1=sint1.get()
    S2=sint2.get()
    S3=sint3.get()
    S4=sint4.get()
    S5=sint5.get()
    S6=sint6.get()
    S7=sint7.get()
    S8=sint8.get()
    S9=sint9.get()
    S10=sint10.get()
    S11=sint11.get()
    S12=sint12.get()
    S13=sint13.get()
    S14=sint14.get()
    S15=sint15.get()
    S16=sint16.get()
    S17=sint17.get()
    S18=sint18.get()
    S19=sint19.get()
    S20=sint20.get()
    S21=sint21.get()
    S22=sint22.get()
    S23=sint23.get()
    S24=sint24.get()
    S25=sint25.get()
    S26=sint26.get()
    S27=sint27.get()
    S28=sint28.get()
    S29=sint29.get()
    S30=sint30.get()
    S31=sint31.get()
    S32=sint32.get()
    S33=sint33.get()
    S34=sint34.get()
    S35=sint35.get()
    S36=sint36.get()
    
    
    if ((S1 == 1) and (S2 == 1) and (S3 == 1) and (S4 == 1) and (S5==1) and (S6==1) and (S7==1) and (S8==1) and (S9==1)):
        resultado=Conector.usar_regla_enfermedad('enf_1')
        if (resultado == 1):
            enfermedad1 = Label (enf1, text="Usted presenta Tuberculosis Pulmonar").place(x=20,y=20)
            enf1.title("Tuberculosis Pulmonar")
            enf1.geometry("500x100")
            ejecutar(mostrar(enf1))
            
    if (S10 == 1 and S11 == 1 and S12 == 1 and S13 == 1 and S14 == 1): 
        resultado=Conector.usar_regla_enfermedad('enf_2')
        if (resultado == 2):
            enfermedad2 = Label (enf2, text="Usted presenta Aerofagia").place(x=20,y=20)
            enf2.title("Aerofagia")
            enf2.geometry("500x100")
            ejecutar(mostrar(enf2))

    if (S11 == 1 and S15 == 1 and S16 == 1 and S17 == 1 and S18 == 1 and S19 == 1 and S20 == 1 and S5==1): 
        resultado=Conector.usar_regla_enfermedad('enf_3')
        if (resultado == 3):
            enfermedad3 = Label (enf3, text="Usted presenta Apendicitis").place(x=20,y=20)
            enf3.title("Apendicitis")
            enf3.geometry("500x100")
            ejecutar(mostrar(enf3))

    if (S21 == 1 and S22 == 1 and S23 == 1 and S24==1 and S5 == 1 and S16==1 and S19==1): 
        resultado=Conector.usar_regla_enfermedad('enf_4')
        if (resultado == 4):
            enfermedad4 = Label (enf4, text="Usted presenta Pancreatitis").place(x=20,y=20)
            enf4.title("Pancreatitis")
            enf4.geometry("500x100")
            ejecutar(mostrar(enf4))
    if (S3 == 1 and S5 == 1 and S25 == 1 and S26 == 1): 
        resultado=Conector.usar_regla_enfermedad('enf_5')
        if (resultado == 5):
            enfermedad5 = Label (enf5, text="Usted presenta Bronquitis.").place(x=20,y=20)
            enf5.title("Bronquitis")
            enf5.geometry("500x100")
            ejecutar(mostrar(enf5))
    if (S27 == 1 and S28 == 1 and S29 == 1 and S30 == 1 and S31==1 and S5==1): 
        resultado=Conector.usar_regla_enfermedad('enf_6')
        if (resultado == 6):
            enfermedad6 = Label (enf6, text="Usted presenta Dengue").place(x=20,y=20)
            enf6.title("Dengue")
            enf6.geometry("500x100")
            ejecutar(mostrar(enf6))
    if (S32 == 1 and S3 == 1 and S1 == 1 and S23 == 1 and S5==1): 
        resultado=Conector.usar_regla_enfermedad('enf_7')
        if (resultado == 7):
            enfermedad7 = Label (enf7, text="Usted presenta Derrame Pleural").place(x=20,y=20)
            enf7.title("Derrame Pleural")
            enf7.geometry("500x100")
            ejecutar(mostrar(enf7))
    if (S33 == 1 and S34 == 1 and S35 == 1 and S36 == 1 and S5 == 1): 
        resultado=Conector.usar_regla_enfermedad('enf_8')
        if (resultado == 8):
            enfermedad8 = Label (enf8, text="Usted presenta Encefalitis").place(x=20,y=20)
            enf8.title("Encefalitis")
            enf8.geometry("500x100")
            ejecutar(mostrar(enf8))
        

# V-main

v0.config(bg="white")
v0.geometry("600x400")
v0.title("Sistema Experto Enfermedades")
fondo=PhotoImage(file="618568_1.gif")
lblImageFondo=Label(v0,image=fondo).place(x=0,y=0)


#consultas

v1.config(bg="white")
v1.geometry("800x600")
v1.title("Consultas")
consultas=PhotoImage(file="2.gif")
lblImageFondo=Label(v1,image=consultas).place(x=0,y=0)


 
b1=Button(v0,text="Consultas",command=lambda: ejecutar(mostrar(v1)), font="impact") # Primer botón
b1.place(x=270,y=150) # El botón es cargado

b3=Button(v1,text="Ocultar",command=lambda: ejecutar(ocultar(v1)), font="impact")
b3.place(x=743,y=567)

 
b5=Button(v0,text="SALIR",command=lambda: ejecutar(cerrar(v0)), font="impact")
b5.place(x=287,y=350)
####################################################################################################
b5=Button(v1,text="Aceptar",command=lambda: ejecutar(mostrarenfermedad()), font="impact")
b5.place(x=0,y=567)


sint1=IntVar()
Si1=Checkbutton(v1, text="Dificultad respiratoria", variable=sint1, onvalue=1, offvalue=0).place(x=60,y=110)

sint2=IntVar()
Si2=Checkbutton(v1, text="Dolor en el pecho", variable=sint2, onvalue=1, offvalue=0).place(x=60,y=160)

sint3=IntVar()
Si3=Checkbutton(v1, text="Tos", variable=sint3, onvalue=1, offvalue=0).place(x=60,y=210)

sint4=IntVar()
Si4=Checkbutton(v1, text="Expectoración con sangre", variable=sint4, onvalue=1, offvalue=0).place(x=60,y=260)

sint5=IntVar()
Si5=Checkbutton(v1, text="Fiebre", variable=sint5, onvalue=1, offvalue=0).place(x=60,y=310)

sint6=IntVar()
Si6=Checkbutton(v1, text="Sudoración excesiva", variable=sint6, onvalue=1, offvalue=0).place(x=60,y=360)

sint7=IntVar()
Si7=Checkbutton(v1, text="Fatiga", variable=sint7, onvalue=1, offvalue=0).place(x=60,y=410)

sint8=IntVar()
Si8=Checkbutton(v1, text="Pérdida de peso", variable=sint8, onvalue=1, offvalue=0).place(x=60,y=460)

sint9=IntVar()
Si9=Checkbutton(v1, text="Sibilancias", variable=sint9, onvalue=1, offvalue=0).place(x=60,y=510)

sint10=IntVar()
Si10=Checkbutton(v1, text="Distensión abdominal", variable=sint10, onvalue=1, offvalue=0).place(x=240,y=110)

sint11=IntVar()
Si11=Checkbutton(v1, text="Dolor abdominal", variable=sint11, onvalue=1, offvalue=0).place(x=240,y=160)

sint12=IntVar()
Si12=Checkbutton(v1, text="Ruidos intestinales", variable=sint12, onvalue=1, offvalue=0).place(x=240,y=210)

sint13=IntVar()
Si13=Checkbutton(v1, text="Eructos", variable=sint13, onvalue=1, offvalue=0).place(x=240,y=260)

sint14=IntVar()
Si14=Checkbutton(v1, text="Meteorismo", variable=sint14, onvalue=1, offvalue=0).place(x=240,y=310)

sint15=IntVar()
Si15=Checkbutton(v1, text="Escalofríos", variable=sint15, onvalue=1, offvalue=0).place(x=240,y=360)

sint16=IntVar()
Si16=Checkbutton(v1, text="Vómitos", variable=sint16, onvalue=1, offvalue=0).place(x=240,y=410)

sint17=IntVar()
Si17=Checkbutton(v1, text="Temblores", variable=sint17, onvalue=1, offvalue=0).place(x=240,y=460)

sint18=IntVar()
Si18=Checkbutton(v1, text="Estreñimiento", variable=sint18, onvalue=1, offvalue=0).place(x=240,y=510)

sint19=IntVar()
Si19=Checkbutton(v1, text="Náuseas", variable=sint19, onvalue=1, offvalue=0).place(x=420,y=110)

sint20=IntVar()
Si20=Checkbutton(v1, text="Falta de apetito", variable=sint20, onvalue=1, offvalue=0).place(x=420,y=160)

sint21=IntVar()
Si21=Checkbutton(v1, text="Sudoración", variable=sint21, onvalue=1, offvalue=0).place(x=420,y=210)

sint22=IntVar()
Si22=Checkbutton(v1, text="Abdomen lleno de gases", variable=sint22, onvalue=1, offvalue=0).place(x=420,y=260)

sint23=IntVar()
Si23=Checkbutton(v1, text="Hipo", variable=sint23, onvalue=1, offvalue=0).place(x=420,y=310)

sint24=IntVar()
Si24=Checkbutton(v1, text="Indigestión", variable=sint24, onvalue=1, offvalue=0).place(x=420,y=360)

sint25=IntVar()
Si25=Checkbutton(v1, text="Mucosidad con salida oral", variable=sint25, onvalue=1, offvalue=0).place(x=420,y=410)

sint26=IntVar()
Si26=Checkbutton(v1, text="Dificultad respiratoria", variable=sint26, onvalue=1, offvalue=0).place(x=420,y=460)

sint27=IntVar()
Si27=Checkbutton(v1, text="Erupción en la piel", variable=sint27, onvalue=1, offvalue=0).place(x=420,y=510)

sint28=IntVar()
Si28=Checkbutton(v1, text="Sangre en las encías", variable=sint28, onvalue=1, offvalue=0).place(x=600,y=110)

sint29=IntVar()
Si29=Checkbutton(v1, text="Debilidad general", variable=sint29, onvalue=1, offvalue=0).place(x=600,y=160)

sint30=IntVar()
Si30=Checkbutton(v1, text="Dolor muscular", variable=sint30, onvalue=1, offvalue=0).place(x=600,y=210)

sint31=IntVar()
Si31=Checkbutton(v1, text="Dolor de garganta", variable=sint31, onvalue=1, offvalue=0).place(x=600,y=260)

sint32=IntVar()
Si32=Checkbutton(v1, text="Dolor torácico", variable=sint32, onvalue=1, offvalue=0).place(x=600,y=310)

sint33=IntVar()
Si33=Checkbutton(v1, text="Convulsiones", variable=sint33, onvalue=1, offvalue=0).place(x=600,y=360)

sint34=IntVar()
Si34=Checkbutton(v1, text="Dolor de cabeza", variable=sint34, onvalue=1, offvalue=0).place(x=600,y=410)

sint35=IntVar()
Si35=Checkbutton(v1, text="Apatía", variable=sint35, onvalue=1, offvalue=0).place(x=600,y=460)

sint36=IntVar()
Si36=Checkbutton(v1, text="Confusión", variable=sint36, onvalue=1, offvalue=0).place(x=600,y=510)


 
v1.withdraw() # Oculta la ventana v1
enf1.withdraw()
enf2.withdraw()
enf3.withdraw()
enf4.withdraw()
enf5.withdraw()
enf6.withdraw()
enf7.withdraw()
enf8.withdraw()
enf9.withdraw()
noenf.withdraw()


v0.mainloop() # Es el evento que llama al inicio de nuestro programa. Siempre lo lleva la ventana principal.

