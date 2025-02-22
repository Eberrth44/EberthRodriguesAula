#esse codigo vai ajudar na criação da calculadora!
def get_nome ():
    nome_usuario = input ("Entre com o seu nome: ")
    return nome_usuario
def print_mensagem(nome_usario):
    print ("Ola jovem", nome_usario)
def main():
    nome_usuario = get_nome()
    print_mensagem (nome_usuario)

main(get_nome)