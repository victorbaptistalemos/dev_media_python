class Comodo:
    __largura: float
    __profundidade: float
    __ALTURA = 2.9

    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except ValueError:
            print('O Valor da Largura é inválido')
            exit()

    @property
    def profundidade(self):
        return self.__profundidade

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except ValueError:
            print('O Valor da Profundidade é inválido')
            exit()

    @property
    def altura(self):
        return self.__ALTURA
