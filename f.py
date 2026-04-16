#contador de vogais

frase = input('digite uma frase qualquer\n>> ')

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

contador = 0

for letra in frase: 

    if letra.isalpha():
        if letra in vogais:
            contador += 1
            
print(contador)