import sys
import os
from PyQt5.QtWidgets import QApplication
from ui.views.login_view import LoginWindow
# from ui.views.main_window import MainWindow

def cargar_estilos(app):
    # Ruta relativa para ubicar tu archivo de diseño modo oscuro/neón
    ruta_qss = os.path.join(os.path.dirname(__file__), "ui", "styles", "theme.qss")
    if os.path.exists(ruta_qss):
        with open(ruta_qss, "r") as archivo_estilos:
            app.setStyleSheet(archivo_estilos.read())
    else:
        print("Advertencia: No se encontró el archivo theme.qss")

def main():
    app = QApplication(sys.argv)
    
    # Aplicar el estilo general a toda la aplicación
    cargar_estilos(app)
    
    # Instanciar e iniciar la ventana de Login
    ventana_login = LoginWindow()
    ventana_login.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()