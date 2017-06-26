from tools.gerador import Gerador
from tools.logger import Logger
from tools.tabvalues import Tabvalues
from model.thre import Thre
from model.recovery import Recovery
import time

class Core():

    def __init__(self):
        self.gerador = Gerador()
        self.tab = Tabvalues()
        self.active_tran = []
        self.lis_transacoes = {} #{T:[VARIAVEL,VALOR ANT, VALOR DP]}
        self.logger = Logger(self.tab, self)

    def transacoes(self):
        x = 0
        self.logger.clean()
        while(self.logger.crash_flag == 0):
            self.get_transacao()
            if self.logger.crash_flag == 1:
                return
            t = Thre(self,x)
            t.start()
            x+=1

    def get_transacao(self):
        if self.gerador.list:
            return
        else:
            time.sleep(1)
            self.get_transacao()

    def recovery(self, lines):
        rec = Recovery(lines, self.lis_transacoes,self)
        rec.start()
