#Este programa se encarga de recibir los datos del servidor para que controle
#el apagado o prendido del televisor por otra parte tambien el sensor de movimiento
#hace su funcion cuando se detecta apaga el televisor
import RPi.GPIO as GPIO
import socket
import time
from datetime import datetime
import cec
import threading
host = "192.168.1.66" #ip server
port = 5000 
cec.init()
command = ''
tv=cec.Device(cec.CECDEVICE_TV)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
value = 0
def speech_recog():
    while True: 
         # Create socket
        s = socket.socket()                                
    # Connect to host
        s.connect((host, port))

    # Receive command voice 
        command = s.recv(1024)
        command = command.decode()     
        if command =="turn on":
            tv.power_on()
        if command =="turn off":
            tv.standby()
        if command == "disconnect":
            s.close()
            print("Disconected from server")
            t1.join()
            t2.join()
            break
    
        s.close()

def movement():
    while True:
        i = GPIO.input(7)
        if i==1:
            tv.standby()
threads = []
t1 = threading.Thread(target=speech_recog)
threads.append(t1)
t1.start()
t2 = threading.Thread(target=movement)
threads.append(t2)
t2.start()
