aluno = input("Digite o nome do aluno: ")
ano_de_nascimento = int(input("Digite o ano de nascimento do aluno: "))
nota1 = float(input("Digite a nota 1 do aluno: "))
nota2= float(input("Digite a nota 2 do aluno: "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao =  "Aprovado!"
elif media >= 5:
    situacao = "Recuperacao"
else:
    situacao = "Reprovado."

ano_atual = 2026
idade = (ano_atual) - (ano_de_nascimento)

print (f"Aluno: {aluno}")
print (f"Idade: {idade}")
print (f"Média: {media}")
print (f"Situaçao do aluno: {situacao}")