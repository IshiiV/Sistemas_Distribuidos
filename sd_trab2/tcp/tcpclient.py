import socket
import sys
try:
    import cPickle as pickle
except:
    import pickle
import requisicao

#argumentos de entrada sao extraidos e usados para informar ip do servidor, porta do servidor, números da operação e a operação
#essas informações são usadas para construir objeto da classe Requisicao, que será enviado ao servidor

HOST = sys.argv[1]
PORT = int(sys.argv[2])
requis = requisicao.Requisicao(int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])

#conexão é feita entre o cliente e o servidor requisitado por ele
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

#mensagem é serializada e enviada ao servidor
msg = pickle.dumps(requis)
tcp.send (msg)

#mensagem do servidor é recebida
msg2 = tcp.recv(1024)
resposta = pickle.loads(msg2)

#resposta da operação é mostrada
print ('resposta:', resposta)

#conexão é fechada e cliente é encerrado
tcp.close()