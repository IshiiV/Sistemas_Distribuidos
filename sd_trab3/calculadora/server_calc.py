import Pyro4

# classe contendo metodo de cálculo usado pelos clientes remotamente

@Pyro4.expose
class Calculadora(object):
    def operacao(self, op, num1, num2):
    	if int(op) == 1:
    		return int(num1) + int(num2)
    	if int(op) == 2:
    		return int(num1) - int(num2)
    	if int(op) == 3:
    		return int(num1) * int(num2)
    	if int(op) == 4:
    		return int(num1) / int(num2)

daemon = Pyro4.Daemon() # construção do daemon do Pyro

ns = Pyro4.locateNS() # conexão com o servidor de nomes

uri = daemon.register(Calculadora) # registro de objeto Pyro da classe Calculadora

ns.register("remote.calculadora", uri) # registro do objeto com o nome remote.calculadora no servidor de nomes. O cliente agora precisa deste nome para alcançar o objeto remoto e utilizar seus métodos

print("Servidor funcionando")

daemon.requestLoop() # inicia o servidor para que receba chamada de clientes