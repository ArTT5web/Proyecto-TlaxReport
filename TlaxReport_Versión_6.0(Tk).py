# Proyecto TlaxReport
# Versión 6.0

import tkinter as tk
from tkinter import messagebox

contador = 0

nombre = [""] * 100
direc = [""] * 100
descrip = [""] * 100
tipoDenuncia = [""] * 100


def guardar_denuncia():

    global contador

    if contador >= 100:
        messagebox.showwarning(
            "Límite alcanzado",
            "No se pueden registrar más denuncias"
        )
        return

    if anonima.get() == 1:
        nombre[contador] = "ANONIMO"
    else:
        nombre[contador] = entrada_nombre.get()

    direc[contador] = entrada_direccion.get()
    descrip[contador] = entrada_descripcion.get()

    tipo = opcion_tipo.get()

    if tipo == "1":
        tipoDenuncia[contador] = "Baches"

    elif tipo == "2":
        tipoDenuncia[contador] = "Falta de Alumbrado"

    elif tipo == "3":
        tipoDenuncia[contador] = "Mantenimiento de Alumbrado"

    elif tipo == "4":
        tipoDenuncia[contador] = "Fuga de agua"

    elif tipo == "5":
        tipoDenuncia[contador] = "Faltan Semáforos"

    elif tipo == "6":
        tipoDenuncia[contador] = "Mantenimiento de Semáforos"

    elif tipo == "7":
        tipoDenuncia[contador] = "Fuga de gas"

    else:
        messagebox.showerror(
            "Error",
            "Seleccione un tipo válido (1 al 7)"
        )
        return

    contador += 1

    messagebox.showinfo(
        "Registro",
        "Denuncia guardada correctamente"
    )

    entrada_nombre.delete(0, tk.END)
    entrada_direccion.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)
    opcion_tipo.delete(0, tk.END)


def mostrar_denuncias():

    texto = ""

    if contador == 0:

        texto = "No hay denuncias registradas"

    else:

        for i in range(contador):

            texto += "Denuncia " + str(i + 1) + "\n"
            texto += "Nombre: " + nombre[i] + "\n"
            texto += "Dirección: " + direc[i] + "\n"
            texto += "Descripción: " + descrip[i] + "\n"
            texto += "Tipo: " + tipoDenuncia[i] + "\n\n"

    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, texto)


def buscar_nombre():

    buscar = entrada_buscar_nombre.get()

    for i in range(contador):

        if nombre[i].upper() == buscar.upper():

            texto = (
                "Nombre: " + nombre[i] +
                "\nDirección: " + direc[i] +
                "\nDescripción: " + descrip[i] +
                "\nTipo: " + tipoDenuncia[i]
            )

            resultado.delete("1.0", tk.END)
            resultado.insert(tk.END, texto)

            return

    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, "No encontrada")


def buscar_tipo():

    tipo = entrada_buscar_tipo.get()

    if tipo == "1":
        tipo = "Baches"

    elif tipo == "2":
        tipo = "Falta de Alumbrado"

    elif tipo == "3":
        tipo = "Mantenimiento de Alumbrado"

    elif tipo == "4":
        tipo = "Fuga de agua"

    elif tipo == "5":
        tipo = "Faltan Semáforos"

    elif tipo == "6":
        tipo = "Mantenimiento de Semáforos"

    elif tipo == "7":
        tipo = "Fuga de gas"

    texto = ""

    for i in range(contador):

        if tipoDenuncia[i].upper() == tipo.upper():

            texto += (
                "Nombre: " + nombre[i] +
                "\nDirección: " + direc[i] +
                "\nDescripción: " + descrip[i] +
                "\nTipo: " + tipoDenuncia[i] +
                "\n\n"
            )

    if texto == "":
        texto = "No encontrada"

    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, texto)


