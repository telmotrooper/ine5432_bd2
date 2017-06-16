from tools.gerador import Gerador
from tools.logger import Logger

class Core():

    def __init__(self):
        self.gerador = Gerador()
        self.logger = Logger()
        self.var = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0}

    def ex_trans(self,n):
        k = self.gerador.gerar()
        t = 'T' + str(n)
        self.logger.new_line(['s',t])
        self.logger.new_line(['w',t,k[0],self.var[k[0]],k[1]])
        self.logger.new_line(['c',t])
        self.gerador.add(k[0])
        self.var[k[0]] = k[1]
