nome = ['eberth', 'kaio','caio', 'daniel']
telefone = [47, 51, 91, 44, 55]
endereco = ['jarivatuba', 'monsenhor gercino', 'ademar garcia,'' iting', 'comasa']


nome = input ("digite nome:")
telefone = int(input ("digite seu telefone:"))
endereco= input ("Digite seu bairro: ")
if nome and telefone and endereco == nome and telefone and endereco:
    print (nome)
    print (telefone)
    print (endereco)
else:
    print ("invalido")