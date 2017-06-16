import random
from random import randint

class Gerador():
    def __init__(self):
        self.list = ['A','B','C','D','E','F','G']

    def gerar(self):
        """
            return: dic com formato x:n onde:
            x = Variavel da lista
            n = Numero aleatorio entre 0 e 100

            OBS: A variavel de retorno é retirada da lista
        """
        try:
            x = random.choice(self.list)
            self.list.remove(x)
            l = [x,randint(0,100)]
            return l
        except:
            print("Sem mais variaveis na lista")

    def add(self, v):
        """
            params v: Variavel a ser adicionada na lista
        """
        self.list.append(v)
