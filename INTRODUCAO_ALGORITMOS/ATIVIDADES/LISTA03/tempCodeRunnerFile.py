import sys

usuarioCadastro = input("Login: ")
senhaCadastro = input("Senha: ")
senhaConfirmacaoCadastro = input("Digite a senha novamente: ")

if(senhaCadastro != senhaConfirmacaoCadastro):
    print("As senhas não correspondem...")
else:
    print("Cadastro realizado")

usuarioLogin = input("Informe o usuario para logar: ")
senhaLogin = input("Informe a senha para logar: ")
if(usuarioLogin != usuarioCadastro and senhaLogin != senhaCadastro):
    print("Os campos incorretos...")
    sys.exit()
else:
    print("Usuário autenticado com sucesso!")