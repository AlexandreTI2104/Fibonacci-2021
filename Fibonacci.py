#Copyright by Alexandre Victor in 20/11/2021
 
def Fibonacci(n1, n2):
  n1 = 0
  n2 = 1
  numnovo = 0

  n = int(input('Inserir um numero para gerar a sequencia de Fibonnaci: '))

  for i in range(0, n):
    numnovo = n1 + n2
    n1 = n2
    n2 = numnovo
    print(numnovo)


Fibonacci(0, 1)