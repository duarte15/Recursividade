2ª Questão
''' Escreva uma função recursiva que retorna a soma de n até zero.'''

soma = 0

def recur(n):

  global soma

  soma+= n

  if (n == 0):

    return soma

  return recur(n-1)



n=int(input("Informe o valor de n: "))

print(recur(n))