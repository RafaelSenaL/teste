#criar um jogo de adivinhação de numeros de 1 a 100



import random
numero = random.randint(1, 100)
tentativas = 0
while True:
   
    x = int(input('adivinhe um numero de 1 a 100\n>> '))
    tentativas += 1

    if x == numero:
        print(f'Parabéns, você acertou em {tentativas} tentativas')
        break
    elif x < numero:
        print('muito baixo')
    else:
        print('muito alto')