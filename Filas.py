class Queue:
    def __init__(self):
        self.fila = []

    def Inserir(self, n):
        self.fila.append(n)

    def Excluir(self):
        if len(self.fila) != 0:
            return self.fila.pop(0)

    def Vazio(self):
        return len(self.fila) == 0


fila = Queue()
fila.Inserir(1)
fila.Inserir(2)
fila.Inserir(3)
print(fila.Excluir())
print(fila.Vazio())
print(fila.Excluir())
print(fila.Vazio())
print(fila.Excluir())
print(fila.Vazio())