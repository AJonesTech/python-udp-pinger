from socket import *
import time

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)

for sequenceNumber in range(1, 11):
    sendTime = time.time()
    message = f"Ping {sequenceNumber} {sendTime}"

    startTime = time.perf_counter()

    try:
        clientSocket.sendto(
            message.encode("ascii"),
            (serverName, serverPort)
        )

        response, serverAddress = clientSocket.recvfrom(1024)

        endTime = time.perf_counter()
        rtt = endTime - startTime

        print(response.decode("ascii"))
        print(f"RTT: {rtt:.6f} seconds")

    except timeout:
        print("Request timed out")

    print()

clientSocket.close()
