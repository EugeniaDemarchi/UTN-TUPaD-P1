""" 1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

""" mayoriaDeEdad=18

edad= int(input(f'Ingresa tu edad'))

if edad> mayoriaDeEdad:
    print('Eres mayor de edad')
else:
     print('Todavia no tenes la mayoria de edad') """

""" 
     2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”. """

""" nota=int(input('Ingresa tu nota: '))

if nota >= 6:
     print('Aprobado!')
else:
     print('Desaprobado') """

""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. """

""" numeroIngresado=int(input('Ingresa un numero: '))

if numeroIngresado%2 == 0:
    print('Has ingresado un numero par')
else:
    print('por favor ingresa un nro par') """

""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años. """

""" edad=int(input('Ingresa tu edad: '))
if edad < 12:
  print('Niño')
elif edad>=12 and edad <18:
    print('Adolescente')
elif edad>=18 and edad < 30:
    print('Adulto joven')
else:
   print('Adulto')  """


""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string """

""" contraseña=input('Ingresa tu contraseña: ')
longitud=len(contraseña)

if longitud < 8 or longitud>14:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')
else:
      print('Ha ingresado una contraseña correcta') """

""" 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
siguiente: 

from statistics import mode, median, mean 
mi_lista = [1,2,5,5,3] 
mean(mi_lista) 

En la documentación oficial se puede encontrar más información sobre este paquete: 
https://docs.python.org/es/3.8/library/statistics.html.  
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
Definir la lista numeros_aleatorios de la siguiente forma:  """
""" from statistics import mode, median, mean 

import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]  """

""" Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
forma aleatoria.  """

""" moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
print(moda, mediana, media)

if media>mediana and mediana>moda:
    print('sesgo positivo')
elif media<mediana and mediana<moda:
    print('sesgo negativo')
elif media == mediana == moda:
    print('sin sesgo') """

""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. """

""" palabra=input('Ingresa una frase o palabra: ')
ultimoCaracter=palabra[-1]

if ultimoCaracter == 'a' or ultimoCaracter == 'e' or ultimoCaracter == 'i' or ultimoCaracter == 'o' or ultimoCaracter =='u':
  print(f'{palabra}!')
else:
    print(palabra) """

""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

""" nombre=input('Ingrese su nombre: ')

eleccionLetras=int(input('Si desea que su nombre este en mayusculas ingrese 1, en minuscula: 2 y con la primer letra en mayuscula: 3: '))

mayuscula=nombre.upper()
minuscula=nombre.lower()
inicialMayuscula=nombre.title()

if eleccionLetras == 1:
    print(mayuscula)
elif eleccionLetras == 2:
    print(minuscula)
elif eleccionLetras == 3:
    print(inicialMayuscula)
else:
    print('ha ingresado un nro incorrecto, debe ser 1, 2 o 3') """

""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """
""" 
magnitudTerremoto=float(input('Ingresa la magnitud del terremoto'))

if magnitudTerremoto<3:
  print('Muy leve (imperceptible)')
elif  magnitudTerremoto < 4:
  print('Leve, ligeramente perceptible')
elif magnitudTerremoto < 5:
  print('Moderado (sentido por personas, pero generalmente no causa daños)')
elif  magnitudTerremoto <6:
  print('Fuerte (puede causar daños en estructuras débiles')
elif magnitudTerremoto<7:
  print('Muy Fuerte (puede causar daños significativos)')
else:
  print('Extremo (puede causar graves daños a gran escala).')  """

""" 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano. """

hemisferio=input('Ingrese en cual hemisferio se encuentra: Ingrese N para Norte y S para sur: ')
hemisferio=hemisferio.upper()
if hemisferio != 'N' and hemisferio != 'S':
    print('Debe ingresar N o S')
    exit()

mes=int(input('Ingrese el mes del año en numero'))
if mes<1 or mes >12:
    print('Debe ingresar un numero entre 1 y 12')
    exit()


if mes == 1 or mes == 3 or mes == 5 or mes== 7 or mes ==8 or mes == 10 or mes == 12:
  dias_maximos=31
elif mes==4 or mes ==6 or mes == 9 or mes == 11:
   dias_maximos=30
else:
    dias_maximos=28

dia= int(input('Ingrese la fecha correspondiente: '))
if dia <1 or dia>dias_maximos:
   print(f'debe ingresar una fecha valida para el mes: {mes}')
   exit()

if hemisferio == 'N': 
         
    if (dia>=21 and mes ==12)  or (mes==1) or (mes==2) or (dia<=20 and mes ==3):
        print('estas en invierno')
    elif (dia>=21 and mes == 3) or (mes==4)or (mes==5) or (dia <=20 and mes ==6):
          print('estas en primavera')
    elif (dia>=21 and mes ==6) or (mes==7) or (mes==8) or (dia <=20 and mes==9):
        print('estas en verano')
    else:
        print('Otoño')


else :
    if (dia>=21 and mes ==12)  or (mes==1) or (mes==2) or (dia<=20 and mes ==3):
        print('estas en verano')
    elif (dia>=21 and mes == 3) or (mes==4)or (mes==5) or (dia <=20 and mes ==6):
          print('estas en otoño')
    elif (dia>=21 and mes ==6) or (mes==7) or (mes==8) or (dia <=20 and mes==9):
        print('estas en invierno')
    else:
        print('primavera')
