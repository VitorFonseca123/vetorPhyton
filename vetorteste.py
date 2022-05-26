n = int(input('Digite o tamanho do vetor: '))
vetor = [n]
value = 0
for i in range(n):
    value = input('Digite uma letra: ')
    vetor.insert(i, value)
for i in range(n):
    print(vetor[i])
