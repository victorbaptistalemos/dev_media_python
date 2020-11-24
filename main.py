from calculadora import Calculadora
from comodo import Comodo

comodo = Comodo(
    input('Qual a largura do cômodo? '),
    input('Qual a profundidade do cômodo? ')
)

calculadora = Calculadora(comodo)


print(f'A área das paredes é: {calculadora.get_area_parede()}')
print(f'A área do teto é: {calculadora.get_area_teto()}')
print(f'A litragem de tinta necessária é: {calculadora.get_litro_rendimento()}')
