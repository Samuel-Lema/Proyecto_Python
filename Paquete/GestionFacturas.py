import sqlite3 as dbapi

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Spacer, Table, TableStyle)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class GestionFacturas(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Gestión de Facturas")

        # DECLARO LA VENTANA PRINCIPAL
        self.caixaventana = Gtk.Box(spacing=10)
        self.caixaventana.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.caixaventana.set_margin_left(10)
        self.caixaventana.set_margin_right(10)
        self.set_border_width(10)
        self.add(self.caixaventana)

        # DECLARO LA VENTANA DE FACTURACIÓN DE COCHES

        self.frameCrear = Gtk.Frame()
        self.frameCrear.set_label("FACTURAR")

        self.caixaCrear = Gtk.Box(spacing=10)
        self.caixaCrear.set_orientation(Gtk.Orientation.VERTICAL)

        self.frameCrear.add(self.caixaCrear)
        self.caixaventana.add(self.frameCrear)

        # COMBO DNI CLIENTE
        self.etiquetaDni = Gtk.Label("Dni del cliente")
        self.comboCliente = Gtk.ComboBoxText()
        self.comboCliente.set_entry_text_column(0)
        self.cargar_dni_cliente()
        self.comboCliente.connect("changed", self.on_country_combo_changed)

        # COMBO ID COCHE

        self.etiquetaIdM = Gtk.Label("ID del Coche")
        self.comboCoche = Gtk.ComboBoxText()
        self.comboCoche.set_entry_text_column(0)
        self.comboCoche.connect("changed", self.on_country_combo_changed2)

        # INPUT NOMBRE FACTURA

        self.etiquetaPrecio = Gtk.Label("Precio")
        self.entryPrecio = Gtk.Entry()

        # INPUT NOMBRE FACTURA

        self.etiquetaFactura = Gtk.Label("ID de Factura")
        self.entryFactura = Gtk.Entry()

        self.botonCrear = Gtk.Button("Facturar")

        self.caixaCrear.add(self.etiquetaDni)
        self.caixaCrear.add(self.comboCliente)
        self.caixaCrear.add(self.etiquetaIdM)
        self.caixaCrear.add(self.comboCoche)
        self.caixaCrear.add(self.etiquetaPrecio)
        self.caixaCrear.add(self.entryPrecio)
        self.caixaCrear.add(self.etiquetaFactura)
        self.caixaCrear.add(self.entryFactura)
        self.caixaCrear.add(self.botonCrear)

        self.botonCrear.connect("clicked", self.on_crear_factura)

    def cargar_dni_cliente(self):

        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()

        try:
            cursor.execute("select dni from clientes")

            for rexistro in cursor.fetchall():
                self.comboCliente.append_text(rexistro[0])

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
            cursor.execute("select id from coches where dni = '" + self.comboCliente.get_active_text() + "'")

            self.comboCoche.remove_all()

            for rexistro in cursor.fetchall():
                self.comboCoche.append_text(rexistro[0])

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

        self.cargar_id_coche()

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

                # for rexistro in cursor.fetchall():
                #   self.entryNombreM.set_text(rexistro[2])
                #  self.entryMarcaM.set_text(rexistro[3])
                # self.entryModeloM.set_text(rexistro[5])

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()

    def on_crear_factura(self, button):

        try:
            bbdd = dbapi.connect("BaseClientes.dat")
            cursor = bbdd.cursor()

            facturas = []

            detalleFactura = []

            cursorCliente = cursor.execute("select * from clientes where dni = '" + self.comboCliente.get_active_text() + "'")

            rexistroCliente = cursorCliente.fetchone()

            detalleFactura.append(['Nome', rexistroCliente[1] + ' ' + rexistroCliente[2], '', '', ''])

            detalleFactura.append(['Dirección', rexistroCliente[4], '', '', ''])
            
            detalleFactura.append(['Telefono', rexistroCliente[5], '', '', ''])
            
            detalleFactura.append(['Email', rexistroCliente[6], '', '', ''])

            cursorCoches = cursor.execute("select * from coches where id = '" + self.comboCoche.get_active_text() + "'")

            rexistroCoche = cursorCoches.fetchone()

            cantidade = 1

            prezoTotal = self.entryPrecio.get_text()

            # TABLA DE PRECIOS

            detalleFactura.append(['','', '', '', ''])

            detalleFactura.append(["Código producto", "Descripción", "Cantidade", "Prezo unitario", "Prezo"])

            detalleFactura.append([rexistroCoche[2], "Reparación\nEstandar", cantidade, prezoTotal, prezoTotal * cantidade])

            detalleFactura.append(["", "", "", "Prezo total:", prezoTotal * cantidade])

            facturas.append(list(detalleFactura))

            detalleFactura.clear()

        finally:

            print("Factura generada")

            cursor.close()

            bbdd.close()

        doc = SimpleDocTemplate("../Facturas/" + self.entryFactura.get_text() + "", pagesize=A4)

        guion = []

        for factura in facturas:

            taboa = Table(factura, colWidths=80, rowHeights=30)

            taboa.setStyle(TableStyle([

                ('TEXTCOLOR', (0, 0), (-1, 3), colors.blue),

                ('TEXTCOLOR', (0, 6), (-1, -1), colors.green),

                ('BACKGROUND', (0, 7), (-1, -1), colors.lightcyan),

                ('ALIGN', (2, 5), (-1, -1), 'RIGHT'),

                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

                ('BOX', (0, 0), (-1, 3), 1, colors.black),

                ('BOX', (0, 5), (-1, -2), 1, colors.black),

                ('INNERGRID', (0, 5), (-1, -2), 0.5, colors.grey)

            ]))

        guion.append(taboa)

        guion.append(Spacer(0, 40))

        guion.append(PageBreak())

        doc.build(guion)

def on_button_toggled(self, button, name):

    if button.get_active():
        state = "on"
    else:
        state = "off"
