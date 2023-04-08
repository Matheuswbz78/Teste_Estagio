# a) 1, 3, 5, 7, ___
print("a) Lógica: adicionar 2 ao número anterior")
ultimo_numero = 7
proximo_numero = ultimo_numero + 2
print("   Próximo número:", proximo_numero)

# b) 2, 4, 8, 16, 32, 64, ____
print("b) Lógica: multiplicar por 2 o número anterior")
ultimo_numero = 64
proximo_numero = ultimo_numero * 2
print("   Próximo número:", proximo_numero)

# c) 0, 1, 4, 9, 16, 25, 36, ____
print("c) Cada número é igual ao anterior acrescido de um número ímpar")
seq = [0, 1, 4, 9, 16, 25, 36]
ultimo_num = seq[-1]
penultimo_num = seq[-2]
diferenca = ultimo_num - penultimo_num
proximo_num = ultimo_num + (diferenca + 2)
print('Resultado será:',proximo_num)

# d) 4, 16, 36, 64, ____
print('D) Cada número é igual ao quadrado dos números pares. ')
seq = [4, 16, 36, 64]
ultimo_num = seq[-1]
proximo_num = (ultimo_num // 2 + 1) ** 2
print('Resultado será:',proximo_num)

# e) 1, 1, 2, 3, 5, 8, ____
print("e) Lógica: somar os dois números anteriores para obter o próximo número")
ultimo_numero = 8
penultimo_numero = 5
proximo_numero = ultimo_numero + penultimo_numero
print("   Próximo número:", proximo_numero)

#f) 2,10, 12, 16, 17, 18, 19, ____
print('f) Todos esse números começam com a letra D, logo o proximo será o numero 200.')