# save sebagai get_capsule.py
import socket
import json

HOST = "94.237.48.12"   # <---- ganti di sini
PORT = 57710

def get_one():
    s = socket.create_connection((HOST, PORT), timeout=10)
    # baca prompt
    data = s.recv(4096)
    print(data.decode(errors="ignore"), end="")
    # kirim 'Y' untuk minta capsule
    s.sendall(b"Y\n")
    # terima JSON
    reply = s.recv(8192).decode()
    s.close()
    print("RAW REPLY:")
    print(reply)
    try:
        j = json.loads(reply)
        print("\nPARSED:")
        print(json.dumps(j, indent=2))
    except Exception as e:
        print("Gagal parse JSON:", e)

if __name__ == "__main__":
    get_one()
