from primos import Primos

num = None
opcoes = None

class Main(object):
  
  num = int(input("Insira o número máximo do crivo: ")) 

  primos = Primos(num)

  def escolha():
    global num
    global opcoes
    primos = Primos(num)
    
    opcoes = int(input('Selecione uma opção: \n 1.Primos gêmeos \n 2.Pares que são a soma de primos\n 3.Primos palíndromos até os 10000 primeiros primos\n 4.Primos entre pares quadráticos\n 5.Sair\n'))
    if opcoes == 1:
      primos.gemeos()
    elif opcoes == 2:
      primos.par()
    elif opcoes == 3:
      primos.palindromo()
    elif opcoes == 4:
      primos.quadratico()
    elif opcoes == 5:
      exit()    
    else:
      print('Opção inválida')


  primos.crivo()

  escolha()
                 
                 

                 


