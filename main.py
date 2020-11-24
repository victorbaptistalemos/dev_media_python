largura: float = float(input('Qual a largura do cômodo? '))  # Não fixa o tipo da váriável
profundidade = float(input('Qual a profundidade do cômodo? '))
ALTURA = 2.9

print(f'A área das paredes é: {2 * (largura + profundidade) * ALTURA}')
