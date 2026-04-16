#detector de palíndromos

palavra = input('digite uma palavra qualquer\n>> ')

palavra = palavra.lower()

if palavra == palavra[::-1]:
    print('Esta palavra é um palíndromo')
else:
    print('Esta palavra não é um palíndromo')