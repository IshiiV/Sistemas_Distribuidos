import socket
import sys
try:
    import cPickle as pickle
except:
    import pickle
import requisicao
import threading
import time
import random

#funçoes de cálculo
def soma(a,b):
	return a + b

def mult(a,b):
	return a * b

def subtr(a,b):
	return a - b

def divisao(a,b):
	return a / b

def operacao(obj): #função que retorna resposta da operação entre os números do objeto da classe Requisição
	if obj.get_op() == 'soma':
		return soma(obj.get_num1(), obj.get_num2())
	if obj.get_op() == 'sub':
		return subtr(obj.get_num1(), obj.get_num2())
	if obj.get_op() == 'div':
		return divisao(obj.get_num1(), obj.get_num2())
	if obj.get_op() == 'multi':
		return mult(obj.get_num1(), obj.get_num2())


def conexao(con, cliente): #função chamada por cada uma das threads

	while True:
		#sleep randomico para testar concorrencia
		time.sleep(1*random.random())
		
		#mensagem do cliente é extraida e transformada em objeto da classe Requisicao
		msg = con.recv(4096)
		if not msg: break
		requis = pickle.loads(msg)
		
		#atributos do objeto sao mostrados na tela
		print (cliente, requis.get_num1(), requis.get_num2(), requis.get_op())
		
		#ip do cliente é extraido
		ipcliente, idcl = cliente
		
		#a #mensagem e o ip do cliente são escritos no arquivo de log
		f.write('[%d %d %s][%s]\n' % (requis.get_num1(), requis.get_num2(), requis.get_op(), ipcliente))
		
		#resposta da operação é serializada e enviada ao cliente
		resposta = operacao(requis)
		msg2 = pickle.dumps(resposta)
		con.send(msg2)
		break
	#thread é encerrada
	print ('Finalizando conexao do cliente', cliente)
	con.close()

f = open('conexao_log.txt', 'w') #arquivo de log onde são gravadas as requisiçoes dos clientes

#argumento de entrada é extraidos e usado para informar a porta que o servidor ouve
PORT = int(sys.argv[1])
HOST = ''

#servidor abre conexão para clientes
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(5)

try:
	while True:
		#servidor se conecta com cliente
		con, cliente = tcp.accept()
		#thread é invocada e para tratar da operação requisitada pelo cliente
		threading.Thread(target = conexao, args = (con,cliente,)).start()

except KeyboardInterrupt: #para encerrar o servidor é necessário a shortcut ctrl+c
	tcp.close()