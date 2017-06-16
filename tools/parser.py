import os

class Parser():
    def __init__(self, file=None):
        if not file:
            file = '{0}/arquivos/input.txt'.format(os.getcwd())

        self.file = open(file,'r')
        self.list = self.get_lines()

    def get_lines(self):
        list = []
        for line in self.file:
            list.append(line.strip())
        return list

    def get_next_inst(self):
        try:
            return self.list.pop(0)
        except:
            print("Sem mais instruções!")
