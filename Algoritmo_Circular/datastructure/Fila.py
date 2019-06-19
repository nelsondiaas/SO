class Fila:
    def __init__(self):
        self.fila = []

    def tamanho(self):
        return len(self.fila)

    def inicio(self):
        return self.fila[0]

    def fim(self):
        return self.fila[len(self.fila) - 1]

    def push(self, procesoo):
        self.fila.append(procesoo)

    def pop(self):
        aux = self.inicio()
        self.fila.remove(self.inicio())
        return aux


