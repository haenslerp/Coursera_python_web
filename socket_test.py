"""
Request Reponse Cycle
Etablissement d'une connection: socket puis TCPIP port (ex port 80)
Hyper Text Transfer Protocol betwern servers and browsers
Uniform Ressource Locator: protocole, host (web server) and document
send a GET request, gets a response in Hyper Text Markup Langage (tags verween <> ) and the browser parses the document (<h1>, <p> paragraph, <a> anchor)
response: 200 ok, 404 page not found, 302 redirection
'"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# create a socket object
mysock.connect(('data.pr4e.org',80))# find the server, establish a socket.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # prepare tge command to send, double enter at the ebd of the line
mysock.send(cmd)

while True:
	data=mysock.recv(512)# receive is a method on the socjet object, receive up to 512 characters, bytes received
	if len(data)<1:
		break
	mystring=data.decode()#decode from bytes to unicode: ascii or  utf-8
	print(mystring)
mysock.close()# close the socket not to take too much resources0