produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'forno']
print(produtos[1])
print (produtos[2])

vendas = [1000,1500,350,270,900]
print ("As vendas de {} foram de {}".format(produtos[1], vendas[1]))

i = produtos.index ('mouse')
print ('o valor de i é '+str (i))
print ('o produto da posiçao i é '+ str (produtos[i]))
print("-----------------------")

#Pesquisa de produto não cadastrado
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'forno', 'nada']
estoque = [1000,1500,350,270,900,2200,777]
produto = input ('insira o nome do produto em letra minuscula:')
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print ('temos {} unidades de {} no estoque'.format(qtde_estoque, produto))
else:
    print ("{} não existe no estoque".format(produto))