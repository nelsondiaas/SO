
class Processo:
    def __init__(self, nomeProcesso, tempoProcesso, quantum, tempoTrocaContexto):
        self.nomeProcesso = nomeProcesso
        self.tempoProcesso = tempoProcesso
        self.quantum = quantum
        self.tempoTrocaContexto = tempoTrocaContexto
        self.controllerTempoProcesso = tempoProcesso
        self.tempoDeEspera = 0
        self.tempoDeExecucao = 0
        self.ultimoTempoDeExecucao = 0

    def __str__(self):
        return self.nomeProcesso.upper()

    def swapUltimoTempoExecucao(self, ultimoTempo):
        self.ultimoTempoDeExecucao = ultimoTempo

    def executando(self):
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
        self.tempoProcesso -= tempoDeExecucaoFinal
        self.tempoDeExecucao += tempoDeExecucaoFinal

    def incrementarTempoDeEspera(self, fila, tempoDeExecucao):
        for processo in fila:
            processo.tempoDeEspera += (tempoDeExecucao + self.tempoTrocaContexto)
        if len(fila) != 0:
            self.tempoDeEspera += self.tempoTrocaContexto


'''
No metodo 'incrementarTempoDeEspera', recebemos a fila (observe que a fila atualmente esta sem o Processo
que esta executando, pois aplicamos um 'pop' nele), em cada processo da fila, temos que incrementar ao
'TempoDeEspera' o 'TempoDeExecucao' (recebido como parametro) e o 'tempoTrocaContexto', ja que os processos
que nao estao sendo executados devem ser incrementados com o tempo do que esta sendo executado juntamente
com o tempo de troca de contexto que e aplicado antes dele finalizar. Ao final, caso o processo que esta
sendo executado seja o ultimo (por isso e verificado se a fila esta vazia), nao e necessario adicionar ao
tempoDeEspera dele o tempo de troca de contexto, ja que ele nao sera trocado por outro processo, ja se ele
nao for o ultimo, e necessario adicionar ao tempoDeEspera dele o tempo de troca de contexto, ja que ele
tambem entra em espera nesse momento.

'''
        

