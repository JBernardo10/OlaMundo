valores = [[], []]
for c in range(0, 7):
    num = int(input(f"Digite o {c+1}° valor: "))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print('-='*20)
print('Os valores impares digitados são: {}'.format(valores[1]))
print("Os valores pares digitados são: {}".format(valores[0]))
