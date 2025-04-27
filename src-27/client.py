import socket
import json
import sys
from pyope.ope import OPE
from phe import paillier

public_key, private_key = paillier.generate_paillier_keypair()
random_key = OPE.generate_key() 
ope_cipher = OPE(random_key)

IP_SERVER = "127.0.0.1"
PORT_SERVER = 9998

def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((IP_SERVER, PORT_SERVER))
        sock.sendall(json.dumps(request).encode())
        response = sock.recv(4096)
    return response

def add_employee():
    nom = input("Nom de l'employé : ")
    salaire = int(input("Salaire : "))
    salaire_paillier = public_key.encrypt(salaire).ciphertext()
    salaire_ope = ope_cipher.encrypt(int(salaire))

    request = {
        "action": "add",
        "nom": nom,
        "salaire_ope": salaire_ope,
        "salaire_paillier": salaire_paillier
    }
    send_request(request)
    print("Employé ajouté.")

def list_employees():
    response = send_request({"action": "list"})
    rows = json.loads(response.decode())
    for row in rows:
        print(f"ID: {row[0]}, Nom: {row[1]}")

def compare_employees():
    id1 = int(input("ID Employé 1 : "))
    id2 = int(input("ID Employé 2 : "))
    request = {
        "action": "compare",
        "id1": id1,
        "id2": id2
    }
    result = send_request(request).decode()
    print(f"Comparaison salaire: Employé {id1} {result} Employé {id2}")

def sum_salaries():
    nom1 = input("Nom du premier employé : ")
    nom2 = input("Nom du deuxième employé : ")

    request = {
        "action": "sum",
        "nom1": nom1,
        "nom2": nom2,
        "nsquare": public_key.nsquare
    }

    result = send_request(request).decode()
    somme_chiffree = int(result)

    somme = private_key.decrypt(somme_chiffree)
    print(f"La somme des salaires est : {somme}")


if __name__ == "__main__":
    # IP_SERVER = sys.argv[1]
    # PORT_SERVER = int(sys.argv[2])

    while True:
        print("\nMenu :")
        print("1 - Ajouter un employé")
        print("2 - Lister les employés")
        print("3 - Comparer 2 employés")
        print("4 - Somme des salaires")
        print("5 - Quitter")

        choice = input("Choix : ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            compare_employees()
        elif choice == "4":
            sum_salaries()
        elif choice == "5":
            break
