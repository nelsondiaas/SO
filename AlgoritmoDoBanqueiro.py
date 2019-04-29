class AlgoritmoDoBanqueiro:
    def __init__(self):
        self.recursosExistentes = []
        self.recursosDisponiveis = []
        self.processos = []
        self.quantidadeTiposDeRecursos = 0
        self.quantidadeDeProcesos = 0

    def adicionarResursosExistentes(self, nomeRecurso, qntRecurso):
        self.recursosExistentes.append({'{}'.format(nomeRecurso): qntRecurso})

    def adicionarRecursosProcesso(self, nomeProcesso):
        self.processos.append({'{}'.format(nomeProcesso): list(self.recursosExistentes)})

    def orquestrador(self):
        recursoQuantidade = int(input("Digite a quantidade de tipos de recursos: "))
        self.quantidadeTiposDeRecursos = recursoQuantidade
        for recurso in range(self.quantidadeTiposDeRecursos):
            nomeRecurso = input("\ndigite o nome do recurso [{}]: ".format(recurso+1))
            quantidadeRecurso = int(input("Digite a quantidade recurso: "))
            self.adicionarResursosExistentes(nomeRecurso, quantidadeRecurso)
        self.criandoMatrizDeAlocacaoCorrente()

    def criandoMatrizDeAlocacaoCorrente(self):
        qntProcessos = int(input("Digite a quantidade de processos: "))
        self.quantidadeDeProcesos = qntProcessos
        for processo in range(self.quantidadeDeProcesos):
            self.adicionarRecursosProcesso('p'+str(processo+1))
        print(self.processos)


if __name__ == '__main__':
    AlgoritmoDoBanqueiro().orquestrador()