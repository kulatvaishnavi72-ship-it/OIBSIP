"""
Two-User Chat Application — Client
Oasis Infobyte SIP, Python Track, Task 5 (Beginner Tier)

Connects to the chat server on localhost and exchanges messages in
real time. Run this script twice (two terminals) to chat between
two users on the same machine.
"""

import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5050


def listen_for_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
        except OSError:
            break
        if not data:
            print("\n[Disconnected from server]")
            break
        print(data.decode("utf-8"), end="")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f"Could not connect to server at {HOST}:{PORT}. Is server.py running?")
        sys.exit(1)

    # First recv is the "Enter your name:" prompt from the server
    prompt = sock.recv(1024).decode("utf-8")
    name = input(prompt)
    sock.sendall(name.encode("utf-8"))

    listener = threading.Thread(target=listen_for_messages, args=(sock,), daemon=True)
    listener.start()

    print("Connected! Type a message and press Enter. Ctrl+C to quit.\n")
    try:
        while True:
            message = input()
            if message.strip() == "":
                continue
            sock.sendall(message.encode("utf-8"))
    except (KeyboardInterrupt, EOFError):
        print("\nDisconnecting...")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
