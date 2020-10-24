#!/usr/bin/python3
import math
import numpy as np
import sys

def export_csv(mylist):
	return ', '.join([str(x) for x in mylist])

class monteCarlo:
	def __init__(self, classes, entradas):
		self.classes = classes
		self.entradas = entradas
		self.delta = (self.get_max() - self.get_min()) / self.classes 
		print(self.delta,file=sys.stderr)
		cla = [0]*self.classes
		increment = [math.floor( ((x if x < self.get_max() else x-0.1) - self.get_min()) / self.delta) for x in entradas] #if para puxar o de valor máximo para a ultima classe
		self.freq_count = list()
		self.pms = list()
		self.freq = list()
		self.freq_acum = list()
		print(str.format("classes: {}\ndelta: {}",self.classes,self.delta),file=sys.stderr)
		for b in range(self.classes):
			self.freq_count += [increment.count(b)]
			self.pms += [self.get_min() + self.delta*b + self.delta/2 ]
		
		sum_count = sum(self.freq_count)
#		sum_intv = 0
		for b in self.freq_count:
			self.freq += [b/sum_count]
			self.freq_acum += [sum(self.freq)]

		print(str.format("increment: {}\nfreq:{}\npms:{}",increment,self.freq_acum,self.pms),file=sys.stderr)
	def get_max(self):
		return max(self.entradas)
	def get_min(self):
		return min(self.entradas)
	def get_rand(self):
		rnd = np.random.rand()
		for i in range(self.classes):
			if rnd < self.freq_acum[i]:
				return self.pms[i]
		return self.classes - 1
	def gen_sim(self,size):
		return [self.get_rand() for i in range(size)]

def main():
	amostras = [int(x) for x in input("amostras: ").split(',')]
	classes = int(input("Numero de classes: "))
	entradas = int(input("tamanho da simulação: "))
	mc = monteCarlo(classes,amostras)
#mc = monteCarlo(4,[1,1,3.5,6,5.9999,3,3.49]) #testes
	print(export_csv(mc.gen_sim(entradas)))
#print(export_csv(mc.gen_sim(20)))

if __name__ == "__main__":
	main()
