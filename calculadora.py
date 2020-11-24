from comodo import Comodo


class Calculadora(Comodo):
    RENDIMENTO_TINTA = 10.0
    area_paredes: float
    area_teto: float
    litro_rendimento: float

    def __init__(self, largura, profundidade):
        self.calcular_area_paredes(largura, profundidade, self.ALTURA)
        self.calcular_area_teto(largura, profundidade)
        self.calcular_rendimento_tinta()

    def calcular_area_paredes(self, largura, profundidade, altura):
        self.area_paredes = 2 * (largura + profundidade) * altura

    def calcular_area_teto(self, largura, profundidade):
        self.area_teto = largura * profundidade

    def calcular_rendimento_tinta(self):
        self.litro_rendimento = (self.area_teto + self.area_paredes) / self.RENDIMENTO_TINTA
