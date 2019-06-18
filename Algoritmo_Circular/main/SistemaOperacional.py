from datastructure.Fila import Fila
from models.Processo import Processo
from utils.ui import *


class SistemaOperacional:
    def __init__(self):
        self.fila = Fila()
        self.finalizados = []

    def verificarFinalizados(self):
        for i in self.finalizados:
            print("\nNome: {}\nTempo espera: {}\nTempo execução: {}".format(i.nomeProcesso, i.tempoDeEspera, i.tempoDeExecucao))

    def cpu(self):
        if len(self.finalizados) != self.qntProcesso:
            for processo in range(self.qntProcesso):
                atualProcesso = self.fila.pop()
                tempoDeExecucaoFinal = atualProcesso.tempoProcesso

                if self.fila.tamanho() == 0: #Se for o ultimo processo na fila
                    atualProcesso.ultimoExecutando(tempoDeExecucaoFinal)
                    atualProcesso.execucaoFinalizada()
                    printProcesso(atualProcesso.nomeProcesso, atualProcesso.tempoProcesso, atualProcesso.controllerTempoProcesso, atualProcesso.tempoDeEspera, tempoDeExecucaoFinal)
                    self.finalizados.append(atualProcesso)
                    break
                else:
                    tempoDeExecucao = atualProcesso.executando()
                    atualProcesso.incrementarTempoDeEspera(self.fila.fila, tempoDeExecucao)
                    printProcesso(atualProcesso.nomeProcesso, atualProcesso.tempoProcesso, atualProcesso.controllerTempoProcesso, atualProcesso.tempoDeEspera, tempoDeExecucao)

                    if atualProcesso.tempoDeExecucao == atualProcesso.controllerTempoProcesso:
                        atualProcesso.execucaoFinalizada()
                        self.finalizados.append(atualProcesso)
                    else:
                        atualProcesso.execucaoFinalizada()
                        self.fila.push(atualProcesso)
            self.cpu()

    def main(self):
        quantum = int(input("Digite a quantidade do quantum: "))
        tempoTrocaContexto = int(input("Digite o tempo de troca de contexto: "))
        self.qntProcesso = int(input("\nQuantidade de processos: "))

        for processo in range(self.qntProcesso):
            nomeProcesso = input("\nDigite o nome do processo: ")
            tempoProcesso = int(input("Digite a quantidade de tempo do processo: "))
            self.fila.push(Processo(nomeProcesso, tempoProcesso, quantum, tempoTrocaContexto))
        self.cpu()
        self.verificarFinalizados()
        

if __name__ == '__main__':
    SistemaOperacional().main()
