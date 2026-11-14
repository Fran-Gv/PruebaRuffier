from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout , QLineEdit
 

app = QApplication([])
ventana1 = QWidget ()
ventana2 = QWidget ()
ventana3 = QWidget ()
ventana1.setWindowTitle('Prueba de ruffier')
ventana2.setWindowTitle('Prueba de ruffier')
ventana3.setWindowTitle('Prueba de ruffier')
ventana1.resize(500, 300)
ventana2.resize(800, 500)
ventana3.resize(300, 300)

ventanas = [ventana1,ventana2,ventana3]

#primera ventana
bienvenida = QLabel('Bienevenido a la prueba de Ruffier')
instrucciones = QLabel('Instrucciones')
start = QPushButton('Comenzar la prueba')

#Botones_segundaVentana

first_test = QPushButton('Empezar la primera prueba')
final_test = QPushButton('Empezar prueba final')
sentadillas = QPushButton('Hacer sentadillas')
result_but = QPushButton('Enviar resultados')

#Texto_segundaVentana
txt_name = QLabel('Nombre')
txt_age = QLabel('Edad')
txt_1 = QLabel('presiona el boton, toma tu pulso durante 15 segundos y escribelo en la casilla')
txt_2 = QLabel('haga 30 sentadillas durante 45 segundos')
txt_3 = QLabel('tome su pulso durante 15 segundos despues de descansar')
txt_timer = QLabel('')

#Lineas editables

nombre = QLineEdit('Nombre')
edad = QLineEdit('Edad')
p1 = QLineEdit('0')
p2 = QLineEdit('0')
p3 = QLineEdit('0')

resultado = ['Bajo','satisfactorio','Promedio','Por encima del promedio','Alto']

def mostrar_resultado(edad,indice):
    if edad == 8 or edad == 7:
       puntajes = [21,17,12,6.5]
    elif edad == 10 or edad == 9:
        puntajes = [19.5,15.5,10.5,5]
    elif edad == 12 or edad ==11:
        puntajes =[18,14,9,3.5]
    elif edad == 14 or edad == 13:
        puntajes = [16.5,12.5,7.5,2]
    elif edad >= 15:
        puntajes = [15,11,6,0.5]
    else:
        return 'Edad fuera de rango'


    for i,p in enumerate(puntajes):
        if indice >= p:
            return resultado[i]
    return resultado[4]

def aparecer_ventana(actual):
    for v in ventanas:
        if v == actual:
            v.show()
        else:
            v.hide()


txt_indice = QLabel('')
text_result = QLabel('')


def enviar_resultado():
    try:
        edad_n =  int(edad.text())
        pulso_1 = int(p1.text())
        pulso_2 = int(p2.text())
        pulso_3 = int(p3.text())
    except ValueError:
        txt_1.setText('Escribe solo números en la edad y los pulsos')
        return

    indice = (4*( pulso_1 + pulso_2 + pulso_3)-200)/10
    nivel = mostrar_resultado(edad_n, indice)

    txt_indice.setText(f'Su indice es la prueba es: {indice}')
    text_result.setText(f'Su resultado en la prueba es {nivel} según su edad')
    aparecer_ventana(ventana3)


time = QTime(0, 0, 15)
timer = QTimer()


def iniciar_reloj(segundos):
    global time
    timer.stop()
    time = QTime(0, 0, segundos)
    txt_timer.setText(time.toString('hh:mm:ss'))  
    timer.start(1000)     



def timer_event():
    global time

    time = time.addSecs(-1)
    txt_timer.setText(time.toString('hh:mm:ss'))

    if time.toString('hh:mm:ss') == '00:00:00':
        timer.stop()

timer.timeout.connect(timer_event)


line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()



line1.addWidget(bienvenida)
line1.addWidget(instrucciones)
line1.addWidget(start)

ventana1.setLayout(line1)

txt_timer.setText(time.toString('hh:mm:ss'))

line2.addWidget(txt_timer, alignment = Qt.AlignRight )
line2.addWidget(txt_name)
line2.addWidget(nombre)
line2.addWidget(txt_age)
line2.addWidget(edad)
line2.addWidget(txt_1)
line2.addWidget(first_test)
line2.addWidget(p1)
line2.addWidget(txt_2)
line2.addWidget(sentadillas)
line2.addWidget(txt_3)
line2.addWidget(final_test)
line2.addWidget(p2)
line2.addWidget(p3)
line2.addWidget(result_but)

ventana2.setLayout(line2)



line3.addWidget(txt_indice)
line3.addWidget(text_result)


ventana3.setLayout(line3)

start.clicked.connect(lambda: aparecer_ventana(ventana2))
result_but.clicked.connect(enviar_resultado)
first_test.clicked.connect(lambda: iniciar_reloj(15))
sentadillas.clicked.connect(lambda: iniciar_reloj(45))
final_test.clicked.connect(lambda: iniciar_reloj(15))










aparecer_ventana(ventana1)
app.exec_()