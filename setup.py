from distutils.core import setup

#ficheiros= ["Cousas/*"]
setup(name = "Proyecto de Taller Mecanico",
      version="1.0",
      description="Aplicacion de exemplo de distribucion",
      long_description="""Descripcion en mais dunha liña
      extensa da aplicacion""",
      author="Samuel Lema",
      author_email="slemagonzalez@danielcastelao.org",
      url="www.urldoproxecto.es",
      keywords="Proba, distribuicion, exemplo",
      platforms="linux",
      packages=['Paquete'],
      scripts=["Lanzador"],
      #py_modulos= ["moduloProbraModulo"]
      #install_requires= ["paquete_requerido >= 1.0 < 2.2"]

      )
#setup_requires
#test_requires

