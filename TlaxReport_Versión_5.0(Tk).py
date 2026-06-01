#Proyecto TlaxReport
#Versión 5.0
import tkinter as tk

contador = 0

nombre = [""] * 100
direc = [""] * 100
descrip = [""] * 100
tipoDenuncia = [""] * 100


def guardar_denuncia():

    global contador

    contador += 1

    nombre[contador] = entrada_nombre.get()
    direc[contador] = entrada_direccion.get()
    descrip[contador] = entrada_descripcion.get()

    tipo = opcion_tipo.get()

    if tipo == "1":
        tipoDenuncia[contador] = "Baches"

    elif tipo == "2":
        tipoDenuncia[contador] = "Falta de Alumbrado"

    elif tipo == "3":
        tipoDenuncia[contador] = "Fuga de agua"

    elif tipo == "4":
        tipoDenuncia[contador] = "Faltan Semáforos"

    elif tipo == "5":
        tipoDenuncia[contador] = "Fuga de gas"

    resultado.config(text="Reporte guardado")

    entrada_nombre.delete(0, tk.END)
    entrada_direccion.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)


def mostrar_denuncias():

    texto = ""

    if contador == 0:

        texto = "No hay denuncias"

    else:

        for i in range(1, contador + 1):

            texto += "Denuncia " + str(i) + "\n"
            texto += "Nombre: " + nombre[i] + "\n"
            texto += "Dirección: " + direc[i] + "\n"
            texto += "Descripción: " + descrip[i] + "\n"
            texto += "Tipo: " + tipoDenuncia[i] + "\n\n"

    resultado.config(text=texto)


def buscar_nombre():

    buscar = entrada_buscar_nombre.get()

    for i in range(1, contador + 1):

        if nombre[i] == buscar:

            resultado.config(
                text="Nombre: " + nombre[i] +
                "\nDirección: " + direc[i] +
                "\nDescripción: " + descrip[i]
            )

            return

    resultado.config(text="No encontrada")


def buscar_tipo():

    tipo = entrada_buscar_tipo.get()

    for i in range(1, contador + 1):

        if tipoDenuncia[i] == tipo:

            resultado.config(
                text="Nombre: " + nombre[i] +
                "\nTipo: " + tipoDenuncia[i]
            )

            return

    resultado.config(text="No encontrada")


ventana = tk.Tk()

ventana.title("TlaxReport")
ventana.geometry("600x700")

tk.Label(
    ventana,
    text="Hacer una denuncia"
).pack()

tk.Label(
    ventana,
    text="1-Baches  2-Alumbrado  3-Fuga Agua  4-Semáforos  5-Fuga Gas"
).pack()

opcion_tipo = tk.Entry(ventana)
opcion_tipo.pack()

tk.Label(
    ventana,
    text="Nombre"
).pack()

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(
    ventana,
    text="Dirección"
).pack()

entrada_direccion = tk.Entry(ventana)
entrada_direccion.pack()

tk.Label(
    ventana,
    text="Descripción"
).pack()

entrada_descripcion = tk.Entry(ventana)
entrada_descripcion.pack()

tk.Button(
    ventana,
    text="Guardar Denuncia",
    command=guardar_denuncia
).pack()

tk.Label(
    ventana,
    text="Buscar por nombre"
).pack()

entrada_buscar_nombre = tk.Entry(ventana)
entrada_buscar_nombre.pack()

tk.Button(
    ventana,
    text="Buscar Nombre",
    command=buscar_nombre
).pack()

tk.Label(
    ventana,
    text="Buscar por tipo"
).pack()

entrada_buscar_tipo = tk.Entry(ventana)
entrada_buscar_tipo.pack()

tk.Button(
    ventana,
    text="Buscar Tipo",
    command=buscar_tipo
).pack()

tk.Button(
    ventana,
    text="Mostrar Denuncias",
    command=mostrar_denuncias
).pack()

tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy
).pack()

resultado = tk.Label(
    ventana,
    text="",
    justify="left"
)

resultado.pack()

ventana.mainloop()
