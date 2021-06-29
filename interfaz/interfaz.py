# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\lauta\Documents\GitHub\PPAI\interfaz\interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import gestor_reserva_visita as gestor
import base_de_datos.base_de_datos as BD
from datetime import datetime, date, time, timedelta



class Ui_Registrarreserva(object):
    def setupUi(self, Registrarreserva):
        
        Registrarreserva.setObjectName("Registrarreserva")
        Registrarreserva.resize(562, 792)
        Registrarreserva.setMinimumSize(QtCore.QSize(562, 792))
        Registrarreserva.setMaximumSize(QtCore.QSize(562, 792))
        Registrarreserva.setAutoFillBackground(False)
        Registrarreserva.setStyleSheet("")
        
        
        self.label = QtWidgets.QLabel(Registrarreserva)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.comboBoxEscuela = QtWidgets.QComboBox(Registrarreserva)
        self.comboBoxEscuela.setGeometry(QtCore.QRect(30, 50, 251, 31))
        self.comboBoxEscuela.setObjectName("comboBoxEscuela")
        self.comboBoxEscuela.activated.connect(self.tomar_seleccion_escuela)
        
        
        self.label_2 = QtWidgets.QLabel(Registrarreserva)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.spinBoxCantVisit = QtWidgets.QSpinBox(Registrarreserva)
        self.spinBoxCantVisit.setGeometry(QtCore.QRect(340, 50, 191, 31))
        self.spinBoxCantVisit.setMaximum(200)
        self.spinBoxCantVisit.setObjectName("spinBoxCantVisit")
        self.spinBoxCantVisit.valueChanged.connect(self.tomar_cantidad_visitantes)
        self.spinBoxCantVisit.valueChanged.connect(self.mostrar_sedes)
        
        self.label_3 = QtWidgets.QLabel(Registrarreserva)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.comboBoxSede = QtWidgets.QComboBox(Registrarreserva)
        self.comboBoxSede.setGeometry(QtCore.QRect(30, 120, 251, 31))
        self.comboBoxSede.setObjectName("comboBoxSede")
        self.comboBoxSede.activated.connect(self.tomar_sede)
        self.comboBoxSede.activated.connect(self.mostrar_tipo_visita)
        
        self.label_4 = QtWidgets.QLabel(Registrarreserva)
        self.label_4.setGeometry(QtCore.QRect(340, 90, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.comboBoxTipoVisita = QtWidgets.QComboBox(Registrarreserva)
        self.comboBoxTipoVisita.setGeometry(QtCore.QRect(340, 120, 191, 31))
        self.comboBoxTipoVisita.setObjectName("comboBoxTipoVisita")
        self.comboBoxTipoVisita.activated.connect(self.tomar_tipo_visita)
        self.comboBoxTipoVisita.activated.connect(self.mostrar_datos_expo_temp_vig)
        
        self.label_5 = QtWidgets.QLabel(Registrarreserva)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Registrarreserva)
        self.label_7.setGeometry(QtCore.QRect(400, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Registrarreserva)
        self.label_8.setGeometry(QtCore.QRect(30, 550, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Registrarreserva)
        self.buttonBox.setGeometry(QtCore.QRect(310, 720, 221, 81))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.tomar_confirmacion)
        self.buttonBox.rejected.connect(self.cerrar_ventana)
        
        self.timeEditHora = QtWidgets.QTimeEdit(Registrarreserva)
        self.timeEditHora.setGeometry(QtCore.QRect(400, 410, 131, 31))
        self.timeEditHora.setObjectName("timeEditHora")
        self.timeEditHora.timeChanged.connect(self.tomar_hora_reserva)
        self.timeEditHora.timeChanged.connect(self.tomar_fecha_hora_reserva)
        self.timeEditHora.timeChanged.connect(self.mostrar_guias_disponibles)
        
        self.tableExposiciones = QtWidgets.QTableWidget(Registrarreserva)
        self.tableExposiciones.setGeometry(QtCore.QRect(30, 180, 501, 171))
        self.tableExposiciones.setDragEnabled(False)
        self.tableExposiciones.setAlternatingRowColors(True)
        self.tableExposiciones.setRowCount(0)
        self.tableExposiciones.setObjectName("tableExposiciones")
        self.tableExposiciones.setColumnCount(4)
        self.tableExposiciones.setColumnWidth(0,75)
        self.tableExposiciones.setColumnWidth(1,274)
        self.tableExposiciones.setColumnWidth(2,100)
        self.tableExposiciones.setColumnWidth(3,50)
        nombreColumnas = ("Exposicion","publico", "horario", "  ")
        self.tableExposiciones.setHorizontalHeaderLabels(nombreColumnas)
        self.tableExposiciones.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableExposiciones.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableExposiciones.itemDoubleClicked.connect(self.tomar_selec_exposiciones)
        
        
        self.tableWidgetGuias = QtWidgets.QTableWidget(Registrarreserva)
        self.tableWidgetGuias.setGeometry(QtCore.QRect(30, 580, 501, 141))
        self.tableWidgetGuias.setAlternatingRowColors(True)
        self.tableWidgetGuias.setColumnCount(3)
        self.tableWidgetGuias.setObjectName("tableWidgetGuias")
        self.tableWidgetGuias.setRowCount(0)
        nombre_columnas_guias=('Nombre','Apellido','Seleccionado')
        self.tableWidgetGuias.setHorizontalHeaderLabels(nombre_columnas_guias)
        self.tableWidgetGuias.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetGuias.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetGuias.itemDoubleClicked.connect(self.tomar_seleccion_guias)
        
        
        self.calendarWidget = QtWidgets.QCalendarWidget(Registrarreserva)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 360, 312, 183))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.tomar_fecha_hora_reserva)
        self.calendarWidget.clicked.connect(self.mostrar_guias_disponibles)

        self.retranslateUi(Registrarreserva)
        QtCore.QMetaObject.connectSlotsByName(Registrarreserva)
        Registrarreserva.setTabOrder(self.comboBoxEscuela, self.spinBoxCantVisit)
        Registrarreserva.setTabOrder(self.spinBoxCantVisit, self.comboBoxSede)
        Registrarreserva.setTabOrder(self.comboBoxSede, self.comboBoxTipoVisita)
        Registrarreserva.setTabOrder(self.comboBoxTipoVisita, self.tableExposiciones)
        Registrarreserva.setTabOrder(self.tableExposiciones, self.timeEditHora)
        Registrarreserva.setTabOrder(self.timeEditHora, self.tableWidgetGuias)

    def retranslateUi(self, Registrarreserva):
        _translate = QtCore.QCoreApplication.translate
        Registrarreserva.setWindowTitle(_translate("Registrarreserva", "Registrar reserva"))
        self.label.setText(_translate("Registrarreserva", "Escuelas"))
        self.label_2.setText(_translate("Registrarreserva", "Cantidad de visitantes"))
        self.label_3.setText(_translate("Registrarreserva", "Sedes"))
        self.label_4.setText(_translate("Registrarreserva", "Tipo de visita"))
        self.label_5.setText(_translate("Registrarreserva", "Exposiciones"))
        self.label_7.setText(_translate("Registrarreserva", "Hora"))
        self.label_8.setText(_translate("Registrarreserva", "Guias"))

    def mostrar_escuelas(self):
        for i in gestor.gestor_reserva_visita_nuevo.buscar_escuelas():
            self.comboBoxEscuela.addItem(i)
            
    def tomar_seleccion_escuela(self):
        for i in BD.array_escuelas:
            if i.get_nombre() == self.comboBoxEscuela.currentText():
                gestor.gestor_reserva_visita_nuevo.tomar_escuela(i)
    
    def tomar_cantidad_visitantes(self):
        gestor.gestor_reserva_visita_nuevo.tomar_cant_visitantes(self.spinBoxCantVisit.value())
    
    def mostrar_sedes(self):
        #aca hay q poner q verifique q sea mayor a null las sedes
        self.comboBoxSede.clear()
        for i in gestor.gestor_reserva_visita_nuevo.buscar_sede():
            self.comboBoxSede.addItem(i)
            
    def tomar_sede(self):
        
        for i in BD.array_sede:
            if i.get_nombre() == self.comboBoxSede.currentText():
                gestor.gestor_reserva_visita_nuevo.tomar_sede(i)
        
                
    def mostrar_tipo_visita(self):
        self.comboBoxTipoVisita.clear()
        for i in gestor.gestor_reserva_visita_nuevo.buscar_tipo_visita():
            self.comboBoxTipoVisita.addItem(i)
            
    def tomar_tipo_visita(self):
        for i in BD.array_tipo_visita:
            if i.get_nombre()==self.comboBoxTipoVisita.currentText():
                gestor.gestor_reserva_visita_nuevo.tomar_tipo_visita(i)

    def mostrar_datos_expo_temp_vig(self):
        expo = gestor.gestor_reserva_visita_nuevo.buscar_exposiciones_temp_vigentes()
        self.tableExposiciones.setRowCount(len(expo))
        
        for vector_exposicion in range (len(expo)):
            #[[exposicion 1,publico destino,horario][exposicion2,...,....]]
            for j in range (len(expo[vector_exposicion])):
                
                self.tableExposiciones.setItem(vector_exposicion,j,QTableWidgetItem(str(expo[vector_exposicion][j])))
                self.tableExposiciones.setItem(vector_exposicion,3,QTableWidgetItem('NO'))
        
    def tomar_selec_exposiciones(self):
        array_exposiciones = []
        filaSeleccionada=self.tableExposiciones.selectedItems()
        fila = filaSeleccionada[0].row()
        if filaSeleccionada[3].text() =='NO':
            self.tableExposiciones.setItem(fila,3,QTableWidgetItem('SI'))
        else:
            self.tableExposiciones.setItem(fila,3,QTableWidgetItem('NO'))
        
        for row in range(self.tableExposiciones.rowCount()):
            for i in gestor.gestor_reserva_visita_nuevo.buscar_exposiciones_temp_vigentes():
                x=self.tableExposiciones.item(row,0).text()
                if x == i[0]:
                    if self.tableExposiciones.item(row,3).text() == 'SI':
                        for expo in BD.array_exposiciones:
                            if expo.get_nombre()==x:
                                array_exposiciones.append(expo)    
        print(array_exposiciones)
        gestor.gestor_reserva_visita_nuevo.tomar_exposiciones(array_exposiciones)
    
    def tomar_fecha_reserva(self):
        fecha=self.calendarWidget.selectedDate()
        fecha=fecha.toPyDate()
    
    def tomar_hora_reserva(self):
        hora=self.timeEditHora.time()
        hora=hora.toPyTime()
    
    def tomar_fecha_hora_reserva(self):
        hora=self.timeEditHora.time()
        hora=hora.toPyTime()
        fecha=self.calendarWidget.selectedDate()
        fecha=fecha.toPyDate()    
        gestor.gestor_reserva_visita_nuevo.tomar_fecha_hora_reserva(datetime(fecha.year,fecha.month,fecha.day,hora.hour,hora.minute))
        gestor.gestor_reserva_visita_nuevo.calcular_duracion_estimada_reserva()
        self.mostrar_cantidad_guias_necesarios()

    def mostrar_cantidad_guias_necesarios(self):
        x=gestor.gestor_reserva_visita_nuevo.calcular_cantidad_guias_necesarios()
        self.label_8.setText(("Guias      GUIAS necesarios:"+str(x)))
    
    def mostrar_guias_disponibles(self):
        guias = gestor.gestor_reserva_visita_nuevo.buscar_guias_disponibles()
        self.tableWidgetGuias.setRowCount(len(guias))
        print('len guias')
        print(len(guias))
        for i in range(len(guias)):
                self.tableWidgetGuias.setItem(i,0,QTableWidgetItem(guias[i].nombre))
                self.tableWidgetGuias.setItem(i,1,QTableWidgetItem(guias[i].apellido))
                self.tableWidgetGuias.setItem(i,2,QTableWidgetItem('NO'))
            
    def tomar_seleccion_guias(self):
        array_guias = []
        filaSeleccionada=self.tableWidgetGuias.selectedItems()
        fila = filaSeleccionada[0].row()
        if filaSeleccionada[2].text() =='NO':
            self.tableWidgetGuias.setItem(fila,2,QTableWidgetItem('SI'))
        else:
            self.tableWidgetGuias.setItem(fila,2,QTableWidgetItem('NO'))
        
        for row in range(self.tableWidgetGuias.rowCount()):
            for i in gestor.gestor_reserva_visita_nuevo.buscar_guias_disponibles():
                x=self.tableWidgetGuias.item(row,0).text()
                if x == i.nombre:
                    if self.tableWidgetGuias.item(row,2).text() == 'SI':
                     array_guias.append(i)    
        print(array_guias)
        gestor.gestor_reserva_visita_nuevo.tomar_guias(array_guias)
        
    def tomar_confirmacion(self):
        gestor.gestor_reserva_visita_nuevo.tomar_confirmacion()
        self.close()
    
    def cerrar_ventana(self):
        self.close()
        