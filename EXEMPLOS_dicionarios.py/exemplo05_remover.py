#REMOVER uma chave!
lucro_2Tri = {"janeiro": 10, "fevereiro": 20, "agosto": 30}
lucro_2Tri = {"abril": 8, "maio": 1, "junho": 2}
del lucro_2Tri["junho"]#seleciona para remover
print (lucro_2Tri) #removido
print ("______________________________________")
#usando o metodo POP

lucroMes = lucro_2Tri.pop("maio")
print ("______________________________________")
print (lucro_2Tri)

#remover todos os dados de um dicionario!
print ("______________________________________")
lucro_2Tri.clear()
print (lucro_2Tri)