from utils.Cores import Cor
import time

cor = Cor()


def tempo():
    time.sleep(2)


def printProcesso(nomeProcesso, tempoDeExecucao, valorAntigoTempoProcesso, tempoProcesso, controllerTempoProcesso, tempoDeEspera, repeteTempoDeExecucao):
    tempo()
    print(cor.colorir("\n*---------- PROCESSO {}{} ----------*".format(cor.colorir(nomeProcesso.upper(), "azul"), cor.colorir("", "branco")), "branco"))
    print(cor.colorir("Tempo processo: ({} - {}) = {}/{}{}"
                      "\nTempo de espera: {}"
                      "\nTempo de execução: {}".format(tempoDeExecucao, valorAntigoTempoProcesso, tempoProcesso, cor.colorir(str(controllerTempoProcesso), "branco"), cor.colorir("", "verde"), tempoDeEspera, repeteTempoDeExecucao), "verde"))

def printFinalizados(lista):
    for item in lista:
        print(cor.colorir("\n*-------- FINALIZADO PROCESSO {}{}--------*".format(cor.colorir(item.nomeProcesso.upper(), "vermelho"), cor.colorir("", "branco")), "branco"))
        print(cor.colorir("Tempo processo: {}"
                          "\nTempo espera: {}"
                          "\nUltimo tempo de execução: {}".format(item.controllerTempoProcesso, item.tempoDeEspera, item.ultimoTempoDeExecucao), 'azul'))

def printTempoMediaEsperaTurnaround(dicionario):
    print(cor.colorir("\n*-------- {}TEMPO MEDIO DE ESPERA & TURNAROUND{} --------*".format(cor.colorir("", "vermelho"), cor.colorir("", "branco")), "branco"))
    print(cor.colorir("Tempo medio de espera: {}\nTempo de turnaround: {:.2f}".format(dicionario["tempoMedioEspera"], dicionario["tempoDeTurnaround"]), "amarelo"))

def printFila(fila):
    print(cor.colorir("\n*------------- {}FILA{} --------------*".format(cor.colorir("", "vermelho"), cor.colorir("", "branco")),"branco"))
    for item in range(len(fila)):
        if item == 0:
            print("[{}]".format(cor.colorir(str(fila[item]), "azul")), end="")
        elif item == len(fila) - 1:
            print("[{}]".format(cor.colorir(str(fila[item]), "vermelho")))
        else:
            print("[{}]".format(str(fila[item])), end="")