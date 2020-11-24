class Calculadora:
    ALTURA = 2.9
    area_paredes: float
    area_teto: float

    def calcular_area_paredes(self, largura, profundidade):
        self.area_paredes = 2 * (largura + profundidade) * self.ALTURA

    def calcular_area_teto(self, largura, profundidade):
        self.area_teto = largura * profundidade
