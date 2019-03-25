import gi
import sqlite3 as dbapi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GestionCoches(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Gestión de Coches")

        # DECLARO LA VENTANA PRINCIPAL
        self.caixaventana = Gtk.Box(spacing=10)
        self.caixaventana.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.caixaventana.set_margin_left(10)
        self.caixaventana.set_margin_right(10)
        self.caixaventana.set_size_request(400, 300)
        self.set_border_width(10)
        self.add(self.caixaventana)

        # DECLARO LA VENTANA DE CREACIÓN DE COCHES

        self.frameCrear = Gtk.Frame()
        self.frameCrear.set_label("REGISTRAR")

        self.caixaCrear = Gtk.Box(spacing=10)
        self.caixaCrear.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.caixaCrearIzq = Gtk.Box(spacing=10)
        self.caixaCrearIzq.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaCrear.add(self.caixaCrearIzq)

        self.caixaCrearDer = Gtk.Box(spacing=10)
        self.caixaCrearDer.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaCrear.add(self.caixaCrearDer)

        self.frameCrear.add(self.caixaCrear)
        self.caixaventana.add(self.frameCrear)

        # Combo DNI
        self.etiquetaDni = Gtk.Label("Dni del cliente")
        self.entryDni = Gtk.ListStore(str)
        self.cargar_dni_cliente()

        self.country_combo = Gtk.ComboBox.new_with_model(self.entryDni)

        self.country_combo.connect("changed", self.on_country_combo_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.country_combo.pack_start(self.renderer_text, True)
        self.country_combo.add_attribute(self.renderer_text, "text", 0)

        ###

        self.etiquetaId = Gtk.Label("Id")
        self.entryId = Gtk.Entry()

        self.etiquetaNombre = Gtk.Label("Nombre")
        self.entryNombre = Gtk.Entry()

        self.etiquetaMarca = Gtk.Label("Marca")
        self.entryMarca = Gtk.Entry()

        self.etiquetaCombustible = Gtk.Label("Combustible")

        self.cajaRadio = Gtk.Box(spacing=10)
        self.cajaRadio.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.combustibleDiesel = Gtk.RadioButton.new_with_label_from_widget(None, "Diesel")
        self.combustibleDiesel.connect("toggled", self.on_button_toggled, "1")

        self.combustibleGasolina = Gtk.RadioButton.new_from_widget(self.combustibleDiesel)
        self.combustibleGasolina.set_label("Gasolina")
        self.combustibleGasolina.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadio.add(self.combustibleDiesel)
        self.cajaRadio.add(self.combustibleGasolina)

        self.etiquetaModelo = Gtk.Label("Modelo")
        self.entryModelo = Gtk.Entry()

        self.botonCrear = Gtk.Button("Registrar Coche")

        self.caixaCrearIzq.add(self.etiquetaDni)
        self.caixaCrearIzq.add(self.country_combo)
        self.caixaCrearIzq.add(self.etiquetaId)
        self.caixaCrearIzq.add(self.entryId)
        self.caixaCrearIzq.add(self.etiquetaNombre)
        self.caixaCrearIzq.add(self.entryNombre)
        self.caixaCrearDer.add(self.etiquetaMarca)
        self.caixaCrearDer.add(self.entryMarca)
        self.caixaCrearDer.add(self.etiquetaModelo)
        self.caixaCrearDer.add(self.entryModelo)
        self.caixaCrearDer.add(self.etiquetaCombustible)
        self.caixaCrearDer.add(self.cajaRadio)

        self.caixaCrearDer.add(self.botonCrear)

        self.botonCrear.connect("clicked", self.on_crear_coche)

        # DECLARACION CAJA DE MODIFICACION

        self.caixaMod = Gtk.Box(spacing=10)
        self.caixaMod.set_orientation(Gtk.Orientation.VERTICAL)

        self.frameMod = Gtk.Frame()
        self.frameMod.set_label("MODIFICAR")
        self.frameMod.add(self.caixaMod)
        self.caixaventana.add(self.frameMod)

        ##
        self.etiquetaIdM = Gtk.Label("Id")
        self.entryIdM = Gtk.ListStore(str)

        self.country_comboM = Gtk.ComboBox.new_with_model(self.entryIdM)

        self.auxMod = self.country_comboM.connect("changed", self.on_country_combo_changed2)
        self.renderer_textM = Gtk.CellRendererText()
        self.country_comboM.pack_start(self.renderer_textM, True)
        self.country_comboM.add_attribute(self.renderer_textM, "text", 0)

        ##

        self.etiquetaNombreM = Gtk.Label("Nombre")
        self.entryNombreM = Gtk.Entry()

        self.etiquetaMarcaM = Gtk.Label("Marca")
        self.entryMarcaM = Gtk.Entry()

        self.etiquetaCombustibleM = Gtk.Label("Combustible")

        self.cajaRadioM = Gtk.Box(spacing=10)
        self.cajaRadioM.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.combustibleDieselM = Gtk.RadioButton.new_with_label_from_widget(None, "Diesel")
        self.combustibleDieselM.connect("toggled", self.on_button_toggled, "1")

        self.combustibleGasolinaM = Gtk.RadioButton.new_from_widget(self.combustibleDieselM)
        self.combustibleGasolinaM.set_label("Gasolina")
        self.combustibleGasolinaM.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadioM.add(self.combustibleDieselM)
        self.cajaRadioM.add(self.combustibleGasolinaM)

        self.etiquetaModeloM = Gtk.Label("Modelo")
        self.entryModeloM = Gtk.Entry()

        self.botonMod = Gtk.Button("Modificar Coche")

        self.caixaMod.add(self.etiquetaIdM)
        self.caixaMod.add(self.country_comboM)
        self.caixaMod.add(self.etiquetaNombreM)
        self.caixaMod.add(self.entryNombreM)
        self.caixaMod.add(self.etiquetaMarcaM)
        self.caixaMod.add(self.entryMarcaM)
        self.caixaMod.add(self.etiquetaCombustibleM)

        self.caixaMod.add(self.cajaRadioM)

        self.caixaMod.add(self.etiquetaModelo)
        self.caixaMod.add(self.entryModelo)

        self.caixaMod.add(self.botonMod)

        self.botonMod.connect("clicked", self.on_modificar_coche)

        # Declaracion caja eliminar

        self.caixaEliminar = Gtk.Box(spacing=10)
        self.caixaEliminar.set_orientation(Gtk.Orientation.VERTICAL)

        self.frameEliminar = Gtk.Frame()
        self.frameEliminar.set_label("ELIMINAR")
        self.frameEliminar.add(self.caixaEliminar)
        self.caixaventana.add(self.frameEliminar)

        ##
        self.etiquetaIdE = Gtk.Label("Id")
        self.entryIdE = Gtk.ListStore(str)
        self.cargar_id_coche()

        self.country_comboE = Gtk.ComboBox.new_with_model(self.entryIdM)

        self.auxEliminar = self.country_comboE.connect("changed", self.on_country_combo_changed3)
        self.renderer_textE = Gtk.CellRendererText()
        self.country_comboE.pack_start(self.renderer_textE, True)
        self.country_comboE.add_attribute(self.renderer_textE, "text", 0)

        ##
        self.botonEliminar = Gtk.Button("Eliminar Coche")

        self.caixaEliminar.add(self.etiquetaIdE)
        self.caixaEliminar.add(self.country_comboE)
        self.caixaEliminar.add(self.botonEliminar)

        self.botonEliminar.connect("clicked", self.on_borrar_coche)

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
            for rexistro in cursor.fetchall():
                self.entryDni.append([rexistro[0]])

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def cargar_id_coche(self):
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
            cursor.execute("select id from coches")

            self.entryIdM.clear()
            self.entryIdE.clear()
            for rexistro in cursor.fetchall():
                self.entryIdM.append([rexistro[0]])
                self.entryIdE.append([rexistro[0]])

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def on_country_combo_changed(self, combo):

        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.aux = country

    def on_country_combo_changed2(self, combo):

        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.auxMod = country
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

                cursor.execute("select * from coches where id = '" + self.auxMod + "'")

                for rexistro in cursor.fetchall():
                    self.entryNombreM.set_text(rexistro[2])
                    self.entryMarcaM.set_text(rexistro[3])
                    self.entryModeloM.set_text(rexistro[5])

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()

    def on_country_combo_changed3(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.auxEliminar = country

    def on_crear_coche(self, button):

        Id = self.entryId.get_text()
        Dni = self.aux
        Nombre = self.entryNombre.get_text()
        Marca = self.entryMarca.get_text()

        if (self.combustibleDiesel.get_active()):
            Combustible = "Diesel"
        else:
            Combustible = "Gasolina"

        Modelo = self.entryModelo.get_text()


        if(Id != "" and Dni != "" and Nombre != "" and Marca != "" and Combustible != "" and Modelo != ""):

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

                sql = "INSERT INTO coches (id,dni,nombre,marca,combustible,modelo) VALUES (?, ?, ?, ?, ?, ?)"
                parametros = (Id, Dni, Nombre, Marca, Combustible, Modelo)

                cursor.execute(sql, parametros)

                bbdd.commit()

                cursor.execute("select * from coches")

                for rexistro in cursor.fetchall():
                    print(rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5])

                self.cargar_id_coche()

            except dbapi.OperationalError as errorOperacion:

                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                self.entryId.set_text("Inserta otro id diferente")
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear el coche")

    def on_modificar_coche(self, button):

        Id = self.auxMod
        Nombre = self.entryNombreM.get_text()
        Marca = self.entryMarcaM.get_text()

        if (self.combustibleDieselM.get_active()):
            Combustible = "Diesel"
        else:
            Combustible = "Gasolina"

        Modelo = self.entryModeloM.get_text()

        if (Nombre != "" and Marca != "" and Combustible != "" and Modelo != ""):

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

                sql = "UPDATE coches SET nombre = ?, marca = ?, combustible = ?, modelo = ? where id = ?"
                parametros = (Nombre, Marca, Combustible, Modelo, Id)

                cursor.execute(sql, parametros)

                bbdd.commit()

                self.cargar_id_coche()

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear el cliente")

    def on_borrar_coche(self, button):
        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS mascotas
                                                                    (id TEXT PRIMARY KEY,
                                                                     dni TEXT NOT NULL,
                                                                     nombre TEXT NOT NULL,
                                                                     marca TEXT NOT NULL,
                                                                     combustible TEXT NOT NULL,
                                                                     modelo TEXT NOT NULL)
                                                        """)
            sql = "DELETE FROM coches where id = '" + self.auxEliminar + "'"

            cursor.execute(sql)
            bbdd.commit()

            self.cargar_id_coche()
            print("Eliminado")

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def on_button_toggled(self, button, name):

        if button.get_active():
            state = "on"
        else:
            state = "off"