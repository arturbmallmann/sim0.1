#!/usr/bin/python3
import sys
medicos = 3
atendentes = 2

class Cliente:
	def __init__(self,chegada,ficha,consulta,pagamento):
		self.chegada=chegada
		self.ficha=ficha
		self.consulta=consulta
		self.pagamento=pagamento

		self.espera=0
		self.atendimento=0
	def esperar(self):
		self.espera+=1
	def pronto(self):
		return self.consulta == self.atendimento
	def consultar(self):
		self.atendimento+=1
		return self.pronto()
	def __str__(self):
		return str.format("(c:{} f:{} c:{} p:{})", self.chegada,self.ficha,self.consulta,self.pagamento)
	def __repr__(self):
		return self.__str__()
	def __unicode__(self):
		return self.__str__()
class Dummy: #singleton
	_instance = None
	def __new__(cls):
		if cls._instance is None:
			print('Creating the object')
			cls._instance = super(Dummy, cls).__new__(cls)
			# Put any initialization here.
		return cls._instance
	def pronto(self):
		return True
	def consultar(self):
		return True

class Entidade:
	def __init__(self, atendentes):
		self.atendentes = atendentes
		self.consultas = [Dummy()]*atendentes #0 == medico livre
	def VerificaDisp(self):
		return False if self.consultas.index(Dummy()) != -1 else True
	def Atender(self,paciente):
		indice = self.consultas.index(Dummy()) #retorna o slot do primeiro medico livre, muito mais rapido que percorrer tudo
		self.consultas[indice]
	def Consultar(self):
		self.consultas = [x-1 for x in self.consultas]
#simulacao
def simulacao(entradas):
	tempo = 0
	(chegada,ficha,consulta,pagamento) = entradas
	pacientes = [Cliente(a,b,c,d) for a,b,c,d in zip(chegada,ficha,consulta,pagamento)]
	filas = {'balcao':[],'consulta':[]}
	balcao = Entidade(atendentes)
	medicos = Entidade(atendentes)
	print (pacientes, file=sys.stderr)
	while (tempo < 100):
		balcao.VerificaDisp()
		tempo+=1

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

	fixas = (chegada,ficha,consulta,pagamento)


	simulacao(fixas)
if __name__ == "__main__":
	main()
