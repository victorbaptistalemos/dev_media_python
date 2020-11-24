from calculadora import Calculadora

calc = Calculadora()
largura: float = float(input('Qual a largura do cômodo? '))  # Não fixa o tipo da váriável
profundidade = float(input('Qual a profundidade do cômodo? '))
ALTURA = 2.9
RENDIMENTO_TINTA = 10.0

calc.calcular_area_paredes(largura, profundidade)
calc.calcular_area_teto(largura, profundidade)

print(f'A área das paredes é: {calc.area_paredes}')
print(f'A litragem de tinta necessária é: {calc.area_teto / RENDIMENTO_TINTA}')
