from models.Processo import Processo
from datastructure.Fila import Fila
from utils.ui import *


class SistemaOperacional:
    def __init__(self):
        self.fila = Fila()
        self.finalizados = []

    def tempoMedioEsperaTurnaround(self):
        dicionario = {"tempoMedioEspera": 0, "tempoDeTurnaround": 0}
        for processo in self.finalizados:
            dicionario["tempoMedioEspera"] += processo.tempoDeEspera
            dicionario["tempoDeTurnaround"] += (processo.tempoDeEspera + processo.controllerTempoProcesso)
        dicionario["tempoMedioEspera"] = (dicionario["tempoMedioEspera"] / self.qntProcesso)
        dicionario["tempoDeTurnaround"] = (dicionario["tempoDeTurnaround"] / self.qntProcesso)
        return dicionario

    def cpu(self):
        if len(self.finalizados) != self.qntProcesso:
            for processo in range(self.qntProcesso):
                printFila(self.fila.fila)
                atualProcesso = self.fila.pop()
                tempoDeExecucaoFinal = atualProcesso.tempoProcesso

                if atualProcesso.quantum == 0 and atualProcesso.tempoTrocaContexto == 0:
                    atualProcesso.quantumTrocaContextoZero(self.fila.fila)
                    printProcesso(atualProcesso.nomeProcesso, atualProcesso.tempoProcesso, atualProcesso.tempoProcesso, 0, atualProcesso.controllerTempoProcesso,atualProcesso.tempoDeEspera, atualProcesso.tempoProcesso)
                    self.finalizados.append(atualProcesso)

                elif self.fila.tamanho() == 0: #Se for o ultimo processo na fila
                    atualProcesso.swapUltimoTempoExecucao(tempoDeExecucaoFinal)
                    atualProcesso.ultimoExecutando(tempoDeExecucaoFinal)
                    printProcesso(atualProcesso.nomeProcesso, self.tempoDeExecucao, self.valorAntigoTempoProcesso,atualProcesso.tempoProcesso, atualProcesso.controllerTempoProcesso,atualProcesso.tempoDeEspera, tempoDeExecucaoFinal)
                    self.finalizados.append(atualProcesso)
                    break
                else:
                    self.valorAntigoTempoProcesso = atualProcesso.tempoProcesso
                    self.tempoDeExecucao = atualProcesso.executando()
                    printProcesso(atualProcesso.nomeProcesso, self.tempoDeExecucao, self.valorAntigoTempoProcesso,atualProcesso.tempoProcesso, atualProcesso.controllerTempoProcesso,atualProcesso.tempoDeEspera, self.tempoDeExecucao)
                    atualProcesso.incrementarTempoDeEspera(self.fila.fila, self.tempoDeExecucao)

                    if atualProcesso.tempoDeExecucao == atualProcesso.controllerTempoProcesso:
                        atualProcesso.swapUltimoTempoExecucao(tempoDeExecucaoFinal)
                        self.finalizados.append(atualProcesso)
                    else:
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
        printFinalizados(self.finalizados)
        printTempoMediaEsperaTurnaround(self.tempoMedioEsperaTurnaround())
        

if __name__ == '__main__':
    SistemaOperacional().main()
