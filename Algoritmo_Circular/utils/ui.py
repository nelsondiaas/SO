from utils.Cores import Cor

cor = Cor()


def printProcesso(nomeProcesso, tempoProcesso, controllerTempoProcesso, tempoDeEspera, tempoDeExecucao):
    print(cor.colorir("-------PROCESSO-------"
          "\nNome: {}"
          "\nTempo processo: {} / {}"
          "\nTempo de espera: {}"
          "\nTempo de execução: {}".format(nomeProcesso, tempoProcesso, controllerTempoProcesso, tempoDeEspera, tempoDeExecucao), "verde"))