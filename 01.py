# Crie um programa em Python que faça as seguintes perguntas para o aluno:
#
# Nome (str)
# Idade (int) - baseada no ano de nascimento
# Notas (float) 
#
# Depois, calcule a Média baseada nas notas inseridas e calcule a situação final do aluno.
# 
# Junte todas as informações e mostre em uma tabela ao final.


nome_do_aluno = input("Digite o nome do aluno: ")

ano_atual = int(input("Digite o ano atual: "))

ano_de_nascimento = int(input("Digite o ano de nascimento do aluno: "))


idade = (ano_atual) - (ano_de_nascimento)


nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))


media = (nota1 + nota2) / 2


if media >= 7:
    situacao = "Aprovado!"
elif media >= 5:
    situacao = "Recuperação..."
else:
    situacao = "Reprovado."


print(f"Aluno: {nome_do_aluno}")
print(f"Idade: {idade}")
print(f"Média do aluno: {media}")
print(f"Situação do aluno: {situacao}")
