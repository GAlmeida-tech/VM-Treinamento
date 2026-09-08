print("Sistema de Login Viana e Moura")

usuario = "vianaMoura"
senha = "12345"
tentativas = 3


def entrar(login_usuario, login_senha):

    if login_usuario != usuario:
        print("Usuário incorreto!")
        return False

    if login_senha != senha:
        print("Senha incorreta!")
        return False

    print("Bem-vindo!")
    return True


while tentativas > 0:

    login_usuario = input("Digite seu usuário: ")
    login_senha = input("Digite sua senha: ")

    if entrar(login_usuario, login_senha):
        break

    tentativas -= 1
    print("Tentativas restantes:", tentativas)