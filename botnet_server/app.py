from flask import Flask, request, session, redirect
import json

app = Flask(__name__)

app.secret_key = "67afa930218239e223ebb99ba83c03e177113214f63c01516b8ca4d21c00431e"

@app.route("/")
def home():
    return "Hello, Home!"

@app.route("/control_panel")
def control_panel():
    return "Control Panel!"

#Incoming Client Information

#class Client():
#    def __init__()


@app.route("/client/connect", methods=["GET"])
def client_connect():
    trust = False
    if request.headers.getlist("X-Forwarded-For"):
        session["ip"] = request.headers.getlist("X-Forwarded-For")[0]
        for x in request.headers.getlist("X-Forwarded-For"):
            app.logger.info("ip's from X-Forwarded-For list: " + x)
    else:
        session["ip"] = request.remote_addr
        app.logger.info("Fetched IP: " + session["ip"])
    #data = request.args.get("data")
    #need to add the data functionality but its just easier no to not
    client = {
        "ip": session["ip"],
        #"data": data
    }
    with open("/Users/joshuawalter/documents/python/network/botnet_server/client_list.json", "r") as client_list_file:
        client_list = json.load(client_list_file)
    app.logger.info("Opened client_list.json")
    with open("/Users/joshuawalter/documents/python/network/botnet_server/trusted_client_list.json", "r") as trusted_client_list_file:
        trusted_client_list = json.load(trusted_client_list_file)
    app.logger.info("Opened trusted_client_list.json")

    if client in trusted_client_list["list"]:
        trust = True
        client_list["list"].append(client)
        with open("/Users/joshuawalter/documents/python/network/botnet_server/client_list.json", "w") as client_list_file:
            json.dump(client_list, client_list_file)
        app.logger.info("Writing Clint IP: " + session["ip"] + "to client_list.json")
        app.logger.info("Connected Client IP: " + session["ip"])
        return "True"
    else:
        #add a way to authenticate or ask for password in POST form
        client_list["list"].append(client)
        with open("/Users/joshuawalter/documents/python/network/botnet_server/client_list.json", "w") as client_list_file:
            json.dump(client_list, client_list_file)
        app.logger.info("Writing Clint IP: " + session["ip"] + " to client_list.json")
        app.logger.info("Connected Client IP: " + session["ip"])
        return "True"
    



#Test ping for client to make sure they are connected, might add one from the server to the client too so...
#both server and client know when they disconnect
@app.route("/client/connect/ping")
def client_connect_ping():
    return "True"


