from tkinter import *
import pickle
from Persona import *
from tkinter import messagebox

listaPersonas = []

raiz = Tk()
raiz.title("Ejercicio de Interfaz")
raiz.resizable(False, False)

miFrame = Frame(raiz, width = "700", height = "350")
miFrame.pack()

miNombre = StringVar()
miApellido = StringVar()
miDireccion = StringVar()
miEdad = IntVar()

lblNombre = Label(miFrame, text = "Nombre: ").place(x = 100, y = 40)
txtNombre = Entry(miFrame, textvariable = miNombre)
txtNombre.place(x = 160, y = 40)

lblApellido = Label(miFrame, text = "Apellido: ").place(x = 100, y = 65)
txtApellido = Entry(miFrame,textvariable = miApellido)
txtApellido.place(x = 160, y = 65)

lblDireccion = Label(miFrame, text = "Dirección: ").place(x = 100, y = 90)
txtDireccion = Entry(miFrame, textvariable = miDireccion)
txtDireccion.place(x = 160, y = 90)

lblEdad = Label(miFrame, text = "Edad: ").place(x = 100, y = 115)
txtEdad = Entry(miFrame, textvariable = miEdad)
txtEdad.place(x = 160, y = 115)

list = Listbox(miFrame, width = 50, height = 7)
list.place(x = 350, y = 35)

def Anadir():
    nombre = miNombre.get()
    apellido = miApellido.get()
    direccion = miDireccion.get()
    edad = int(txtEdad.get())
    a = Persona(nombre, apellido, direccion, edad)
    listaPersonas.append(a)
    list.delete(0, END)
    list.insert(END, *listaPersonas)

btnAnadir = Button(miFrame, text = "Añadir", command= Anadir).place(x = 100, y = 200)

def Borrar():
    respuesta = messagebox.askyesno("Borrar usuario", "¿Estás seguro de quieres eliminar los datos seleccionados?")
    if respuesta == True:
        posicion = list.curselection()[0]
        list.delete(posicion)
        del listaPersonas[posicion]

btnBorrar = Button(miFrame, text = "Borrar", command= Borrar).place(x = 150, y = 200)

def Modificar():
    respuesta = messagebox.askyesno("Modificar", "¿Quieres modificar los datos seleccionados?")
    if respuesta == True:
        posicion = list.curselection()[0]
        a = listaPersonas[posicion]

        a.set_nombre(miNombre.get())
        a.set_apellido(miApellido.get())
        a.set_direccion(miDireccion.get())
        a.set_edad(miEdad.get())

        list.delete(0, END)
        list.insert(END, *listaPersonas)

btnModificar = Button(miFrame, text = "Modificar", command= Modificar).place(x = 200, y = 200)

def Consultar():
    posicion = list.curselection()[0]
    a = listaPersonas[posicion]

    txtNombre.delete(0, END)
    txtNombre.insert(0, a.get_nombre())

    txtApellido.delete(0, END)
    txtApellido.insert(0, a.get_apellido())

    txtDireccion.delete(0, END)
    txtDireccion.insert(0, a.get_direccion())

    txtEdad.delete(0, END)
    txtEdad.insert(0, a.get_edad())

btnConsultar = Button(miFrame, text = "Consultar", command= Consultar).place(x = 270, y = 200)

def Importar():
    fichero_binario = open("listaPersonas", "rb")
    listaPersonas = pickle.load(fichero_binario)
    list.delete(0, END)
    list.insert(END, *listaPersonas)
    fichero_binario.close()

btnImportar = Button(miFrame, text = "Importar", command= Importar).place(x = 430, y = 160)
def Exportar():
    fichero_binario = open("listaPersonas", "wb")
    pickle.dump(listaPersonas, fichero_binario)
    fichero_binario.close()

btnExportar = Button(miFrame, text = "Exportar", command= Exportar).place(x = 500, y = 160)

raiz.mainloop()