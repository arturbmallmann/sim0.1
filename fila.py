#!/usr/bin/python3
import sys
medicos = 3
atendentes = 2


class Cli:
    def pronto(self):
        pass
    def consultar(self):
        pass

class Cliente(Cli):
    def __init__(self,chegada,ficha,consulta,pagamento):
        self.chegada=chegada
        self.at_caixa=-1
        self.fila_c1=-1
        self.ficha=ficha
        self.at_consulta=-1
        self.fila_c2=-1
        self.consulta=consulta
        self.pagamento=pagamento

        self.tempo_filas=0
        self.atendimento=0

    def pronto(self):
        return self.consulta == self.atendimento
    def consultar(self):
        self.atendimento+=1
        return self.pronto()
    def tempo_total(self):
            return self.tempo_filas + self.ficha + self.consulta + self.pagamento
    def __str__(self):
        return ','.join([str(x) for x in [self.chegada,self.at_caixa,self.fila_c1,self.ficha,self.at_consulta,self.fila_c2,self.pagamento]])
    def __repr__(self):
        return self.__str__()
    def __unicode__(self):
        return self.__str__()

class Dummy(Cli): #singleton
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
        self.atendentes = [Dummy()]*n_at #Dummy == entidade livre:ninguém
        self.fila = []
    def verif_disp(self):
        return False if self.atendentes.index(Dummy()) != -1 else True
    def atende_prox(self):
        indice = self.atendentes.index(Dummy()) #retorna o slot da primeira entidade livre
        if(self.fila.index(0)[0] == self.time):
            print(f"Atendendo cliente {self.fila.index(0)[2]}",file = sys.stderr) 
            self.consultas[indice] = self.fila.pop(0)
    def entra_na_fila (self,hora,dest,cli): #hora q entrou na fila, destino(1=consulta ou 0=sair) e dados do cliente
        self.fila.append((hora,dest,cli))
        self.fila.sort(key= lambda x: x[0])
#        print("fila em ordem: {}".format(self.fila),file = sys.stderr)
    def time(self,time):
        self.time = time

def simrun(entidade):
    pass

#simulacao
def simulacao(entradas):
    tempo = 0
    (chegada,ficha,consulta,pagamento) = entradas
    pacientes = [Cliente(float(a),float(b),float(c),float(d)) for a,b,c,d in zip(chegada,ficha,consulta,pagamento)]
    pacientes.sort(key= lambda paciente : paciente.chegada)
#    filas = {'balcao':[],'consulta':[]}
    balcao = Entidade(atendentes)
    clinica = Entidade(medicos)
    print (pacientes, file=sys.stderr)
    print ("chegada,at_caixa,fila_c1,ficha,at_consulta,fila_c2,pagamento")
    while (tempo < 100000):
#        print(tempo)
        indexes = [i for i,s in enumerate(pacientes) if s.chegada*1000==tempo]
        if(len(indexes)!= 0):
            print("entrou aqui {}".format(indexes))
            for i in indexes: balcao.entra_na_fila(pacientes[i].chegada,1,pacientes[i])
        if balcao.verif_disp():
            balcao.atende_prox()
    #    balcao.VerificaDisp()
        tempo += 1



# def main():
#     print("insira os tempos que cada paciente leva:",file=sys.stderr)
#     print("chegada:",file=sys.stderr)
#     le = input()
#     chegada = le.split(',')
#     print("ficha:",file=sys.stderr)
#     le = input()
#     ficha = le.split(',')

#     print("consulta:",file=sys.stderr)
#     le = input()
#     consulta = le.split(',')

#     print("pagamento:",file=sys.stderr)
#     le = input()
#     pagamento = le.split(',')
    
#     fixas = (chegada,ficha,consulta,pagamento)
#     simulacao(fixas)

# if __name__ == "__main__":
#     main()
