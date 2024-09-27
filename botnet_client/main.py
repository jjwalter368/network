import requests, os
from time import sleep

def client_connect_ping():
        #Changing to a more headless mode with only intervening when the connection is unsuccesful
        #print("Test Pinging Server...")
        if requests.get("http://127.0.0.1:5000/client/connect/ping").text == "True":
             #print("Test Ping Succesful")
             return True
        else:
             print("Test Ping Failure")
             return False

def connect():
     if requests.get("http://127.0.0.1:5000/client/connect").text == "True":
          return True
     else: 
          print(requests.get("http://127.0.0.1:5000/client/connect").text)
          return False

def main():
    if connect() == True:
         connected = True
    else:
         connected = False
         print("Initial Connection Failed")
    while connected:
        sleep(5)
        connected = client_connect_ping()

main()