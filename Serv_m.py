"""
This is server for TCP connection
Execute on your pc
"""


#!usr/bin/python

import threading
import socket




class server(object):
	"""docstring for server"""
	def __init__(self):
		ip.self = ''
		port.self = 8684
		tcp.self = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	def connect1(self):
		try:
			tcp.self.bind((ip.self, port.self))
			tcp.self.listen(5)

			print('[*] @ listen on >> ip : {} port {}'.format(ip.self, port.self))
		except:
			print('[*] @ Error server listen !')

	def had_client(self):
		try:

			request = clt_socket.recv(1024)
			print('[*] @ Recived (response): {}'.format(request))
			clt_socket.send('[*] @ ON !')
			clt_socket.close()
		except:
			connect1()

	def base64():
		pass

	connect1()
	had_client()

	while True:
		clt,addr = tcp.accept()
		print('[*] @ Accept connection from : {} and {}',format(addr[0],addr[1]))

		clt_handler = thread to handler incoming data
		clt_handler.start()

			
