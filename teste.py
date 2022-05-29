#>>>>>  CALCULANDO A MEDIA DE NOTAS  <<<<<

#n1 =int (input("nota 01:"))
#n2 =int (input("nota 02:"))
#n3 =int (input("nota 03:"))
#m = (n1+n2+n3)/3

#print(' A nota 1 é:{0}\n a nota 2 é:{1}\n a nota 3 é:{2} a media é:{3}'.format(n1,n2,n3,m))



#>>>>>  CALCULANDO O DOBRO DE UM NUMERO E SUA RAIZ QUADRADA  <<<<<<

#n1 = int(input('digite um mumero:'))
#d = n1+n1
#r = n1*n1

#print('numero: {} seu dobro: {} sua raiz quadrada : {}'.format(n1,d,r))

#>>>>>>> CONVERTER METROS E CENTIMENTROS EM MILIMETROS <<<<<<

#m = float (input('digite uma valor:'))
#cm = m*100
#mm = m*1000

#print('{} Metros\n{}cm convertido em cm\n{}mm convertido em mm'.format(m,cm,mm))
 
#>>>>>>> CONVERSOR DE REAL PARA DOLAR <<<<<

#real = int(input('quanto vc tem?'))
#dolar = 4,98
#con = (real * 4,98)

#print('Você tem: {0} R$ \n O valor do dolar atualmente esta: {1} Dolares \n Voce pode comprar: {2} de #dolares'.format(real,dolar,con))

#>>>>>>> CALCULADORA DE TINTA <<<<<<<<

#A = int(input('Quantos metros de altura tem a parede?'))
#L = int(input('Quantos metros de Largura tem a parede?'))
#M = A*L
#LT = M/2

#print(' A area total é : {} metros quadrados \n Sera necessario {} Litros de tinta'.format(M,LT))

#>>>>> CALCULANDO O VALOR DE UM PRODUTO COMM DESCONTO <<<<<

#v = int(input('O valor do produto é: '))
#vd = int(input("O valor do desconto é: "))
#vf = v - vd

#print('O valor do produto sem desconto é: {0}\n O valor dodesconto é: {1}\n O valor final do produto com desconto é: {2}'.format(v,vd,vf))

#>>>>>>>>>> DIGIANDO UM NUMERO E SUA TABUADA <<<<<<<<<<<<<<

#import math
#num1= int(input('Digite um numero:'))
#num2 = 1
#res1 = num1 * 1
#num3 = 2
#res2 = num1 * 2
#num4 = 3
#res3 = num1 * 3

#print('{} x {} = {}'.format(num1,num2,res1 ))
#print('{} x {} = {}'.format(num1,num3,res2 ))
#print('{} x {} = {}'.format(num1,num4,res3 ))

#>>>>>>> CALCULANDO A RAIZ QUADRADA DE UM NUMERO <<<<<<<<<

from math import sqrt
num = int(input("Digite um numero: "))
raiz = sqrt(num)
print('A raiz quadradada de :{} \n É: {:.0f}'.format(num,raiz))