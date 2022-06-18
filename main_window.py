import serial
import mysql.connector

from PyQt5 import QtWidgets

from listener import Listener
from serial_ports import serial_ports
from typing import Union
from design import design


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.port: Union[serial.Serial, None] = None
        self.listener = None
        self.init_elements()
        self.temperature = ""
        self.humidity = ""
        self.getTemperature1.clicked.connect(self.click)

    def click(self):
        data = str(self.port.readline())
        self.temperature = data[2:4]
        self.humidity = data[7:9]
        self.dispTemp.setText(self.temperature + " C")
        self.dispHum.setText(self.humidity + "  %")

        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="conditioner",
                user="root",
                password="Mary123"
            )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                cursor = connection.cursor()

                sql = "INSERT INTO state (humidity, temp) VALUES (%s, %s)"
                print(sql)
                val = (self.temperature, self.humidity)
                cursor.execute(sql, val)

                connection.commit()
                cursor.close()
            connection.close()

        except mysql.connector.Error:
            print("Error while connection to database")

    def init_elements(self):
        self.comComboBox.addItems(serial_ports())
        self.port = serial.Serial(self.comComboBox.currentText(),
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  bytesize=serial.EIGHTBITS,
                                  timeout=2)

    def listen_port(self):
        self.listener = Listener(self.port, self.receive_message)
        self.listener.start()

    def receive_message(self, message):
        print(message.decode("utf-8"))

    def send_message(self, message):
        if self.port:
            self.port.write(str(message).encode("utf-8"))