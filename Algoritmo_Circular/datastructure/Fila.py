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

    def imprimirFila(self):
        return self.fila


if __name__ == '__main__':
    fila = Fila()
    fila.push(1)
    fila.push(2)
    fila.push(3)
    fila.push(4)
    fila.push(5)

    print(fila.imprimirFila())

    fila.push(fila.pop())

    print(fila.imprimirFila())