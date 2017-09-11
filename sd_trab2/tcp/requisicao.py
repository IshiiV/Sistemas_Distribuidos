#a classe Requisicao possui metodo inicializador que recebe os 
#numeros da operação e a string relacionada com a operação que se quer
#tomar com esses números além de métodos para retornar os atributos
#da classe.

class Requisicao(object):

	def __init__(self, num1, num2, operacao):
		self.num1 = num1
		self.num2 = num2
		self.operacao = operacao
		#vlores possiveis de operação: 'soma', 'sub', 'div', 'multi'

	def get_op(self):
		return self.operacao
	def get_num1(self):
		return self.num1
	def get_num2(self):
		return self.num2