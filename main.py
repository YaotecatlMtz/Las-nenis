#Importación de librerías y otros archivos
from datetime import datetime
from almacen import *
from balance import *
from Datos import *
from ajustes import ventana_ajustes
from Hoja_de_personalizacion import *
from tkinter import *
import io

#lectura de archivos
nombre_empresa = open('nombre.txt', 'r')
empresa = nombre_empresa.readline()
nombre_empresa.close()
#Asígnamos el módulo datetime a dt para escribir menos xd 
dt = datetime.now()
#Crear ventana principal
main_window = Tk()
main_window.geometry('900x750')
main_window.configure(bg = Color_de_fondo)
main_window.title('Inicio')
#Sección de textos sin interacción
Fecha = Label(main_window, 
                      text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), 
                      bg = Color_de_fondo,
                      font = (Fuente_titulos, 10)).grid(column = 2)
label2 = Label(main_window, text = empresa,
                       bg = Color_de_fondo, 
                       font = (Fuente_titulos, Tamaño_titulos)).grid(padx = espacio_lateral, pady = espacio_superior)
#Sección de botones
boton_almacen = Button(main_window, 
                               text = ' Almacén ',
                               border = Tamaño_bordes,
                               bg = Color_de_botones, 
                               command = Almacen, 
                               heigh = Altura_botones, 
                               width = Ancho_botones,   
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_balance = Button(main_window, text = ' Registro ',
                               border = Tamaño_bordes,
                               bg = Color_de_botones, 
                               command = ventana_balance,
                               heigh = Altura_botones, 
                               width = Ancho_botones,
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_datos = Button(main_window, text = '  Datos  ',
                             border = Tamaño_bordes,
                             bg = Color_de_botones, 
                             command = Ventana_datos, 
                             heigh = Altura_botones, 
                             width = Ancho_botones,
                             activebackground = botones_activos,
                             cursor = Figura,
                             relief = Tipo_borde,
                             font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_ajustes = Button(main_window, text = ' Ajustes ',
                               bg = Color_de_botones,
                               border = Tamaño_bordes, 
                               command = ventana_ajustes , 
                               heigh = Altura_botones, 
                               width = Ancho_botones,
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_salir = Button(main_window, text = '  Salir  ', 
                             bg = Color_de_botones,
                             border = Tamaño_bordes,
                             command = main_window.destroy, 
                             heigh = Altura_botones, 
                             width = Ancho_botones,
                             activebackground = botones_activos,
                             cursor = Figura,
                             relief = Tipo_borde,
                             font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)

#Lo hacemos un bucle infinito para que no se cierre
main_window.mainloop()