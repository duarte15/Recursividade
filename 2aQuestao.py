2� Quest�o
''' Escreva uma fun��o recursiva que retorna a soma de n at� zero.'''

soma = 0

def recur(n):

  global soma

  soma+= n

  if (n == 0):

    return soma

  return recur(n-1)



n=int(input("Informe o valor de n: "))

print(recur(n))