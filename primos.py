
numeros = [True]

class Primos(object):

  def __init__(self, num):
    self.num = num

  def getNum(self):
    return self.__num

  def setNum(self, num):
    self.__num = num
 
  def crivo(self):
    global num
    global numeros
    numeros = [True]*(self.num)
    numeros[0] = False
    numeros[1] = False
    for i in range(2,self.num):
      if numeros[i]:
        for j in range(i*i,self.num,i):
           numeros[j]=False
 
    for i in range(2,self.num):
      if numeros[i]: 
        print (i)
    

  def gemeos(self):
    global numeros
    for i in range(2, len(numeros)):
      if i/2 != 0 and i > 2:
        if numeros[i-2] and numeros[i]:
          print(i-2, '  ', i)

  def par(self):
    global numeros
    for k in range(2, len(numeros)):
      if k%2 == 0:
        for i in range(2, k):
          if numeros[i]:
            j = k - i
          if numeros[j]:
              if i <= j:
                print (k, ' = ', i , ' + ', j)

  def palindromo(self):
    primos = 0
    base = [True]*4
    base[0] = False
    base[1] = False
    while primos <= 10000:
      for i in range(2, len(base)):
        if base[i]:
          base.append(True)
          for j in range(i*i, len(base), i):
            base[j] = False
            base.append(True)
      for i in range(0, len(base)):
        if base[i]:
          primos += 1
    for i in range(0, len(base)):
      if base[i]:
        if str(i) == str(i)[::-1]:
          print(i)

  def quadratico(self):
    base = [True]*400
    base[0] = False
    base[1] = False
    for i in range(2, len(base)):
      if base[i]:
        for j in range(i*i, len(base), i):
          base[j] = False

    for i in range(0, 20):
      for j in range(0, len(base)):
        if base[j] and j > i*i and j < (i+1)*(i+1):
          print(i*i, '<', j, '<', (i+1)*(i+1))
