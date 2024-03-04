# Criação de identificadores tem alguns parâmetros:
# • As letras de A a Z (maiúsculas e minúsculas)

# • Os dígitos de 0 a 9 •

# O símbolo underscore _

# • Deve começar obrigatoriamente com uma letra ou underscore 

# •Não deve conter espaços, caracteres especiais ou letras acentuadas

# • Python faz diferenciação entre maiúsculas e minúsculas. Portanto nota é diferente de NOTA.

# Q1. Escreva 5 exemplos de identificadores válidos e 5 exemplos de identificadores inválidos.
    
#Formas válidas

# nome_aluno = "Jeremias Verissimo"
# idade_aluno = 19
# altura_aluno = 1.70
# inteligencia = 100
# velocidade = 1.80

# #Formas inválidas

# 12nome = jere
# -idade = 19
# @altura = 1.90
# velocidade do aluno = 10.90
# ''inteligencia = 100
#===================================//==============================


# Q2. Supondo que as variáveis nome_aluno, nota_aluno, matricula_aluno, genero_aluno, idade_aluno sejam utilizadas para armazenar o nome do aluno, a nota na disciplina, 
# o número de matrícula, o gênero, e a idade. Qual o tipo que cada variável deve possuir para armazenar o valor adequado?

# nome_aluno será string
# nota_aluno será float ou int
# matricula_aluno será int
# genero_aluno será string
# idade_aluno será int


# Q3.  Faça um programa que leia o nome de uma pessoa e a sua idade. 
# Imprima uma mensagem que diga "Olá, [nome]. Você terá  [idade] anos daqui a 10 anos". 
# Os dados de entrada devem ser armazenados em variáveis distintas. 
# Para o processamento, considere o ano atual.

nome_aluno = input("Digite seu nome: ")
idade_aluno = int(input("Digite sua idade: "))
idade_futura = idade_aluno + 10
print(f'Bem-vindo {nome_aluno} você terá {idade_futura} daqui a dez anos')

# Q4. Escreva um algoritmo que leia a nota de 3 estudantes e retorne a média das notas.
idade_aluno1 = float(input("Digite nota do primeiro aluno: "))
idade_aluno2 = float(input("Digite nota do segundo aluno: "))
idade_aluno3 = float(input("Digite nota do terceiro aluno: "))
media_alunos = (idade_aluno1 + idade_aluno2 + idade_aluno3) / 3
print(f'A media entre as notas é de {media_alunos}')

# Q5. Escreva um algoritmo que solicita ao usuário uma quantidade de tempo em metros e então a converte para centimetros.
# Por exemplo, se o usuário inserir 2 metros, o programa deve imprimir "200 centímetros".
distancia = int(input("Digite uma distância em metros: "))
converte = distancia * 100
print(f'{converte} centímetros')

# Q6. Escreva um algoritmo que solicita ao usuário uma temperatura em graus Celsius e a
# converte para graus Fahrenheit e Kelvin. Use as fórmulas Fahrenheit = Celsius * 1.8 + 32 e Kelvin = Celsius + 273.15 para realizar as conversões.

temperatura_celsius = float(input("Insira a temperatura em graus celsius: "))
temperatura_em_fahrenheit = (temperatura_celsius * 1.8) + 32
temperatura_em_kelvin = (temperatura_celsius + 273.15)
print(f'Temperatua em Fahrenheit: {temperatura_em_fahrenheit} Temperatura em Kelvin: {temperatura_em_kelvin}')

# Q7. Área de um Retângulo: Escreva um algoritmo que solicita ao usuário a largura e o comprimento de um retângulo, depois calcula e exibe a área do retângulo.
# A fórmula para calcular a área de um retângulo é área = largura x comprimento.

largura_triangulo = float(input("Digite a largura do triângulo: "))
comprimento_triangulo = float(input("Digite o comprimento do triângulo: "))
area_triangulo = (largura_triangulo * comprimento_triangulo)
print(f'A área do triângulo é: {area_triangulo}')

# Q8. Área de um Círculo: Escreva um algoritmo que solicita ao usuário o raio de um círculo, depois calcula e exibe a área do círculo.
# A fórmula para calcular a área de um círculo é área = π x raio^2.
# Você pode usar a aproximação de 3.1416 para π.

raio_circulo = float(input("Digite o ráio do círculo: "))
area_circulo = 3.1416 * (raio_circulo ** 2) 
print(f'A área do círculo é de: {area_circulo}')

# Q9. Área de um Triângulo: Escreva um algoritmo que solicita ao usuário a base e a altura de um triângulo, depois calcula e exibe a área do triângulo.
# A fórmula para calcular a área de um triângulo é área = (base x altura) / 2.

base_triangulo = float(input("Insira a base do triângulo: "))
altura_triangulo = float(input("Insira a altura do triângulo: "))
area_triangulo = (base_triangulo * altura_triangulo) / 2
print(f'Área do triângulo é de: {area_triangulo}')