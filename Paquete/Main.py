import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

from Paquete import GestionClientes
from Paquete import GestionCoches
from Paquete import GestionListado
from Paquete import GestionFacturas

class Main(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Principal")

        self.set_border_width(10)

        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('style.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # Declaracion de la caja principal
        caixaventana = Gtk.Box(spacing=2)
        caixaventana.set_orientation(Gtk.Orientation.VERTICAL)
        caixaventana.set_margin_left(10)
        caixaventana.set_margin_right(10)
        caixaventana.set_size_request(200, 150)

        self.add(caixaventana)

        # Declaracion de la caja Superior
        caixaSuperior = Gtk.Box()
        caixaventana.add(caixaSuperior)

        nombretienda = Gtk.Label("Taller Mecanico")
        caixaSuperior.add(nombretienda)

        caixaSuperior.set_margin_bottom(30)

        # Declaracion de la caja Inferior
        caixaInferior = Gtk.Box(spacing=40)
        caixaInferior.set_orientation(Gtk.Orientation.HORIZONTAL)
        caixaInferior.set_size_request(200, 150)

        caixaventana.add(caixaInferior)

        # Declaracion de las cajas separadoras dere e izq
        caixaInferiorDere = Gtk.Box(spacing=40)
        caixaInferiorDere.set_orientation(Gtk.Orientation.VERTICAL)
        caixaInferiorDere.set_size_request(200, 50)

        caixaInferiorIzq = Gtk.Box(spacing=40)
        caixaInferiorIzq.set_orientation(Gtk.Orientation.VERTICAL)
        caixaInferiorIzq.set_size_request(200, 50)

        btnGesCoches = Gtk.Button("Gestión de coches")
        btnGesClientes = Gtk.Button("Gestión de clientes")
        btnGesLista = Gtk.Button("Lista")
        btnGesFacturas = Gtk.Button("Facturas")
        btnGesSalir = Gtk.Button("Salir")

        # Declaracion de los botones
        caixaInferiorDere.add(btnGesClientes)
        caixaInferiorIzq.add(btnGesCoches)
        caixaInferiorDere.add(btnGesLista)
        caixaInferiorIzq.add(btnGesFacturas)
        caixaInferiorIzq.add(btnGesSalir)

        caixaInferior.add(caixaInferiorDere)
        caixaInferior.add(caixaInferiorIzq)

        # Eventos de los botones
        btnGesCoches.connect("clicked", self.on_btn_coches)
        btnGesClientes.connect("clicked", self.on_btn_clientes)
        btnGesLista.connect("clicked", self.on_btn_lista)
        btnGesFacturas.connect("clicked", self.on_btn_facturas)
        btnGesSalir.connect("clicked", self.on_btn_salir)

    def on_btn_coches (self, button):

        GestionCoches.GestionCoches().show_all()

    def on_btn_clientes (self, button):
        GestionClientes.GestionClientes().show_all()

    def on_btn_lista (self, button):
        GestionListado.GestionListado().show_all()

    def on_btn_facturas(self, button):
        GestionFacturas.GestionFacturas().show_all()

    def on_btn_salir (self, button):
        Gtk.main_quit()

Main().connect("delete-event", Gtk.main_quit)
Main().show_all()
Gtk.main()
