''' 
Loop que percorre sequências, repetindo açôes para cada elemento.

MINHA LÓGICA
1 vou criar 1 lista NOTAS
2 vou fazer um for para 3 alunos onde colocarei Nome e 4 notas assim fazendo a média
3 fiz um len(notas) para saber quantos alunos foram lançados mas antes
    eu tinha feito um contnome = 0 e cada fim de for eu colocava +1 no contnome
4 vou fazer um novo for 

'''

notas = []

cont = 1
#contnome = 0
for x in range(3):
    nome = input(f'Nome {cont}° anolo/a: ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    nota3 = float(input('3ª nota: '))
    nota4 = float(input('4ª nota: '))
    media = ((nota1+nota2+nota3+nota4)/4)
    cont += 1
    #contnome += 1
    resultado = [nome, media]
    notas.append(resultado)
    
for n in notas:
    nome = n[0]
    mediaaluno = n[1]
    if n[1] >= 5:
        print(f'O aluno {nome} teve a média {mediaaluno} e ele está aprovado.')
    else:
        print(f'O aluno {nome} teve a média {mediaaluno} e ele está reprovado.')
print(f'Temos {len(notas)} alunos lançados.')