#Juntar lista e ordenar.
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'forno']
novo_produtos = ['chromecast', 'windows phone']
produtos.extend(novo_produtos)
print (produtos)
print("-------------------------------")

#Juntar lista e ordenar usando  outro metodo.
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'forno']
novo_produtos = ['chromecast', 'windows phone']
produtos_compilados = produtos+ novo_produtos
print(produtos_compilados)

print("-------------------------------")
#adicionar produtos usando append.
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'forno']
novo_produtos = ['chromecast', 'windows phone']

print("-------------------------------")
print('usando + :')
produtos_compilados = produtos+ novo_produtos
print (produtos_compilados)

print ('usando append')
produtos.append(novo_produtos)
print(produtos)
