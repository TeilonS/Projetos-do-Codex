print('BANK OF CODÉDEX')

pin = int(input('Digite seu PIN: '))

while pin != 1234:
  pin = int(input('PIN incorreto. Digite seu PIN novamente: '))

if pin == 1234:
  print('PIN aceito!')
