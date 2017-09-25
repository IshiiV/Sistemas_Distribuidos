import Pyro4

# cliente usa lookup para procurar o objeto remoto que possui o nome remote.claculadora no servidor de nomes do Pyro

calcular_result = Pyro4.Proxy("PYRONAME:remote.calculadora")

while True:

	# O programa pede ao usuário que forneça os dados da operacao matemática

	ope = input("Que operação deseja fazer?\n[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\nDigite o número da operação correspondente: ").strip()
	nume1 = input("Digite o primeiro número: ").strip()
	nume2 = input("Digite o segundo número: ").strip()

	# cliente envia os argumentos da operação para o método do objeto remoto e imprime na tela o resultado

	print("Resultado: ", calcular_result.operacao(ope,nume1,nume2))

	# o usuário pode fazer uma nova operação ou sair do programa

	contin = input("Deseja fazer outra operação? s/n: ").strip()
	if contin == 'n':
		break