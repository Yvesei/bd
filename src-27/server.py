import sqlite3
import socketserver
import json

DB_FILE = "employes.db"

# Création BDD
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS employes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    salaire_ope BLOB,
    salaire_paillier TEXT
)
""")
conn.commit()
conn.close()

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(4096).decode()
        request = json.loads(data)

        action = request.get("action")
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()

        if action == "add":
            nom = request["nom"]
            salaire_ope = request["salaire_ope"]
            salaire_paillier = request["salaire_paillier"]
            cur.execute("INSERT INTO employes (nom, salaire_ope, salaire_paillier) VALUES (?, ?, ?)",
                        (nom, salaire_ope, str(salaire_paillier)))
            conn.commit()
            self.request.sendall(b"OK")

        elif action == "list":
            cur.execute("SELECT id, nom FROM employes")
            rows = cur.fetchall()
            self.request.sendall(json.dumps(rows).encode())

        elif action == "compare":
            id1, id2 = request["id1"], request["id2"]
            cur.execute("SELECT salaire_ope FROM employes WHERE id=?", (id1,))
            salaire1 = cur.fetchone()[0]
            cur.execute("SELECT salaire_ope FROM employes WHERE id=?", (id2,))
            salaire2 = cur.fetchone()[0]

            # Comparaison directe
            if salaire1 > salaire2:
                result = ">"
            elif salaire1 < salaire2:
                result = "<"
            else:
                result = "="

            self.request.sendall(result.encode())

        elif action == "sum_all":
            cur.execute("SELECT salaire_paillier FROM employes")
            salaires = [int(row[0]) for row in cur.fetchall()]
            public_key_nsquare = request["public_key_nsquare"]
            # Addition homomorphe : multiplication des chiffrés pour Paillier
            if not salaires:
                self.request.sendall(json.dumps({"error": "No salaries"}).encode())
            else:
                result = salaires[0]
                for salaire in salaires[1:]:
                    result = (result * salaire) % public_key_nsquare  # produit modulo n²
                self.request.sendall(json.dumps({"sum": result}).encode())

        elif action == "sum":
            data = self.request.recv(4096)
            data = json.loads(data.decode())

            nom1 = data["nom1"]
            nom2 = data["nom2"]
            nsquare = int(data["nsquare"])

            cur.execute("SELECT salaire_paillier FROM employes WHERE nom = ?", (nom1,))
            row1 = cur.fetchone()
            if row1 is None:
                self.request.sendall(f"Employé {nom1} introuvable.\n".encode())
                return
            salaire1 = int(row1[0])

            cur.execute("SELECT salaire_paillier FROM employes WHERE nom = ?", (nom2,))
            row2 = cur.fetchone()
            if row2 is None:
                self.request.sendall(f"Employé {nom2} introuvable.\n".encode())
                return
            salaire2 = int(row2[0])

            # Addition = multiplication modulo n^2
            somme_chiffree = (salaire1 * salaire2) % nsquare

            self.request.sendall(str(somme_chiffree).encode())

        conn.close()

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9998
    with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
        print(f"Serveur en ligne sur {HOST}:{PORT}")
        server.serve_forever()
