class Cor:
    def __init__(self):
        self.off = '\33[0m'
        self.cores = {}
        self.cores['azul'] = '\33[1;34m'
        self.cores['amarelo'] = '\33[33m'
        self.cores['verde'] = '\33[1;32m'
        self.cores['vermelho'] = '\33[1;31m'
        self.cores['branco'] = '\33[1;30m'

    def colorir(self, arquivo, cor):
        return self.cores[cor] + arquivo + self.off

    def colorirBooleano(self, bool):
        if bool == True:
            return self.colorir("EXECUTADO", 'verde')
        else:
            return self.colorir("NAO EXECUTADO", 'vermelho')