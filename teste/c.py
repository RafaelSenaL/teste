#soma de numeros pares positivos

soma = 0
while True:

    try:

        n = int(input('digite um numero inteiro positivo par\n>> '))

        if n < 0:
            print('apenas numeros positivos')
        elif n % 2 != 0:
            print('apenas numeros pares')
        
        elif n % 2 == 0:
            soma = sum(range(0, n+1, 2))
            print(f'este é o valor da soma dos pares do seu numero: {soma}')
            break
    except ValueError:
        print('digite apenas numeros')
       
        