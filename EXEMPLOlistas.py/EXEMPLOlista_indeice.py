produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
print(produtos[1])
print (produtos[2])

vendas = [1000,1500,350,270,900]
print ("As vendas de {} foram de {}".format(produtos[1], vendas[1]))

i = produtos.index ('mouse')
print ('o valor de i é '+str (i))
print ('o produto da posiçao i é '+ str (produtos[i]))
print("-----------------------")

#Pesquisa de produto não cadastrado
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'forno']
estoque = [1000,1500,350,270,900]
produto = input ('insira o nome do produto em letra minuscula:')
if produto == '':
    i = produtos.index(produto)
    print(i)
else:
    print("error 404")
