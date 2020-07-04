from alberti import Alberti
alb = Alberti()
 
## PRIMEIRO METODO
##alfabeto do disco fixo
alb.set_fixed_disk('ABCDEFGILMNOPQRSTVXZ1234')
##alfabeto do disco movel
#alb.set_movable_disk('gklnprtvz&xysomqihfdbace')
alb.set_movable_disk('abcdefgilmnopqrstvxzhky&')

##chave do disco movel
alb.set_movable_key('e')
cifrado = alb.encrypt('EelcoroDnavirusnSomevaOaderrNotar')
print('Cifrando/Decifrando con el primer metodo Alberti')
print('Texto cifrado - ' + cifrado)
print('Texto decifrado - ' + alb.decrypt(cifrado))
print('')
 
"""
## SEGUNDO METODO
##chave inicial do disco movel
alb.set_movable_key('p')
print('Cifrando/Decifrando com o segundo metodo da cifra de Alberti')
cifrado = alb.encrypt('Dosar1gento4eotra2idor')
print('Texto cifrado - ' + cifrado)
##chave inicial do disco movel
alb.set_movable_key('p')
print('Texto decifrado - ' + alb.decrypt(cifrado))
print('')
 
## TERCEIRO METODO
print('Cifrando/Decifrando com o terceiro metodo')
##chaves do disco fixo e do disco movel
alb.set_keys('O', 'c')
cifrado = alb.encrypt('perigo', 2)
print('Texto cifrado - ' + cifrado)
alb.set_keys('O', 'c')
print('Texto decifrado - ' + alb.decrypt(cifrado, 2))"""