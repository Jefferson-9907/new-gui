from tkinter import *
import Principal


class StartApp:
    """
        Comprobará si la base de datos ya está conectada, el formulario de pantalal de inicio aparecerá
        de lo contrario le pedirá que conecte la base de datos llamando a la base de datos para la conexión.
    """

    def __init__(self, window):
        self.window = window
        self.window.geometry("0x0+0+0")
        self.window.title("SYST_CONTROL(COMERCIAL DELFINA®)-(CONTROL DE INVENTARIO Y STOCK)")
        self.window.resizable(False, False)

        win = Toplevel()
        Principal.Principal(win)
        self.window.withdraw()
        win.deiconify()


def win():
    window = Tk()
    StartApp(window)
    window.mainloop()


if __name__ == '__main__':
    win()
