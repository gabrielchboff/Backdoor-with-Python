# obj server
class ServerConn(object):
    import threading

    def __init__(self, server):
        self.server = server
    
    def listen(self, ip, port, max_conn):
        try:
            self.server.bind((ip, port))
            self.server.listen(max_conn)
            print('[*] @ listen on >> ip : {} port {}'.format(ip, port))
        except Exception as e:
            print('[*] @ Error server listen ! \nThe Exception: {}'.format(str(e)))

    # this is our client-handling thread
    def handle_client(self, client_socket):
        try:
            # print out what the client sends
            request = client_socket.recv(1024)
            print('[*] Received!: {}'.format(request))
            # send back a packet
            client_socket.send('[*] @ ON !')
            client_socket.close()
            
        except Exception as e:
            print('[*] @ Error get connection \nThe Exception: {}'.format(str(e)))

    def entry_go(self, handle_client):
        handle_client = handle_client()
        while(True):
            client, addr = self.server.accept()
            print('[*] Accepted connection from: {}:{}'.format(addr[0],addr[1]))
            # spin up our client thread to handle incoming data
            client_handler = self.threading.Thread(target=handle_client,args=(client,))
            client_handler.start()

       