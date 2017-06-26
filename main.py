from model.core import Core

print("Recovery UNDO/REDO com checkpoint\n")
print("Aguarde enquanto as transações são geradas e escalonadas...")
c = Core()
c.transacoes()
