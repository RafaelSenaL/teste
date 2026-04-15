lista = []
frase = input('digite uma frase\n>> ')

lista = frase.split()
print(frase.upper()) #.upper() deixa os caracteres maiusculos e .lower para minusculos
print(len(frase)) #len() conta itens especificos
print(len(lista))
print(lista[0], lista[-1]) #[0] primeiro item de uma lista [-1] ultimo item de uma lista