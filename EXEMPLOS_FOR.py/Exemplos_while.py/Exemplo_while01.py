venda = input ('Registre um produto. Para cancelar o registro de um novo produto, baasta apertar enter sem digitar nada:')
vendas = [];
#crie aqui o programa 
while vendas != '':
    vendas.append(venda)
    venda = input ("registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada:")
print ("registros Finalizados. As vendas cadastradas foram: {}".format(vendas))

