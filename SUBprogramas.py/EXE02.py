def get_data ():
    nome=input ("Escreva seu nome: ")
    idade = int (input ("Digite sua idade: "))
    tupla_data = (nome, idade)
    return tupla_data

def mensagem (nome, idade):
    if idade <= 10:
        print ("oi", nome)
        print ("Idade:",idade)
    else:
        print ("Ola",nome)
        print ("Idade:",idade)

def main():
    nome, idade = get_data()
    mensagem(nome, idade)
main()