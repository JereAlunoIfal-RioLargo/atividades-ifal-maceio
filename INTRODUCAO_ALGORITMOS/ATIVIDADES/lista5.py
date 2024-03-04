# i = 0
# contador = 0
# contadorMultiplos = 0
# while i < 500:
#     i = i + 1
#     if(i % 2 != 0):
#         if(i%3 == 0 ):
#             contador = contador + i
#             # print(i)
#             quantidadeImpares = i
#     if(i % 3 == 0):
#         contadorMultiplos = contadorMultiplos + 1
#         # print(i)

        
# print(f'A soma dos números ímpares múltiplos de 3 é: {contador}')
# print(f'Quantidade de números multiplos de 3 de 0 a 500: {contadorMultiplos}')


# for altura in range(pessoas):
#     print(altura)

# Q2

# maior_nome = ''
# maior_altura = float('-inf')
# menor_nome = ''
# menor_altura = float('inf')

# for i in range(1,3):
#     nome = input(f'Informe o nome da pessoa {i}: ')
#     altura = float(input(f'Informe o nome de {nome}: '))
    
#     if(altura > maior_altura):
#         maior_nome = nome
#         maior_altura = altura
    
#     if(altura < menor_altura):
#         menor_nome = nome
#         menor_altura = altura

# print(f'A pessoa mais alta é: `{maior_nome} com {maior_altura} metros por altura')
# print(f'A pessoa mais baixa é: `{menor_nome} com {menor_altura} metros por altura')


# Q3

# import random

# numeroAleatorio = random.randint(1,100)


# while True:
#     chute = int(input('Digite um número: '))
#     if(chute > numeroAleatorio):
#         print("O número escolhido é maior que o sorteado\n =======================")
#     elif(chute == numeroAleatorio):
#         print(f"Parabéns! Você acertou. O numero sorteado foi: {numeroAleatorio}")
#     else:
#         print("O número escolhido é menor que o sorteado\n ========================")

        
# Q4

# quantidadeAlunos = int(input('Quantidade de alunos: '))
# quantidadeAprovados = 0
# quantidadeReprovados = 0

# for aluno in range(quantidadeAlunos):
#     nome = input('Nome: ')
#     situacao = input('Status: ')
#     if(situacao.lower() == 'aprovado'):
#         quantidadeAprovados = quantidadeAprovados + 1
#     else:
#         quantidadeReprovados = quantidadeReprovados + 1

# print(f'Alunos aprovados: {quantidadeAprovados}')
# print(f'Alunos reprovados: {quantidadeReprovados}')

# Q5

valor = int(input('Número: '))
variador = 0
acumulador = 0

for x in range(1, valor):
    variador = valor - x
    print(f'Variador: {variador}')
    # print(f'{valor} x {variador}')
    # print(variador)
    operacao = valor * variador
    acumulador = operacao * variador
    resultado = acumulador
print(resultado)


    