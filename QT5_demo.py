import sys
from PyQt5 import uic, QtWidgets
from datetime import date

qtCreatorFile = "pantalla_principal.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_aceptar.clicked.connect(self.agregar)
    def agregar(self):
    	fecha= date.today()
    	self.txtTexto.setText("La fecha de hoy es: " + str(fecha))

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())