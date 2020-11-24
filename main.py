largura: float = float(input('Qual a largura do cômodo? '))  # Não fixa o tipo da váriável
profundidade = float(input('Qual a profundidade do cômodo? '))
ALTURA = 2.9
RENDIMENTO_TINTA = 10.0
area_paredes = 2 * (largura + profundidade) * ALTURA
area_teto = largura * profundidade

print(f'A área das paredes é: {area_paredes}')
print(f'A litragem de tinta necessária é: {(area_paredes + area_teto) / RENDIMENTO_TINTA}')
