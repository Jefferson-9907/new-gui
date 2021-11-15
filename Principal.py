import random
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox

import pyodbc
import startapp


class Principal:
    """
        Permite al usuario iniciar sesión en el sistema proporcionándoles una interfaz de usuario, verifica el nombre
        de usuario correo electrónico y la contraseña de la tabla no verificada y de administración de la base de datos,
        si el usuario existe, verifique la contraseña y permita que inicien sesión si coincidió, de lo contrario,
        mensaje de error emergente.
    """

    def __init__(self, root):
        """
            Ventana para mostrar todos los atributos y métodos para esta clase
        """
        self.root = root
        self.root.geometry("550x325")
        self.root.title("SYST_CONTROL(COMERCIAL DELFINA®)-(INVENTARIO Y STOCK)")
        self.root.iconbitmap("COM_DELFINA.ico")
        self.root.resizable(False, False)

        imagenes = {
            'save': PhotoImage(file='Guardar1.png'),
            'fondo': PhotoImage(file='FONDO.png')
        }

        # =============================================================
        # FONDO PANTALLA PRINCIPAL
        # =============================================================
        self.fondo = Label(self.root, image=imagenes['fondo'], bg="#003366", fg='White',
                           font=("Cooper Black", 12), compound="left")
        self.fondo.image = imagenes['fondo']
        self.fondo.place(x=0, y=35)


        self.txt = "CONTROL DE INVENTARIO Y STOCK"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 18), bg="#000000",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=650)
        self.slider()
        self.heading_color()

        # ========================================================================
        # ===========================COD. BARRA===================================
        # ========================================================================
        self.cod_b = StringVar()
        self.cant = DoubleVar()
        self.nomb_prod = StringVar()

        self.c_b_label = Label(self.root, text="CÓD. BARRA ", bg="#be1d2c", fg="WHITE",
                               font=("Cooper Black", 11))
        self.c_b_label.place(x=20, y=160)

        self.c_b_entry = Entry(self.root, textvariable=self.cod_b, highlightthickness=0, relief=FLAT,
                               bg="#D3D3D3", fg="#4f4e4d", font=("Cooper Black", 12))
        """self.c_b_entry.bind('<Return>', self.s_name)"""
        self.c_b_entry.place(x=150, y=160, width=250)
        self.c_b_entry.focus()

        """# ========================================================================
        # ======================NOMBRE DEL PRODUCTO===============================
        # ========================================================================

        self.n_b_label = Label(self.root, text="PRODUCTO ", bg="#be1d2c", fg="WHITE",
                               font=("Cooper Black", 11))
        self.n_b_label.place(x=20, y=190)

        self.n_b_entry = Entry(self.root, textvariable=self.nomb_prod, highlightthickness=0, relief=FLAT,
                               bg="#D3D3D3", fg="#4f4e4d", font=("Cooper Black", 12), state='readonly')
        self.n_b_entry.place(x=150, y=190, width=250)"""

        # ========================================================================
        # ===========================CANTIDAD=====================================
        # ========================================================================

        self.cant_label = Label(self.root, text="CANTIDAD ", bg="#be1d2c", fg="WHITE",
                                font=("Cooper Black", 11))
        self.cant_label.place(x=20, y=220)

        self.cant_entry = Entry(self.root, textvariable=self.cant, highlightthickness=0,
                                relief=FLAT, bg="#D3D3D3", fg="#4f4e4d", font=("Cooper Black", 12))
        self.cant_entry.place(x=150, y=220, width=65)

        # ========================================================================
        # ==========================Botón de Guardar==============================
        # ========================================================================

        self.sinc_button = Button(self.root, image=imagenes['save'], text=' SINCRONIZAR STOCK ', bg="#003366",
                                  fg='White', font=("Cooper Black", 12), command=self.validation, compound="left")
        self.sinc_button.image = imagenes['save']
        self.sinc_button.place(x=160, y=250, width=225)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y"

        self.footer0 = Label(self.root, text='', font=("Cooper Black", 9), bg='black',
                            fg='white')                                                                              
        self.footer0.place(x=0, y=285, width=550)
        self.footer = Label(self.root, text='  FECHA Y HORA: ', font=("Cooper Black", 9), bg='black',
                            fg='white')
        self.footer.place(x=0, y=285, width=100)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10), bg='black',
                              fg='white')
        self.footer_1.place(x=110, y=285, width=190)

        self.clock = Label(self.root)
        self.clock['text'] = '00:00:00'
        self.clock['font'] = 'Tahoma 9 bold'
        self.clock['bg'] = 'black'
        self.clock['fg'] = 'white'
        self.clock.place(x=460, y=285)
        self.tic()
        self.tac()

        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=75,
                              bg='#808080', fg='white')
        self.footer_4.place(x=0, y=305, width=550)

    def tic(self):
        self.clock["text"] = strftime("%H:%M:%S %p")

    def tac(self):
        self.tic()
        self.clock.after(1000, self.tac)

    def slider(self):
        """creates slides for heading by taking the text,
        and that text are called after every 100 ms"""
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1

        self.heading.after(100, self.slider)

    def heading_color(self):
        """
        configures heading label
        :return: every 50 ms returned new random color.
        """
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)
    
    """def s_name(self):
        # ========================================================================
        # ======================NOMBRE DEL PRODUCTO===============================
        # ========================================================================
        try:
            self.codigo_barr = self.cod_b.get()

            if self.cod_b.get() == "":
                messagebox.showwarning("SYST_CONTROL(COMERCIAL DELFINA®)-(ADVERTENCIA)", "EL CAMPO: CÓD. BARRAS NO DEBE DE ESTAR VACÍO")
            else:
                self.connection = pyodbc.connect(driver='{SQL Server Native Client 11.0};', server='SERVIDOR',
                                            database='COMDELFINA', trusted_connection='yes')
                self.cursor = self.connection.cursor()

                query = "SELECT * FROM INV_PRODUCTOS WHERE CódigoBarra1='" + self.codigo_barr + "';"
                nomb_tuple = self.cursor.execute(query)

                self.nomb_list = []
                for i in nomb_tuple:
                    data_list_n = str(i[1])

                    self.nomb_prod.set(data_list_n)

                    self.cant_entry.focus()
                

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(COMERCIAL DELFINA®)-(ERROR)", f"NO SE ENCUENTRA CONECTADO A LA BASE DE "
                                                                             f"DATOS DEL SERVIDOR\n"
                                                                             f"VERIFIQUE LA CONEXIÓN {msg}")"""

    def validation(self):
        if self.cod_b.get() == '':
            messagebox.showwarning("SYST_CONTROL(COMERCIAL DELFINA®)-(ADVERTENCIA)",
                                   "INGRESE EL CAMPO: CÓDIGO DE BARRAS")

        elif self.cant.get() == '':
            messagebox.showwarning("SYST_CONTROL(COMERCIAL DELFINA®)-(ADVERTENCIA)", "INGRESE EL CAMPO: CANTIDAD")

        else:
            self.update()

    def update(self):
        try:
            self.connection = pyodbc.connect(driver='{SQL Server Native Client 11.0};', server='SERVIDOR',
                                         database='COMDELFINA', trusted_connection='yes')
            self.cursor = self.connection.cursor()

            query = 'UPDATE INV_PD_BODEGA_STOCK SET Stock =Stock+? FROM INV_PD_BODEGA_STOCK JOIN INV_PRODUCTOS ON INV_PD_BODEGA_STOCK.ProductoID=INV_PRODUCTOS.ID WHERE CódigoBarra1=?'
            values = (self.cant.get(), self.cod_b.get())
            self.cursor.execute(query, values)
            self.connection.commit()
            messagebox.showinfo("SYST_CONTROL(COMERCIAL DELFINA®)-->(ÉXITO)",
                                f"STOCK DEL PRODUCTO CON CÓD. DE BARRA: {self.cod_b.get()}\n"
                                f"HA SIDO ACTUALIZADO DEL REGISTRO")

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    def clear(self):
        self.cod_b.set("")
        self.nomb_prod.set("")
        self.cant.set("")


def win():
    root = Tk()
    Principal(root)
    root.mainloop()


if __name__ == '__main__':
    win()
