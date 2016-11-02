import serial
import timeit
from matplotlib import pyplot as plt
import csv

voltage = 0

arduino = serial.Serial(port='COM3', baudrate=9600, bytesize=8)

arduino.flush()

if(arduino.isOpen()):
    try:
        start = timeit.default_timer()
        while timeit.default_timer() - start <= 5:
            voltage = arduino.read()
            print(voltage)
            with open('logged_data.csv', 'a') as csv_data:
                writer = csv.writer(csv_data, delimiter=',')
                writer.writerow(voltage)
    except Exception:
        print('Eror Reading from serial port')
else:
    print('Cannot open serial port')
