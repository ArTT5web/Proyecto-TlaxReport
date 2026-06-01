#TlaxReport
#Versión 6.0
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

contador = 0

nombre = [""] * 100
direc = [""] * 100
descrip= [""] * 100
tipoDenuncia = [""] * 100

def hacer_denuncia():
    global contador

    opcion = simpledialog.askinteger(
        "=Tipo de denuncia=",
        "1. Baches\n"
        "2. Alumbrado público\n"
        "3. Fuga de agua\n"
        "4. Semáforos\n"
        "5. Fuga de gas"
    )

    if opcion is None:
        return

    contador += 1
    if opcion == 1:
        tipoDenuncia[contador] = "Baches"

    elif opcion == 2:
        subopc = simpledialog.askinteger(
            "=Alumbrado público="
            "1. Falta de Akumbrado\n"
            "2. Mantenimiento de Alumbrado"
        )
        if subopc == 1:
            tipoDenuncia[contador] = "Falta de Alumbrado"
        elif subopc == 2:
            tipoDenuncia[contador]
