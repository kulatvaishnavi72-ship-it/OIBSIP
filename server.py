"""
Two-User Chat Application — Server
Oasis Infobyte SIP, Python Track, Task 5 (Beginner Tier)

Listens for exactly two client connections on localhost, then relays
every message it receives from one client to the other in real time.
Handles disconnection gracefully by notifying the remaining client.
"""

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5050

clients = []          # list of (conn, addr, name)
clients_lock = threading.Lock()


def timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")


def broadcast(message: str, sender_conn):
    """Send a message to every connected client except the sender."""
    with clients_lock:
        for conn, addr, name in clients:
            if conn is not sender_conn:
                try:
                    conn.sendall(message.encode("utf-8"))
                except OSError:
                    pass


def remove_client(conn):
    with clients_lock:
        for entry in clients:
            if entry[0] is conn:
                clients.remove(entry)
                return entry[2]  # return their name
    return None


def handle_client(conn, addr):
    name = None
    try:
        conn.sendall(b"Enter your name: ")
        name = conn.recv(1024).decode("utf-8").strip()
        with clients_lock:
            clients.append((conn, addr, name))
        print(f"[{timestamp()}] {name} connected from {addr}")
        broadcast(f"[{timestamp()}] * {name} has joined the chat *\n", conn)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode("utf-8").strip()
            if not text:
                continue
            line = f"[{timestamp()}] {name}: {text}\n"
            print(line.strip())
            broadcast(line, conn)

    except (ConnectionResetError, ConnectionAbortedError):
        pass
    finally:
        removed_name = remove_client(conn) or name or "A user"
        print(f"[{timestamp()}] {removed_name} disconnected")
        broadcast(f"[{timestamp()}] * {removed_name} has left the chat *\n", conn)
        conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[{timestamp()}] Chat server listening on {HOST}:{PORT} ...")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print(f"\n[{timestamp()}] Server shutting down.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
