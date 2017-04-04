1ª Questão
''' Escreva uma função recursiva que  imprima de um número x até um y.'''

def recur(x,y):

  print(x)

  if (x == y):

    return("")

  return recur(x+1,y)

x=int(input("Informe o valor de x: "))

y=int(input("Informe o valor de y(maior que x): "))

if (x<y):

  recur(x,y)

else:

  print("O valor de x deve ser menor que o valor de y!")