#TRANSFORMAR APENAS A PRIMEIRA LETRA DE UMA STRING EM MAIUSCULA
nome = "eberth"
print (nome.capitalize(),"\n")
print ("--------------------------------------------")


#TRANFORMA TODAS AS LETRAS EM MINUSCULA
nome = "EBERTH"
print (nome.casefold(),"\n")
print ("--------------------------------------------")


#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING 
email = "EberthSilva@gamail.com"
print (email.count('i'), "\n")
print ("--------------------------------------------")


#RETORNA TRUE (veradeiro) OU false (falso) PARA UM TESTE se A STRING TERMINA COM UMA STRING 
nome = "EberthSilva@gmail.com"
print (nome.endswith('gamil.com'),"\n")
print ("--------------------------------------------")


#ENCONTRA A POSIÇAO DO TERMO PROCURADO. LEMBRE-SE COMEÇA DO zero
nome = "Eberthsilva@gmail.com"
print (nome.find('@'),"\n")
print ("--------------------------------------------")


#VERIFICA SE O TEXTO É (TODO) COM LETRAS
nome = "Eberth"
print (nome.isalpha(),"\n")
print ("--------------------------------------------")


#VERIFICA SE TODO O TEXTO E COM NUMEROS
nome = "123"
print (nome.isnumeric(),"\n")
print ("--------------------------------------------")


#SUBSTITUI UM CARATERE ESCOLHIDO POR OUTRO.
nome = "Eberth"
print (nome.replace('o','u'),"\n")
print ("--------------------------------------------")


#SEPARA O TEXTO string BASEADO EM ALGUM CARACTERE INDICADO
nome = "Eberth @ Silva Rodrigues"
print (nome.split('@'), "\n")
print ("--------------------------------------------")


#COLOCAR TODAS AS LETRAS INICIADAS EM MAISCULAS. 
nome = "eberth da silva rodrigues"
print (nome.title(),"\n")
print ("--------------------------------------------")


#RETIRA OS CARACTERES INDESEJADOS, COMO POR EXEMPLO espaços QUE NÃO AGREGAM VALOR   
nome = "    eberth silva rodrigues"
print (nome.strip(),"\n")
print ("--------------------------------------------")

#RETORNA true OU false PARA UM TESTE DE UMA STRING COM TEXTO ESPECIFICO
nome = "eberth 2008"
print (nome.startswith("ebe"),"\n")
print (nome.startswith("Ebe"),"\n")
print ("--------------------------------------------")


#