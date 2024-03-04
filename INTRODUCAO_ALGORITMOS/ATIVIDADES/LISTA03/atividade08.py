# Elabore um algoritmo que solicita duas informações do usuário. A primeira, pergunta se possui bolsa família (S ou N), e a segunda, se possui mais de três filhos (S ou N). Se for contemplado pelo bolsa família e possuir mais de três filhos, deverá retornar Verdadeiro, significando que pode acessar à vaga de cotista.

bolsaFamília = input("Você recebe o bolsa família? Responde com (S) ou (N)")
filhos = input("Você tem mais de três filhos? (S) |  (N)")
if(bolsaFamília == "S" or filhos == "S"):
    True
