#Este programa se encarga de reconocer el audio para luego enviarselo a la raspberry pi
import speech_recognition as sr
import socket  
import time     

host = "192.168.1.66"
port = 5000 

conn = None
addr = None

r1 = sr.Recognizer()

# Create socket
s = socket.socket()             
s.bind((host, port))            
s.listen()          
print ("Server listening....")

while True:

    # Accept connection
    conn, addr = s.accept()     
    print ("Got connection from", addr)

    #Audio recognition
    try:
        with sr.Microphone() as source:
            audio = r1.listen(source)
        if 'turn on' in r1.recognize_google(audio):
            print("turn on")
            msg = 'turn on'  
            conn.send(msg.encode())      
        elif 'turn off' in r1.recognize_google(audio):
            print("turn off")
            msg = 'turn off'  
            conn.send(msg.encode()) 
        elif 'disconnect' in r1.recognize_google(audio):
            print("disconnect")
            msg = 'disconnect'  
            conn.send(msg.encode())
            conn.close()
            break
        else:
            conn.send("Command not available.".encode())
            print("Command not available")
    except:
        print("command not recognized")
    conn.close()
