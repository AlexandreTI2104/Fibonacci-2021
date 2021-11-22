#Copyright by Alexandre Victor in 20/11/2021

# Fiz uma função Fibonacci envolvendo dois números com valores n1=0, n2=1 e numnovo=0 respectivamente, para descobrir a sequência de fibonacci. 
def Fibonacci(n1, n2):
  n1 = 0
  n2 = 1
  numnovo = 0

# Coloquei uma variável n para que o usuário possa digitar um número inteiro para gerar a sequência fibonacci.
  n = int(input('Inserir um numero para gerar a sequencia de Fibonacci: '))

# Em seguida usei o for para descobrir a sequência do fibonacci indo de 0 até n.
  for i in range(0, n):
    numnovo = n1 + n2
    n1 = n2
    n2 = numnovo
    print(numnovo)


Fibonacci(0, 1)