def estadisticas():

    texto = ""

    texto += "Baches: " + str(tipoDenuncia.count("Baches")) + "\n"
    texto += "Falta de Alumbrado: " + str(tipoDenuncia.count("Falta de Alumbrado")) + "\n"
    texto += "Mantenimiento de Alumbrado: " + str(tipoDenuncia.count("Mantenimiento de Alumbrado")) + "\n"
    texto += "Fuga de agua: " + str(tipoDenuncia.count("Fuga de agua")) + "\n"
    texto += "Faltan Semáforos: " + str(tipoDenuncia.count("Faltan Semáforos")) + "\n"
    texto += "Mantenimiento de Semáforos: " + str(tipoDenuncia.count("Mantenimiento de Semáforos")) + "\n"
    texto += "Fuga de gas: " + str(tipoDenuncia.count("Fuga de gas"))

    messagebox.showinfo(
        "Estadísticas",
        texto
    )


ventana = tk.Tk()

ventana.title("TlaxReport")
ventana.geometry("650x750")
ventana.configure(bg="#C8A2C8")

tk.Label(
    ventana,
    text="TLAXREPORT",
    font=("Arial", 16, "bold"),
    bg="#C8A2C8"
).pack(pady=10)

tk.Label(
    ventana,
    text="Sistema de Denuncias Ciudadanas",
    bg="#C8A2C8"
).pack(pady=5)

tk.Label(
    ventana,
    text="Tipos de denuncia:",
    bg="#C8A2C8"
).pack(pady=5)

tk.Label(
    ventana,
    text="1-Baches\n"
         "2-Falta de Alumbrado\n"
         "3-Mantenimiento de Alumbrado\n"
         "4-Fuga de agua\n"
         "5-Faltan Semáforos\n"
         "6-Mantenimiento de Semáforos\n"
         "7-Fuga de gas",
    bg="#C8A2C8"
).pack(pady=5)

opcion_tipo = tk.Entry(ventana)
opcion_tipo.pack(pady=5)

tk.Label(
    ventana,
    text="Nombre",
    bg="#C8A2C8"
).pack(pady=5)

entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack(pady=5)

anonima = tk.IntVar()

tk.Checkbutton(
    ventana,
    text="Realizar denuncia anónima",
    variable=anonima,
    bg="#C8A2C8"
).pack(pady=5)

tk.Label(
    ventana,
    text="Dirección",
    bg="#C8A2C8"
).pack(pady=5)

entrada_direccion = tk.Entry(ventana, width=40)
entrada_direccion.pack(pady=5)

tk.Label(
    ventana,
    text="Descripción",
    bg="#C8A2C8"
).pack(pady=5)

entrada_descripcion = tk.Entry(ventana, width=40)
entrada_descripcion.pack(pady=5)

tk.Button(
    ventana,
    text="Guardar Denuncia",
    command=guardar_denuncia
).pack(pady=10)

tk.Label(
    ventana,
    text="Buscar por nombre",
    bg="#C8A2C8"
).pack(pady=5)

entrada_buscar_nombre = tk.Entry(ventana, width=40)
entrada_buscar_nombre.pack(pady=5)

tk.Button(
    ventana,
    text="Buscar Nombre",
    command=buscar_nombre
).pack(pady=5)

tk.Label(
    ventana,
    text="Buscar por tipo",
    bg="#C8A2C8"
).pack(pady=5)

entrada_buscar_tipo = tk.Entry(ventana, width=40)
entrada_buscar_tipo.pack(pady=5)

tk.Button(
    ventana,
    text="Buscar Tipo",
    command=buscar_tipo
).pack(pady=5)

tk.Button(
    ventana,
    text="Mostrar Denuncias",
    command=mostrar_denuncias
).pack(pady=5)

tk.Button(
    ventana,
    text="Estadísticas",
    command=estadisticas
).pack(pady=5)

tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy
).pack(pady=10)

resultado = tk.Text(
    ventana,
    width=70,
    height=12
)

resultado.pack(pady=15)

ventana.mainloop()
