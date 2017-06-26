import os
from random import randint


class Logger:
    def __init__(self, tab,core, prob=None):
        self.dir = '{0}/arquivos/log.txt'.format(os.getcwd())
        self.crash_flag = 0
        self.tab = tab
        self.core = core
        self.count = 0
        if not prob:
            prob = 3
        self.prob = prob

    def new_line(self, oper,recover=False):
        """
            params oper: Dados da Operaçao em lista no formato [K,T,V,A,D] onde:
            K = Tipo da transação (s = start, w = write, c = commit)
            T = Nome de transação
            V = Variavel
            A = Valor antes da transação
            D = Valor depois da transação
        """

        if not recover:
            if self.count == 5:
                self.count = 0
                arch = open(self.dir,'a')
                arch.write(self.active())
                arch.close()

            if self.crash_flag ==1:
                return
            self.crash()
            self.count += 1

        arch = open(self.dir, 'a')
        arch.write(self.params(oper))
        arch.close()

    def params(self, oper):
        st = ''
        if oper[0] == 's':
            st = "<start {0}>\n".format(oper[1])

        elif oper[0] == 'c':
            st = "<commit {0}>\n".format(oper[1])
            self.core.tab.set_banco(oper[2],oper[3])

        else:
            oper.pop(0)
            st = "<write {0},{1},{2},{3}>\n".format(*oper)
            self.core.tab.set_atual(oper[1], oper[3])

        return st

    def active(self):
        ls = self.core.active_tran.copy()
        ls.reverse()
        t = ls.pop()
        for x in ls:
            t = t + ',{0}'.format(x)
        return '<checkpoint {0}>\n'.format(t)

    def clean(self):
        arch = open(self.dir, 'w')
        arch.write('')
        arch.close()

    def crash(self):
        c = randint(0, 100)
        if c <= self.prob:
            self.crash_flag = 1
            print("Devido a um crash, o banco pode estar inconsistente.")
            print("Verifique o log.txt para mais informações.\n")

            print("Estado atual do banco")
            self.tab.show()
            arch = open(self.dir, 'a')
            arch.write("{0}Crash!{1}\n".format('*'*5, '*'*5))
            arch.close()

            arch = open(self.dir, 'r')
            lines = arch.readlines()
            lines.reverse()
            self.core.recovery(lines)

    def add_line(self,text):
        arch = open(self.dir, 'a')
        arch.write(text)
        arch.close()
