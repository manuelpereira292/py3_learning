n = str(input('Digite o seu nome completo -> ')).strip()
print('Nome em maiúsculas: {}'.format(n.upper()))
print('Nome em minúsculas: {}'.format(n.lower()))
print('seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
separa = n.split()
print('O seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))