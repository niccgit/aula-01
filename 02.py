# Crie um algoritmo em Python que leia 3 valores (lados de um triângulo).
#
# Primeiro determine se esses valores são suficientes para formar um triângulo.
# Caso sejam suficientes, verifique se é um triângulo Equilátero, Isósceles ou Escaleno.


a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: ")) 
c = float(input("Digite o lado C: ")) 

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


# (a + b > c) and (a + c > b) and (b + c > a) (é a condição de existência de qualquer triângulo: cada lado precisa ser menor que a soma dos outros dois lados)
#
# a == b and a == c and b == c (é a condição de existência do triângulo equilátero: todos os lados devem ser iguais)
#
# a == b or a == c or b == c (é a condição de existência do triângulo isósceles: pelo menos dois lados devem ser iguais)
#
# a != b and a != c and b != c (é a condição de existência do triângulo escaleno: todos os lados devem ser diferentes)
