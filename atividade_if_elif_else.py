meta = 20000
vendas = 40000
if vendas < meta:
    print ("Não ganhou bonus")
elif vendas >  (meta*2):
    bonus = 0.007 *vendas
    print ("ganhou {} de bonus".format(bonus))
else:
    bonus = 0.03 * vendas
    print ("ganhou {} de bonus ".format(bonus))