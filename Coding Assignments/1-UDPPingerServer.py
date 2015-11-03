# UDPPingerServer.py
# We will need the following module to generate randomized lost packets import random
#from socket import *
import socket
import random
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
# Assign IP address and port number to socket
UDP_IP = "127.0.0.1"
serverSocket.bind((UDP_IP, 12000))
while True:
    print 'start receiving...'
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    print 'ramdom number is ', rand
    # Receive the client packet along with the address it is coming from
    try:
        message, address = serverSocket.recvfrom(1024)
    except Exception as e:
        print(e)
    print 'Message received is \'', message, '\' from', address
    # Capitalize the message from the client
    message = message.upper()
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
   
    serverSocket.sendto(message, address)
