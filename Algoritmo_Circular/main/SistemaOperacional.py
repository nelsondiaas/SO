from datastructure.Fila import Fila
from models.Processo import Processo


class SistemaOperacional:
    def __init__(self):
        self.fila = Fila()

    def main(self):
        quantum = int(input("Digite a quantidade do quantum: "))
        tempoTrocaContexto = int(input("Digite o tempo de troca de contexto: "))
        qntProcesso = int(input("\nQuantidade de processos: "))

        for processo in range(qntProcesso):
            nomeProcesso = input("\nDigite o nome do processo: ")
            tempoProcesso = int(input("Digite a quantidade de tempo do processo: "))
            self.fila.push(Processo(nomeProcesso, tempoProcesso, quantum, tempoTrocaContexto))
        self.verificarFila()

    def verificarFila(self):
        for i in self.fila.imprimirFila():
            print(i)


if __name__ == '__main__':
    SistemaOperacional().main()
