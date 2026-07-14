# AJ - 2026-07-12
# UDP Pinger Server

import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", 12000))

print("UDP Pinger Server is running on port 12000...")

while True:
    rand = random.randint(0, 10)

    message, address = serverSocket.recvfrom(1024)

    message = message.upper()

    if rand < 4:
        continue

    serverSocket.sendto(message, address)
