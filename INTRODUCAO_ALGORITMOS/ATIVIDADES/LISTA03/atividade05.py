import sys

usuarioCadastro = input("Digite o usuário: ")
senhaCadastro = input("Digite sua senha: ")
senhaConfirmacao = input("Confirme sua senha: ")

if(senhaCadastro != senhaConfirmacao):
    print("A senha não coincidem")
    sys.exit()
else:
    print("Usuário cadastrado...")

usuarioLogin = input("Informe seu login: ")
senhaLogin = input("Informe sua senha: ")
if(senhaLogin != senhaCadastro and usuarioLogin != usuarioCadastro):
    print("Campos incorretos!")
    sys.exit()
else:
    print("Usuário logado!")