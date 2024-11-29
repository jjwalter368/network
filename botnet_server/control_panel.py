import requests

admin_username = "root"
admin_password = "root"

def auth():
    username = input("Username: ")
    password = input("Password: ")
    if username == admin_username and password == admin_password:
        return True
    else:
        exit()

def main():
    while True:
        command = input("root> ").split()
        match command[0]:
            case "list":
                # show all clients
                with open("client_list.json", "w") as client_list:
                    print(client_list)

print("Welcome to control panel v1.00")
if auth():
    main()