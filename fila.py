import sys


tempo=0;

medicos = 3
atendentes = 2

class Cliente:
	def __init__(self,chegada,eletronico,caixa,gerente):
		self.chegada=chegada
		self.eletronico=eletronico
		self.caixa=caixa
		self.gerente=gerente

class Entidade:
	def __init__(self, atendentes):
		self.atendentes = atendentes
		self.consultas = [0]*atendentes #0 == medico livre
	def VerificaDisp(self):
		return True if self.consultas.index(0) != -1 else False 
	def Atender(self,tempo):
		indice = self.consultas.index(0) #retorna o slot do primeiro medico livre
		self.consultas[indice]
	def Consultar(self):
		self.consultas = [x-1 for x in self.consultas]
#simulacao
def simulacao(entradas):
	(chegada,ficha,consulta,pagamento) = entradas
	pacientes = [(a,b,c,d) for a,b,c,d in zip(chegada,ficha,consulta,pagamento)]
	filas = {'balcao':[],'consulta':[]}
	balcao = Entidade(atendentes)
	medicos = Entidade(atendentes)

	while (tempo < 100):
		balcao.VerificaDisp()

def main():
	print("insira os tempos que cada paciente leva:",file=sys.stderr)
	print("chegada:",file=sys.stderr)
	le = input()
	chegada = le.split(',')
	print("ficha:",file=sys.stderr)
	le = input()
	ficha = le.split(',')

	print("consulta:",file=sys.stderr)
	le = input()
	consulta = le.split(',')

	print("pagamento:",file=sys.stderr)
	le = input()
	pagamento = le.split(',')
	espera = [0] * len(chegada)

	entradas = (chegada,ficha,consulta,pagamento)


	simulacao(fixas)
if __name__ == "__main__":
	main()
