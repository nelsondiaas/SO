class Processo:
    def __init__(self, nomeProcesso, tempoProcesso, quantum, tempoTrocaContexto):
        self.nomeProcesso = nomeProcesso
        self.tempoProcesso = tempoProcesso
        self.quantum = quantum
        self.tempoTrocaContexto = tempoTrocaContexto
        self.controllerTempoProcesso = tempoProcesso
        self.tempoDeEspera = 0
        self.tempoDeExecucao = 0
        self.status = False

    def __str__(self):
        return self.nomeProcesso

    def executando(self):
        self.status = True
        if self.tempoProcesso > self.quantum:
            self.tempoProcesso -= self.quantum
            self.tempoDeExecucao += self.quantum
            return self.quantum
        else:
            aux = self.tempoProcesso
            self.tempoDeExecucao += aux
            self.tempoProcesso = 0
            return aux

    def ultimoExecutando(self, tempoDeExecucaoFinal):
        self.status = True
        self.tempoProcesso -= tempoDeExecucaoFinal
        self.tempoDeExecucao += tempoDeExecucaoFinal

    def execucaoFinalizada(self):
        self.status = False

    def incrementarTempoDeEspera(self, fila, tempoDeExecucao):
        for processo in fila:
            if processo != self and processo.status != True:
                processo.tempoDeEspera += tempoDeExecucao

        

