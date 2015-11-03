# UDPPingerClient.py
# We will need the following module to send 10 pings to the server.
import socket
import datetime
import time
import array
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
#set the timeout for 1 sec to wait for the reply
clientSocket.settimeout(1.0)
UDP_IP = "127.0.0.1"
UDP_PORT = 12000
MSSG = 'ping message'
#initial the counter
i = 1
#initial the array to save RTT
RTTList = []
while i <= 10:
  #initial current time and set the time format
  sendTime = time.time()
  formatSendTime = datetime.datetime.fromtimestamp(sendTime).strftime('%Y-%m-%d %H:%M:%S:%f')
  try:
    #send ping message to server socket
    clientSocket.sendto(MSSG,(UDP_IP,UDP_PORT))
    #print ping message with format 'Ping sequence_number time'
    print 'Ping ', i, ' ', formatSendTime
    
    #start reveiving the reply
    data , addr = clientSocket.recvfrom(1024)
    #set the receive time to calculate the RTT
    receiveTime = time.time()
    formatRecTime = datetime.datetime.fromtimestamp(receiveTime).strftime('%Y-%m-%d %H:%M:%S:%f')
    RTT = round((receiveTime - sendTime),6)
    RTTList.append(RTT)
    print 'Received from ', addr, 'at ',formatRecTime
    print 'Received message:', data, 'RTT=',RTT,'ms'
  #if the timeout error happens print the request timed out
  except socket.timeout:
    print 'Request timed out'
  i = i +1
#calculate the packets loss % and total RTT
print i-1,' packets transmitted, ',len(RTTList),' packets received,',float(i-1-len(RTTList))/float(i-1)*100,'% packets loss'
print 'round-trip min/avg/max',min(RTTList),'/',sum(RTTList) / float(len(RTTList)),'/',max(RTTList),'ms'