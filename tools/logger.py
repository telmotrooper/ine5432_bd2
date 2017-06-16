import os

class Logger():
    def __init__(self):
        self.dir = '{0}/arquivos/output.txt'.format(os.getcwd())

    def new_line(self, oper):
        """
            params oper: Dados da Operaçao em lista no formato [K,T,V,A,D] onde:
            K = Tipo da transação (s = start, w = write, c = commit)
            T = Nome de transação
            V = Variavel
            A = Valor antes da transação
            D = Valor depois da transação
        """
        arch = open(self.dir,'a')
        arch.write(self.params(oper))
        arch.close()

    def params(self, oper):
        st = ''
        if oper[0] == 's':
            st = "<start {0}>\n".format(oper[1])

        elif oper[0] == 'c':
            st = "<commit {0}>\n".format(oper[1])

        else:
            oper.pop(0)
            st = "<write {0},{1},{2},{3}\n".format(*oper)

        return st
