import time


class Recovery:
    def __init__(self, lis, transacoes, core):
        self.lis = lis
        self.core = core
        self.transacoes = transacoes
        self.comitted = []
        self.redo = {}

    def start(self):
        time.sleep(2)
        print("Iniciando processo de recuperação...\n")
        start_time = time.time()
        # self.core.logger.add_line('Starting Recovery....\n')
        self.clean_list()
        # print(self.lis)
        # print(self.transacoes)
        for x in range(0, len(self.lis)):
            if 'commit' in self.lis[x]:
                self.register_commit(self.lis[x])

            if 'write' in self.lis[x]:
                self.recovery_write(self.lis[x])

        self.start_redo()
        print("Estado do banco após recovery")
        self.core.tab.show()
        exec_time = time.time()-start_time

        print("Tempo de execução do recovery: %.2f segundos\n" % exec_time)

    def clean_list(self):
        for x in range(0,len(self.lis)):
            if 'Crash' in self.lis[x]:
                self.lis = self.lis[x+1::]
                return

    def register_commit(self, line):
        self.comitted.append(line[8:10])

    def start_redo(self):
        self.comitted.reverse()
        for req in self.comitted:
            line = [req]
            line.extend(self.redo[req])
            time.sleep(0.5)
            self.core.logger.new_line(['s', line[0]], True)
            self.core.logger.new_line(['w', line[0], line[1], line[2], line[3]], True)
            self.core.logger.new_line(['c', line[0], line[1], line[3]], True)

    def recovery_write(self, line):
        line = line.split('<write ')[1].split('>')[0].split(',')
        if line[0] in self.comitted:
            self.redo.update({line[0]: line[1::]})
        else:
            self.core.logger.new_line(['s', line[0]], True)
            self.core.logger.new_line(['w', line[0], line[1], line[2], line[2]],True)
            self.core.logger.new_line(['c', line[0], line[1], line[2], line[2]], True)
