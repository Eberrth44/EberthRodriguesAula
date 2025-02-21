pessoas_presentes = ["jonh", "jesse", "aria", "tyrion"]
#quero sber se uma pessoa especifica esta presente
chamada = "aria"
for pessoa in pessoas_presentes:
     if pessoa == chamada:
          print ("{}esta presente.".format(chamada))
          break
else:
    print ("{} não esta presente na sala!")    