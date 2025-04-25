""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """

""" for cont in range(0, 101):
  cont+1  
  print(cont) """
""" 
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. """
""" 
numero=int(input('ingresa un numero entero'))
nroOriginal=numero
cont=0

if numero>0:
  while numero > 0:
    cont+=1
    numero=numero//10   # con '// '  divide y se queda con el entero

  print('el numero ingresado', nroOriginal, '  tiene ', cont, ' digitos')    
else:
  print('el nro debe ser positivo') """
 
"""  3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. """

""" primerValor=int(input('Ingresa el primer nro'))
segundoValor=int(input('ingresa el segundo valor'))
acu=0

if primerValor==segundoValor:
     print('debes colocar valores distintos')
else:
    if primerValor>segundoValor:
      primerValor, segundoValor = segundoValor, primerValor #Si el primer valor es mayor que el segundo, intercambia sus valores.

    for count in range(primerValor+1, segundoValor):
      acu+=count
    print(acu) """

""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.  """
""" numero=int(input('Ingresa un numero entero'))
acu=0

while numero !=0:
    acu+=numero
    numero=int(input('Ingresa otro numero entero'))

print(f'El numero acumulado es {acu}') """

"""  5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
 programa debe mostrar cuántos intentos fueron necesarios para acertar el número.  """

""" import random
numeroRandom = random.randint(0, 9)  
acertado=False
cantidadIntentos=0
print('Adivina el numero aleatorio entre 0 y 9')

while not acertado:
    intento=int(input('Ingresa un numero: '))
    if 0<=intento<=9:
      cantidadIntentos+=1
      if intento == numeroRandom:
         acertado=True
      else:
         print('No acertaste, intenta de nuevo...')
    else:
      print('Numero fuera de rango. debe ser entre 0 y 9')

print(f'Acertaste en {cantidadIntentos} intentos! El numero aleatorio era {numeroRandom}') """

""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. """

""" for nros in range(100, -1, -2):
    print(nros) """

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario """

""" numero=int(input('Ingresa un numero entero'))
acu=0

if numero >0:
  for cont in range(0, numero+1):
    acu+=cont
  print(f'La suma de los numeros hasta {numero} es {acu}')

else:
  print('El numero debe ser mayor a 0')   """
  

"""   8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). """

""" ingresos=6
contPares=0
contImpares=0
contNeg=0
contPos=0

for cont in range(1, ingresos+1):
  numero=int(input(f'ingresa un numero'))

  if numero>0:
    contPos+=1
  elif numero<0:
    contNeg+=1
  if numero%2==0:
    contPares+=1
  else:
    contImpares+=1

print(f'La cantidad de pares es {contPares}, la cantidad de impares {contImpares}, de negativos {contNeg} y de positivos {contPos} ')     """  

""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).  """

""" ingresos=5
acu=0

for cont in range(1,ingresos+1):
  numero=int(input('Ingresa un numero'))
  acu+=numero
print(f'El promedio de los numeros ingresados es {acu/ingresos}')   """

""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """

""" numero=int(input('Ingresa un numero de mas de un digito'))
numeroOriginal=numero
numeroInvertido=0

while numero >0:
  digito=numero%10
  numeroInvertido=numeroInvertido * 10 + digito
  numero=numero // 10
print(f'El numero ingresado {numeroOriginal} quedo como {numeroInvertido}') """