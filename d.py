#registro de nomes, notas e medias

aluno = {

    }

for i in range(3):
    nome = input('digite o nome do aluno\n>> ')
    nota1 = int(input('digite a primeira nota do aluno\n>> '))
    nota2 = int(input('digite a segunda nota do aluno\n>> '))

    nota = [nota1, nota2]

    aluno[nome] = nota
    media = (nota1 + nota2)/2

    print(f'nome: {nome}\n notas: {nota1}, {nota2}\n media final: {media}')
   
 