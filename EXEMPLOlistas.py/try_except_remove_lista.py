#remover produtos de uma lista com escolha do usuario
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'forno']
item_usuario = input ("qual item deseja remover?")
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print ("o produto {} nao exite na lista.".format(item_usuario))