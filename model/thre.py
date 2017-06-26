import threading
from tools.gerador import Gerador
import time
from random import randint


class Thre (threading.Thread):

    def __init__(self, core, num):
        threading.Thread.__init__(self)
        self.gerador = Gerador()
        self.core = core
        self.num = num

    def run(self):
        k = self.core.gerador.gerar()
        if not k:
            return
        t = 'T' + str(self.num)
        self.core.lis_transacoes.update({t: [k[0], self.core.tab.atual(k[0]),k[1]]})

        time.sleep(randint(0, 3))
        self.core.logger.new_line(['s', t])
        self.core.active_tran.append(t)
        time.sleep(randint(0,3))
        self.core.logger.new_line(['w', t, k[0], self.core.tab.atual(k[0]) ,k[1]])
        time.sleep(randint(0,3))
        self.core.logger.new_line(['c', t, k[0], k[1]])
        self.core.active_tran.remove(t)
        self.core.gerador.add(k[0])
