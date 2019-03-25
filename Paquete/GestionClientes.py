import gi
import sqlite3 as dbapi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GestionClientes(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Gestión de Clientes")

        # DECLARO LA VENTANA PRINCIPAL
        self.caixaventana = Gtk.Box(spacing=10)
        self.caixaventana.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.caixaventana.set_margin_left(10)
        self.caixaventana.set_margin_right(10)
        self.caixaventana.set_size_request(400, 300)
        self.set_border_width(10)
        self.add(self.caixaventana)

        self.frameDere = Gtk.Frame()
        self.frameDere.set_label("REGISTRAR")

        # DECLARO LA VENTANA DE CREACIÓN DE CLIENTES

        self.caixaventanaDerecha = Gtk.Box(spacing=10)
        self.caixaventanaDerecha.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.caixaventanaDerecha1 = Gtk.Box(spacing=10)
        self.caixaventanaDerecha1.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaDerecha.add(self.caixaventanaDerecha1)

        self.caixaventanaDerecha2 = Gtk.Box(spacing=10)
        self.caixaventanaDerecha2.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaDerecha.add(self.caixaventanaDerecha2)

        self.frameDere.add(self.caixaventanaDerecha)
        self.caixaventana.add(self.frameDere)

        self.etiquetaDni = Gtk.Label("Dni")
        self.entryDni = Gtk.Entry()

        self.etiquetaNombre = Gtk.Label("Nombre")
        self.entryNombre = Gtk.Entry()

        self.etiquetaApellidos = Gtk.Label("Apellidos")
        self.entryApellidos = Gtk.Entry()

        self.etiquetaSexo = Gtk.Label("Sexo")

        self.cajaRadio = Gtk.Box(spacing=10)
        self.cajaRadio.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoH = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.sexoH.connect("toggled", self.on_button_toggled, "1")

        self.sexoM = Gtk.RadioButton.new_from_widget(self.sexoH)
        self.sexoM.set_label("Mujer")
        self.sexoM.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadio.add(self.sexoH)
        self.cajaRadio.add(self.sexoM)

        self.etiquetaDireccion = Gtk.Label("Direccion")
        self.entryDireccion = Gtk.Entry()

        self.etiquetaTelefono = Gtk.Label("Telefono")
        self.entryTelefono = Gtk.Entry()

        self.etiquetaEmail = Gtk.Label("Email")
        self.entryEmail = Gtk.Entry()

        self.botonCrear = Gtk.Button("Aceptar")

        self.caixaventanaDerecha1.add(self.etiquetaDni)
        self.caixaventanaDerecha1.add(self.entryDni)
        self.caixaventanaDerecha1.add(self.etiquetaNombre)
        self.caixaventanaDerecha1.add(self.entryNombre)
        self.caixaventanaDerecha1.add(self.etiquetaApellidos)
        self.caixaventanaDerecha1.add(self.entryApellidos)
        self.caixaventanaDerecha1.add(self.etiquetaSexo)

        self.caixaventanaDerecha1.add(self.cajaRadio)

        self.caixaventanaDerecha2.add(self.etiquetaDireccion)
        self.caixaventanaDerecha2.add(self.entryDireccion)
        self.caixaventanaDerecha2.add(self.etiquetaTelefono)
        self.caixaventanaDerecha2.add(self.entryTelefono)
        self.caixaventanaDerecha2.add(self.etiquetaEmail)
        self.caixaventanaDerecha2.add(self.entryEmail)

        self.caixaventanaDerecha2.add(self.botonCrear)

        self.botonCrear.connect("clicked", self.on_crear_cliente)

        # DECLARO LA VENTANA DE MODIFICACIÓN DE CLIENTES

        self.frameCentro = Gtk.Frame()
        self.frameCentro.set_label("MODIFICAR")

        self.caixaventanaCentro = Gtk.Box(spacing=10)
        self.caixaventanaCentro.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.caixaventanaCentro1 = Gtk.Box(spacing=10)
        self.caixaventanaCentro1.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaCentro.add(self.caixaventanaCentro1)

        self.caixaventanaCentro2 = Gtk.Box(spacing=10)
        self.caixaventanaCentro2.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaCentro.add(self.caixaventanaCentro2)

        self.frameCentro.add(self.caixaventanaCentro)
        self.caixaventana.add(self.frameCentro)

        self.etiquetaDniM = Gtk.Label("Dni")
        self.entryDniM = Gtk.ListStore(str)

        self.country_combo = Gtk.ComboBox.new_with_model(self.entryDniM)

        self.aux = self.country_combo.connect("changed", self.on_country_combo_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.country_combo.pack_start(self.renderer_text, True)
        self.country_combo.add_attribute(self.renderer_text, "text", 0)

        self.etiquetaNombreM = Gtk.Label("Nombre")
        self.entryNombreM = Gtk.Entry()

        self.etiquetaApellidosM = Gtk.Label("Apellidos")
        self.entryApellidosM = Gtk.Entry()

        self.etiquetaSexoM = Gtk.Label("Sexo")

        self.cajaRadioM = Gtk.Box(spacing=10)
        self.cajaRadioM.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoHM = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.sexoHM.connect("toggled", self.on_button_toggled, "1")

        self.sexoMM = Gtk.RadioButton.new_from_widget(self.sexoHM)
        self.sexoMM.set_label("Mujer")
        self.sexoMM.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadioM.add(self.sexoHM)
        self.cajaRadioM.add(self.sexoMM)

        self.etiquetaDireccionM = Gtk.Label("Dirección")
        self.entryDireccionM = Gtk.Entry()

        self.etiquetaTelefonoM = Gtk.Label("Telefono")
        self.entryTelefonoM = Gtk.Entry()

        self.etiquetaEmailM = Gtk.Label("Email")
        self.entryEmailM = Gtk.Entry()

        self.botonM = Gtk.Button("Aceptar")

        self.caixaventanaCentro1.add(self.etiquetaDniM)
        self.caixaventanaCentro1.add(self.country_combo)
        self.caixaventanaCentro1.add(self.etiquetaNombreM)
        self.caixaventanaCentro1.add(self.entryNombreM)
        self.caixaventanaCentro1.add(self.etiquetaApellidosM)
        self.caixaventanaCentro1.add(self.entryApellidosM)
        self.caixaventanaCentro1.add(self.etiquetaSexoM)

        self.caixaventanaCentro1.add(self.cajaRadioM)

        self.caixaventanaCentro2.add(self.etiquetaDireccionM)
        self.caixaventanaCentro2.add(self.entryDireccionM)
        self.caixaventanaCentro2.add(self.etiquetaTelefonoM)
        self.caixaventanaCentro2.add(self.entryTelefonoM)
        self.caixaventanaCentro2.add(self.etiquetaEmailM)
        self.caixaventanaCentro2.add(self.entryEmailM)

        self.caixaventanaCentro2.add(self.botonM)

        self.botonM.connect("clicked", self.on_modificar_cliente)

        # DECLARO LA VENTANA DE ELIMINACIÓN DE CLIENTES

        self.caixaventanaIzq = Gtk.Box(spacing=10)
        self.caixaventanaIzq.set_orientation(Gtk.Orientation.VERTICAL)

        self.frameIzq = Gtk.Frame()
        self.frameIzq.set_label("ELIMINAR")
        self.frameIzq.add(self.caixaventanaIzq)
        self.caixaventana.add(self.frameIzq)

        self.etiquetaDniE = Gtk.Label("Dni")
        self.entryDniE = Gtk.ListStore(str)
        self.cargar_dni_cliente()

        self.country_comboM = Gtk.ComboBox.new_with_model(self.entryDniE)

        self.aux2 = self.country_comboM.connect("changed", self.on_country_combo_changed2)
        self.renderer_textM = Gtk.CellRendererText()
        self.country_comboM.pack_start(self.renderer_textM, True)
        self.country_comboM.add_attribute(self.renderer_textM, "text", 0)

        self.botonBorrar = Gtk.Button("Borrar cliente")

        self.caixaventanaIzq.add(self.etiquetaDniE)
        self.caixaventanaIzq.add(self.country_comboM)

        self.caixaventanaIzq.add(self.botonBorrar)


        self.botonBorrar.connect("clicked", self.on_borrar_cliente)

    # DECLARO LAS FUNCIONES

    def cargar_dni_cliente(self):
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

            cursor.execute("select dni from clientes")
            self.entryDniM.clear()
            self.entryDniE.clear()
            for rexistro in cursor.fetchall():
                print([rexistro[0]])
                self.entryDniM.append([rexistro[0]])
                self.entryDniE.append([rexistro[0]])


        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("Tratamiento de otra excepción")

        finally:
            cursor.close()
            bbdd.close()

    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.aux = country

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
                sql = "select * from clientes where dni = '" + country + "'"

                cursor.execute(sql)

                for rexistro in cursor.fetchall():
                    self.entryNombreM.set_text(rexistro[1])
                    self.entryApellidosM.set_text(rexistro[2])
                    self.entryDireccionM.set_text(rexistro[4])
                    self.entryTelefonoM.set_text(rexistro[5])
                    self.entryEmailM.set_text(rexistro[6])

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("Tratamiento de otra excepción")

            finally:
                cursor.close()
                bbdd.close()

    def on_country_combo_changed2(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.aux2 = country

    def on_crear_cliente(self, button):

        Dni = self.entryDni.get_text()
        Nombre = self.entryNombre.get_text()
        Apellidos = self.entryApellidos.get_text()

        if (self.sexoH.get_active()):
            Sexo = "H"
        else:
            Sexo = "M"

        Direccion = self.entryDireccion.get_text()
        Telefono = self.entryTelefono.get_text()
        Email = self.entryEmail.get_text()

        if (Dni != "" and Nombre != "" and Apellidos != "" and Sexo != "" and Direccion != "" and Telefono != "" and Email != ""):

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

                # Crear Cliente

                sql = "INSERT INTO clientes (dni,nombre,apellidos,sexo,direccion,telefono,email) VALUES (?, ?, ?, ?, ?, ?, ?)"
                parametros = (Dni, Nombre, Apellidos, Sexo, Direccion, Telefono, Email)

                cursor.execute(sql, parametros)

                bbdd.commit()

                cursor.execute("select * from clientes")

                for rexistro in cursor.fetchall():
                    print(rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5], rexistro[6])

                self.cargar_dni_cliente()

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("Tratamiento de otra excepción")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear el cliente")

    def on_modificar_cliente(self, button):

        Dni = self.aux
        Nombre = self.entryNombreM.get_text()
        Apellidos = self.entryApellidosM.get_text()

        if (self.sexoHM.get_active()):
            Sexo = "H"
        else:
            Sexo = "M"

        Direccion = self.entryDireccionM.get_text()
        Telefono = self.entryTelefonoM.get_text()
        Email = self.entryEmailM.get_text()

        if (Dni != "" and Nombre != "" and Apellidos != "" and Sexo != "" and Direccion != "" and Telefono != "" and Email != ""):

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

                sql = "UPDATE clientes SET nombre = ?, apellidos = ?, sexo = ?, direccion = ?, telefono = ?, email = ? where dni = ?"
                parametros = (Nombre, Apellidos, Sexo, Direccion, Telefono, Email, Dni)

                cursor.execute(sql, parametros)

                bbdd.commit()

                cursor.execute("select * from clientes")

                for rexistro in cursor.fetchall():
                    print(rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5], rexistro[6])

                self.cargar_dni_cliente()

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("Tratamiento de otra excepción")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear el cliente")

    def on_borrar_cliente(self, button):
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

            sql = "DELETE FROM clientes where dni = '" + self.aux2 + "'"

            cursor.execute(sql)
            bbdd.commit()

            self.cargar_dni_cliente()
            print("Eliminado")

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("Tratamiento de otra excepción")

        finally:
            cursor.close()
            bbdd.close()

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
