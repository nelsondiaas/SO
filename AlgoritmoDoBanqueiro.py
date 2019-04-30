class AlgoritmoDoBanqueiro:
    def __init__(self):
        self.recursosExistentes = []
        self.recursosDisponiveis = None
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

        self.recursosDisponiveis = list(self.recursosExistentes)
        self.criandoMatrizDeAlocacaoCorrente()
        self.controllerProcessosRecursos()
        #print(self.recursosExistentes)

    def criandoMatrizDeAlocacaoCorrente(self):
        qntProcessos = int(input("\nDigite a quantidade de processos: "))
        self.quantidadeDeProcesos = qntProcessos
        for processo in range(self.quantidadeDeProcesos):
            self.adicionarRecursosProcesso('p'+str(processo+1))
        #print(self.processos)

    def controllerProcessosRecursos(self):
        for processo in range(len(self.processos)):
            for recurso in range(len(self.recursosExistentes)):
                verifica = False
                while(verifica != True):
                    processoImprimir = self.processos[processo].copy().popitem()[0]
                    recursoImprimir = self.recursosExistentes[recurso].copy().popitem()[0]

                    recursoSolicitado = int(input("Digite a quantidade de recurso [{}] do [{}]: ".format(recursoImprimir, processoImprimir)))
                    print("\nprocesso: {}\nrecurso: {}".format(self.recursosExistentes[recurso].copy().popitem()[0], self.processos[processo].copy().popitem()[1][recurso].copy().popitem()[0]))
                    recursoExistente = self.recursosExistentes[recurso].copy().popitem()[0]
                    processoRecurso = self.processos[processo].copy().popitem()[1][recurso].copy().popitem()[0]
                    if recursoExistente == processoRecurso:
                        print("recursos iguais")
                        print(self.recursosDisponiveis[recurso].copy().popitem()[1])
                        if recursoSolicitado <= self.recursosDisponiveis[recurso].copy().popitem()[1]:
                            self.processos[processo][processoImprimir][recurso][recursoImprimir] = recursoSolicitado
                            verifica = True
                            print("RECURSO DISPONIVEL")
                            print(self.processos)

                        elif self.recursosDisponiveis[recurso].copy().popitem()[1] == 0:
                            self.processos[processo][processoImprimir][recurso][recursoImprimir] = 0
                            verifica = True

                        else:
                            print("Quantidade de recurso disponivel em [{}] de [{}] => {}".format(recursoImprimir, processoImprimir, self.recursosDisponiveis[recurso].copy().popitem()[1]))
    '''
    Falta decrementar em self.recursosDisponiveis o recursoSolicitado.

    
    '''


if __name__ == '__main__':
    AlgoritmoDoBanqueiro().orquestrador()