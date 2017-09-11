import socket
import sys
import select

#É capturado os argumentos de entrada do usuário.
HOST = "".join(sys.argv[1])
PORT_str = "".join(sys.argv[2])
data = "".join(sys.argv[3])
PORT = int(PORT_str)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))	#É enviado a mensagem para o servidor

sock.setblocking(0)
ready = select.select([sock], [], [], 5)	#Foi colocado um timeout de 5 segundos
if ready[0]:	#If utilizado para identificar alguma falha do servidor
    received = str(sock.recv(1024),"utf-8")
    print(received)
else:
	print('Timeout')