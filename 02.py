# Crie um algoritmo que leia 3 valores (lados de um triângulo)
# Determine se formam um triângulo, e se formar verifique
# se é um equilátero, isósceles ou escaleno.

a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: ")) 
c = int(input("Digite o lado C: ")) 

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Forma um triângulo: ")
    if a == b and a == c and b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
     print("Não forma um triângulo!")