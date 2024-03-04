#  Elabore um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500. No final, exiba a quantidade de números ímpares múltiplos de 3, e o resultado da soma.
# i = 0
# contador = 0
# quantidadeImpar = 0
# while i < 500:
#     if(i % 2 != 0):
#         if(i%3==0):
#             contador+=i
#             quantidadeImpar+=1
#     i+=1
# print(contador)
# print(f'Quantidade ímpares: {quantidadeImpar}')


# Q2. Escreva um algoritmo que leia o nome e a altura de 10 pessoas, e imprima o nome da maior e da menor pessoa.

# nome_pessoa_maior = ''
# nome_pessoa_menor = ''

# altura_pessoa_maior = float('-inf')
# altura_pessoa_menor = float('inf')

# i = 0 
# while i < 3:
#     nome = input('Nome: ')
#     altura = float(input(f'Insira a altura de {nome}: '))

#     if(altura > altura_pessoa_maior):
#         altura_pessoa_maior = altura
#         nome_pessoa_maior = nome
#     if(altura < altura_pessoa_menor):
#         altura_pessoa_menor = altura
#         nome_pessoa_menor = nome
#     i+=1
    
# print(f'Pessoa mais alta: {nome_pessoa_maior} | Altura: {altura_pessoa_maior}')
# print(f'Pessoa menor: {nome_pessoa_menor} | Altura: {altura_pessoa_menor}')

# Q3. Escreva um algoritmo que possui um número secreto de 1 a 100, e fica pedindo que o usuário digite um número inteiro de 1 a 100 até acertar o número secreto. Quando acertar, informar com quantos chutes ele conseguiu acertar o número.

# import random

# numeroAleatorio = random.randint(0,100)
# print(f'Número aleaório: {numeroAleatorio}')

# chute = int(input('Chute: '))

# while chute != numeroAleatorio:
#     print('Número errado!')
#     chute = int(input('Chute: '))

# if(chute == numeroAleatorio):
#     print(f'Você acertou! O número sorteado foi: {numeroAleatorio}')


# =========================================================
# Q4. Escreva um algoritmo que:
# Solicita a área em que um estudante prestou o vestibular (humanas, saúde, exatas).
# Define a pontuação de corte de cada área.
# Solicita a quantidade de estudantes que a turma de um cursinho  pré-vestibular possui.
# Para cada estudante:
# Solicita a área que prestou o vestibular.
# Solicita a nota do ENEM.
# Informe se o estudante foi classificado ou não. 
# No final, o sistema deverá informar:
# Quantos alunos foram classificados e quantos foram desclassificados para cada área. 
# A porcentagem de alunos classificados e desclassificados por área.
# A porcentagem de alunos classificados e desclassificados no total.

# humanas = 600
# exatas = 700
# saude = 780

# aprovadosEmHumanas = 0
# aprovadosEmSaude = 0
# aprovadosEmExatas =0

# reprovadosEmHumanas = 0
# reprovadoEmExatas = 0
# reprovadoEmSaude = 0

# quantidadesDeAlunos = int(input('Quantidade de alunos: '))

# for i in range(quantidadesDeAlunos):
#     areaEscolhida = input('Área esolhida: ')
#     nota = int(input('Informe a nota: '))

#     if(areaEscolhida == 'humanas'):
#         if(nota >= 700):
#             print('Parabéns! Você foi aprovado!')
#             print('=======')
#             aprovadosEmHumanas+=1
#         else:
#             print('Infelizmente você não foi aprovado')
#             reprovadosEmHumanas +=0
#     if(areaEscolhida == 'exatas'):
#         if(nota >= 700):
#             print('Parabéns! Você foi aprovado!')
#             print('=======')

#             aprovadosEmExatas+=1
#         else:
#             print('Infelizmente você não foi aprovado')
#             reprovadoEmExatas+=1
#     if(areaEscolhida == 'saude'):
#         if(nota >= 780):
#             print('Parabéns! Você foi aprovado!')
#             print('=======')
#             aprovadosEmSaude+=1
#         else:
#             print('Infelizmente você não foi aprovado')
#             reprovadoEmSaude+=1
# print('===================')
    
# print(f'Alunos aprovados em Exatas: {aprovadosEmExatas}')
# print(f'Alunos reprovados em Exatas: {reprovadoEmExatas}')
# print('===================')
# print(f'Aprovados em Humanas: {aprovadosEmHumanas}')
# print(f'Reprovados em Humanas: {reprovadosEmHumanas}')
# print('===================')
# print(f'Aprovados em Saúde: {aprovadosEmSaude}')
# print(f'Reprovados em Saude: {reprovadoEmSaude}')
# ==================================================




# Q5. Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o seu resultado. Este algoritmo representa o cálculo fatorial de um número.
# Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
# Utilize o loop while para resolver esta questão.

numero = int(input('Número: '))

i = 1
acumulador = 1

while i <= numero:
    acumulador = acumulador * i
    i+=1
    
print(acumulador)