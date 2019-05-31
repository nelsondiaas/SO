from copy import deepcopy
from Cores import Cor


class AlgoritmoDoBanqueiro:
    def __init__(self):
        self.recursosDisponiveis = None
        self.recursosExistentes = []
        self.processosAlocacaoCorrente = []
        self.processoDeRequisicoes = []
        self.cor = Cor()

    def adicionarResursosExistentes(self, nomeRecurso, qntRecurso):
        self.recursosExistentes.append({'{}'.format(nomeRecurso): qntRecurso})

    def adicionarRecursosProcessoAlocacaoCorrente(self, nomeProcesso):
        self.processosAlocacaoCorrente.append({'{}'.format(nomeProcesso): deepcopy(self.recursosExistentes)})
        self.adicionarRecursosProcessoDeRequisicoes(nomeProcesso)

    def adicionarRecursosProcessoDeRequisicoes(self, nomeProcesso):
        self.processoDeRequisicoes.append([{'{}'.format(nomeProcesso): deepcopy(self.recursosExistentes)}, {'executado': False}])

    def imprimirMatriz(self, lista, nome, cor):
        print("\n-- {} --".format(self.cor.colorir(nome, 'branco')))
        for item in lista:
            for key in item:
                print("{}: {}".format(self.cor.colorir(key, cor), item[key]))

    def orquestrador(self):
        recursoQuantidade = int(input("Digite a quantidade de tipos de recursos: "))
        for recurso in range(recursoQuantidade):
            nomeRecurso = input("\ndigite o nome do recurso [{}]: ".format(recurso+1))
            quantidadeRecurso = int(input("Digite a quantidade recurso: "))
            self.adicionarResursosExistentes(nomeRecurso, quantidadeRecurso)

        self.recursosDisponiveis = deepcopy(self.recursosExistentes)
        self.imprimirMatriz(self.recursosExistentes, "RECURSOS EXISTENTES", 'azul')
        self.imprimirMatriz(self.recursosDisponiveis, "RECURSOS DISPONIVEIS", 'azul')
        self.criandoMatrizDeAlocacaoCorrente()
        self.controllerProcessosRecursos()
        self.controllerProcessosDeRequisicao()
        self.controllerDeadlock()

    def criandoMatrizDeAlocacaoCorrente(self):
        qntProcessos = int(input("\nDigite a quantidade de processos: "))
        for processo in range(qntProcessos):
            self.adicionarRecursosProcessoAlocacaoCorrente('p' + str(processo + 1))


    def controllerProcessosDeRequisicao(self):
        for processo in range(len(self.processoDeRequisicoes)):
            for recurso in range(len(self.recursosExistentes)):
                keyProcessoAlocacaoCorrente = self.processosAlocacaoCorrente[processo].copy().popitem()[0]
                keyRecursoAlocacaoCorrente = self.recursosExistentes[recurso].copy().popitem()[0]

                keyProcessoDeRequisicao = self.processoDeRequisicoes[processo][0].copy().popitem()[0]
                keyRecursoDeRequisicao = self.processoDeRequisicoes[processo][0][keyProcessoDeRequisicao][recurso].copy().popitem()[0]

                recursoSolicitado = int(input("\nDigite a quantidade de recurso do processo de requisiçao[{}] do [{}]: ".format(self.cor.colorir(keyRecursoDeRequisicao, 'azul'), self.cor.colorir(keyProcessoDeRequisicao, 'verde'))))

                if keyProcessoAlocacaoCorrente == keyProcessoDeRequisicao and keyRecursoAlocacaoCorrente == keyRecursoDeRequisicao:
                    self.processoDeRequisicoes[processo][0][keyProcessoDeRequisicao][recurso][keyRecursoDeRequisicao] = recursoSolicitado


    def controllerDeadlock(self):
        for processo in range(len(self.processoDeRequisicoes)):
            controller = 0
            for recurso in range(len(self.recursosDisponiveis)):
                keyProcessoDeRequisicao = self.processoDeRequisicoes[processo][0].copy().popitem()[0]
                keyRecursoDeRequisicao = self.processoDeRequisicoes[processo][0][keyProcessoDeRequisicao][recurso].copy().popitem()[0]

                valorRecursoRequisicao = self.processoDeRequisicoes[processo][0][keyProcessoDeRequisicao][recurso][keyRecursoDeRequisicao]
                boleanRecursoRequisicao = self.processoDeRequisicoes[processo][1]['executado']

                if valorRecursoRequisicao > self.recursosDisponiveis[recurso][keyRecursoDeRequisicao]:
                    controller += 0
                else:
                    controller += 1

            if controller == len(self.recursosDisponiveis):
                self.processoDeRequisicoes[processo][1]['executado'] = True

        print("\n{}".format(self.processoDeRequisicoes))

    def controllerProcessosRecursos(self):
        for processo in range(len(self.processosAlocacaoCorrente)):
            for recurso in range(len(self.recursosExistentes)):

                verifica = False
                while(verifica != True):
                    processoImprimir = self.processosAlocacaoCorrente[processo].copy().popitem()[0]
                    recursoImprimir = self.recursosExistentes[recurso].copy().popitem()[0]

                    self.imprimirMatriz(self.recursosDisponiveis, "RECURSOS DISPONIVEIS", 'azul')
                    recursoSolicitado = int(input("\nDigite a quantidade de recurso do processo de alocaçao corrente [{}] do [{}]: ".format(self.cor.colorir(recursoImprimir, 'azul'), self.cor.colorir(processoImprimir, 'verde'))))

                    recursoExistente = self.recursosExistentes[recurso].copy().popitem()[0]
                    processoRecurso = self.processosAlocacaoCorrente[processo].copy().popitem()[1][recurso].copy().popitem()[0]
                    if recursoExistente == processoRecurso:
                        if recursoSolicitado <= self.recursosDisponiveis[recurso].copy().popitem()[1]:
                            self.processosAlocacaoCorrente[processo][processoImprimir][recurso][recursoImprimir] = recursoSolicitado
                            self.recursosDisponiveis[recurso][recursoImprimir] = self.recursosDisponiveis[recurso][recursoImprimir] - recursoSolicitado
                            verifica = True

                        elif self.recursosDisponiveis[recurso].copy().popitem()[1] == 0:
                            self.processosAlocacaoCorrente[processo][processoImprimir][recurso][recursoImprimir] = 0
                            verifica = True

                        else:
                            print("\nQuantidade de recurso disponivel em [{}] do [{}] => {}".format(self.cor.colorir(recursoImprimir, 'azul'), self.cor.colorir(processoImprimir, 'verde'), self.recursosDisponiveis[recurso].copy().popitem()[1]))

        self.imprimirMatriz(self.processosAlocacaoCorrente, "PROCESSOS RECURSOS", 'verde')
        self.imprimirMatriz(self.recursosDisponiveis, "RECURSOS DISPONIVEIS", 'azul')



if __name__ == '__main__':
    AlgoritmoDoBanqueiro().orquestrador()