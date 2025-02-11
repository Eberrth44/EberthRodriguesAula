#faca um programa que receba uma nota do aluno e se for suoerior ou igual a 7 apareca a mensagem que esta aprovado
#se for INFERIOR a 5 ele esta "nao aprovado/ reprovado direto"
#se estiver entre 5 e 7 apareca a mensagem "nao aprovado/ recuperaçao"

numero = float (input ("DIgite um numero: "))
if numero >= 7:
    print ("Aprovado")

else: 
    if numero <= 5:
     print ("nao aprovado/reprovado direto")
    else:
      print("nao aprovado/Recuperaçao")