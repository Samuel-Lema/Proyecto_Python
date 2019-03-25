import gi
import sqlite3 as dbapi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GestionListado(Gtk.Window):

    '''
    Permite consultar un listado de clientes /coches existentes en la BBDD
    '''

    def __init__(self):
        Gtk.Window.__init__(self, title="Lista General")
        self.set_default_size(250, 100)
        self.set_border_width(10)

        self.cajaVentana = Gtk.Box(spacing=20)
        self.cajaVentana.set_orientation(Gtk.Orientation.VERTICAL)

        self.add(self.cajaVentana)

        ##Tabla Clientes
        self.columnas = ["Dni", "Nombre", "Apellidos", "Sexo", "Direccion", "Telefono", "Email"]
        self.modelo = Gtk.ListStore(str, str, str, str, str, str, str)
        self.axenda = []
        self.vista = Gtk.TreeView(model=self.modelo)

        self.vista.get_selection().connect("changed", self.on_changed)

        self.nombre = Gtk.Label("Registro de Clientes")
        self.cajaVentana.add(self.nombre)
        self.cajaVentana.add(self.vista)

        ##Tabla Coches
        self.columnasM = ["Id", "Dni", "Nombre", "Marca", "Combustible", "Modelo"]
        self.modeloM = Gtk.ListStore(str, str, str, str, str, str)
        self.axendaM = []
        self.vistaM = Gtk.TreeView(model=self.modeloM)
        self.auxiliar = True

        self.nombreM = Gtk.Label("Registro de Coches")
        self.cajaVentana.add(self.nombreM)
        self.cajaVentana.add(self.vistaM)


        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                        (dni TEXT PRIMARY KEY, 
                         nombre TEXT NOT NULL, 
                         apellidos TEXT NOT NULL,
                         sexo TEXT NOT NULL,
                         direccion TEXT NOT NULL, 
                         telefono TEXT NOT NULL,
                         email TEXT NOT NULL)
            """)

            cursor.execute("select * from clientes")

            for rexistro in cursor.fetchall():
                self.axenda.append([rexistro[0] , rexistro[1] , rexistro[2] , rexistro[3] , rexistro[4] , rexistro[5] , rexistro[6]])

            for elemento in self.axenda:
                self.modelo.append(elemento)

            for i in range(len(self.columnas)):
                    celda = Gtk.CellRendererText()
                    self.columna = Gtk.TreeViewColumn(self.columnas[i], celda, text=i)
                    self.vista.append_column(self.columna)

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("Tratamiento de otra excepción")

        finally:
            cursor.close()
            bbdd.close()

    def on_changed(self, selection):
        """
        funcion
        :param selection: 4rff4r
        :return: 43t3
        """

        (model, iter) = selection.get_selected()

        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS coches
                                                    (id TEXT PRIMARY KEY,
                                                     dni TEXT NOT NULL,
                                                     nombre TEXT NOT NULL,
                                                     marca TEXT NOT NULL,
                                                     combustible TEXT NOT NULL,
                                                     modelo TEXT NOT NULL)
                                        """)
            cursor.execute("select * from coches where dni = '" + model[iter][0] + "'")

            self.axendaM.clear()
            for rexistro in cursor.fetchall():
                self.axendaM.append([rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5]])

            self.modeloM.clear()
            for elemento in self.axendaM:
                self.modeloM.append(elemento)

            if (self.auxiliar):
                for i in range(len(self.columnasM)):
                    celda = Gtk.CellRendererText()
                    self.columnaM = Gtk.TreeViewColumn(self.columnasM[i], celda, text=i)
                    self.vistaM.append_column(self.columnaM)
                    self.auxiliar = False

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("Tratamiento de otra excepción")

        finally:
            cursor.close()
            bbdd.close()
        return True