from tabulate import tabulate


class Tabvalues(object):
    def __init__(self):
        self.table = {
        'A':{'banco': 0, 'esperado':0},
        'B':{'banco': 0, 'esperado':0},
        'C':{'banco': 0, 'esperado':0},
        'D':{'banco': 0, 'esperado':0},
        'E':{'banco': 0, 'esperado':0},
        'F':{'banco': 0, 'esperado':0},
        'G':{'banco': 0, 'esperado':0}
        }

    def show(self):
        tab = []
        for key, value in sorted(self.table.items()):
            tab.append([key, value['banco'], value['esperado']])

        headers = ["Variavel", "Banco", "Valor"]
        out = tabulate(tab, headers, numalign="center", tablefmt='psql')
        print(out)
        return out

    def atual(self, key):
        return self.table[key]['banco']

    def set_banco(self,key,value):
        self.table[key]['banco'] = value

    def set_atual(self,key,value):
        self.table[key]['esperado'] = value
