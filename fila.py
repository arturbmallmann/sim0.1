#!/usr/bin/python3
import sys
medicos = 3
atendentes = 2


class cli:
	def pronto(self):
		pass
	def consultar(self):
		pass

class Cliente(cli):
	def __init__(self,chegada,ficha,consulta,pagamento):
		self.chegada=chegada
		self.ficha=ficha
		self.consulta=consulta
		self.pagamento=pagamento

		self.atendimento=0
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

class Dummy(cli): #singleton
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
	def __init__(self, n_at):
		self.n_at = n_at
		self.atendentes = [Dummy()]*n_at #0 == medico livre
		self.fila = []
	def VerificaDisp(self):
		return False if self.atendentes.index(Dummy()) != -1 else True
	def AtenderProx(self):
		indice = self.atendentes.index(Dummy()) #retorna o slot do primeiro medico livre, muito mais rapido que percorrer tudo
		self.consultas[indice] = self.fila.pop(0)
	def Entrar_na_fila (self,time,dest,cli_data): #hora q entrou na fila, destino(consulta ou sair) e dados do cliente
		fila.append((time,dest,cli_data))
		fila.sort(key= lambda x: x.time)
		print("fila em ordem: {}".format(self.fila))
		

#simulacao
def simulacao(entradas):
	(chegada,ficha,consulta,pagamento) = entradas
	pacientes = [Cliente(float(a),float(b),float(c),float(d)) for a,b,c,d in zip(chegada,ficha,consulta,pagamento)]
	pacientes.sort(key= lambda paciente : paciente.chegada)
#	filas = {'balcao':[],'consulta':[]}
	balcao = Entidade(atendentes)
	clinica = Entidade(medicos)
	print (pacientes, file=sys.stderr)
	#while (tempo < 100):
		
	#	balcao.VerificaDisp()



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
	
	fixas = (chegada,ficha,consulta,pagamento)
	simulacao(fixas)

if __name__ == "__main__":
	main()
