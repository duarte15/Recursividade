1� Quest�o
''' Escreva uma fun��o recursiva que  imprima de um n�mero x at� um y.'''

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