class Processo:
    def __init__(self, nomeProcesso, tempoProcesso, quantum, tempoTrocaContexto):
        self.nomeProcesso = nomeProcesso
        self.tempoProcesso = tempoProcesso
        self.quantum = quantum
        self.tempoTrocaContexto = tempoTrocaContexto
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
