from socket import *
import ssl
import base64
msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start 
mailserver = 'smtp.gmail.com'
SER_PORT = 587						
#Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
try:
	clientSocket = socket(AF_INET,SOCK_STREAM)
	clientSocket.connect((mailserver,SER_PORT))
	print '---TCP connection has established---'
except error, errmsg:
	print 'Couldnt connect with the socket-server:', errmsg           
#Fill in end
recv = clientSocket.recv(1024)
print '1-',recv
if recv[:3] != '220':
	print '220 reply not received from server.'
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print '2-',recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

#Prepare username and password
USER = 'yuxinwoziji'
PASSWD = '******'#here I hide the password
#Send STARTTLS command
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand)
recv2 = clientSocket.recv(1024)
print '3-',recv2
if recv2[:3] != '220':
	print '220 reply not received from server.'
else:#ready for TLS,use ssl to wrap the client socket
	sslClientSocket = ssl.wrap_socket(clientSocket)
	#send AUTH LOGIN request to email server
	sslClientSocket.send('AUTH LOGIN\r\n')
	recv3 = sslClientSocket.recv(1024)
	print '4-',recv3
	if recv3[:3] != '334':
		print '334 reply not received from server'
	else:
		#send username and password to mail server to get the authrization
		sslClientSocket.send(base64.b64encode(USER)+'\r\n')
		sslClientSocket.send(base64.b64encode(PASSWD)+'\r\n')
		recv4 = sslClientSocket.recv(1024)
		print '5-',recv4
		if recv4[:3] != '334':
			print '334 reply not received from server'
# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM: <'+USER+'>\r\n'
sslClientSocket.send(mailFrom)
recv5 = sslClientSocket.recv(1024)
print '6-',recv5
if recv5[:3] != '235':
	print '235 reply not received from server.'
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptTo = 'RCPT TO: <xyun@uwo.ca>\r\n'
sslClientSocket.send(rcptTo)
recv6 = sslClientSocket.recv(1024)
print '7-',recv6
if recv6[:3] != '250':
	print '250 reply not received from server.'
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
sslClientSocket.send(data)
recv7 = sslClientSocket.recv(1024)
print '8-',recv7
if recv7[:3] != '250':
	print '250 reply not received from server.'
# Fill in end
# Send message data.
# Fill in start
sslClientSocket.send(msg)
recv8 = sslClientSocket.recv(1024)
print '9-',recv8
if recv8[:3] != '354':
	print '354 reply not received from server.'
# Fill in end 
# Message ends with a single period.
# Fill in start
sslClientSocket.send(endmsg)
recv9 = sslClientSocket.recv(1024)
print '10-',recv9
if recv9[:3] != '250':
	print '250 reply not received from server.'
# Fill in end
# Send QUIT command and get server response.
# Fill in start
sslClientSocket.send('QUIT\r\n')
recv10 = sslClientSocket.recv(1024)
print '11-',recv10
# Fill in end
#close the TCP socket
if recv10[:3] != '221':
	print '221 reply not received from server'
else:#quit successfully, then close the socket
	clientSocket.close()
	print '----TCP socket closed----'