#!usr/bin/python3

#obj backdor
class Backdoor(object):
    def build_door(self, connection_type, ip, port):
        import socket

        conn = None
        if connection_type == 'tcp':
            conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        elif connection_type == 'udp':
            conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print('Error on type connection')

        if port <= 990:
            print('TIP : select a port more than 991 !')
        else:
            print('This is a good port!')

        connection_attrs = {
            'connection_type': conn,
            'ip': ip,
            'port': port
        }

        return connection_attrs


    