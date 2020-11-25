class Calculadora:
    __RENDIMENTO_TINTA = 10.0
    __area_paredes: float
    __area_teto: float
    __rendimento_tinta: float

    def __init__(self, comodo):
        self.rendimento_tinta = comodo

    @property
    def area_paredes(self):
        return self.__area_paredes

    @area_paredes.setter
    def area_paredes(self, comodo):
        self.__area_paredes = 2 * (comodo.largura + comodo.profundidade) * comodo.altura

    @property
    def area_teto(self):
        return self.__area_teto

    @area_teto.setter
    def area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade

    @property
    def rendimento_tinta(self):
        return self.__rendimento_tinta

    @rendimento_tinta.setter
    def rendimento_tinta(self, comodo):
        self.area_paredes = comodo
        self.area_teto = comodo
        try:
            if self.area_teto <= 0 or self.area_paredes <= 0:
                raise UserWarning('Não foi possível calcular a litragem com os valores informados')
            else:
                self.__rendimento_tinta = (self.area_teto + self.area_paredes) / self.__RENDIMENTO_TINTA
        except UserWarning as e:
            print(e)
            exit()
