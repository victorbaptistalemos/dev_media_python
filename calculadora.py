class Calculadora:
    __RENDIMENTO_TINTA = 10.0
    __area_paredes: float
    __area_teto: float
    __litro_rendimento: float

    def __init__(self, comodo):
        self.calcular_area_paredes(comodo)
        self.calcular_area_teto(comodo)
        self.calcular_rendimento_tinta()

    def calcular_area_paredes(self, comodo):
        self.__area_paredes = 2 * (comodo.largura + comodo.profundidade) * comodo.ALTURA

    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade

    def calcular_rendimento_tinta(self):
        self.__litro_rendimento = (self.__area_teto + self.__area_paredes) / self.__RENDIMENTO_TINTA

    def get_area_parede(self):
        return self.__area_paredes

    def get_area_teto(self):
        return self.__area_teto

    def get_litro_rendimento(self):
        return self.__litro_rendimento
