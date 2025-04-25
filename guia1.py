
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print('Hola mundo')
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 
name=input('ingresa tu nombre')
print(f'Hola', {name})
"""  """
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla."
""" name=(input('Ingresa tur nombre'))
apellido=(input('Ingresa tu apellido'))
edad=input('ingresa tu edad')
residencia=input('ingresa tu lugar de residencia')
print(f'Soy {name} {apellido}, tengo {edad} años y vivo en {residencia}') """
#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
""" import math
radio=float(input('ingresa el radio del circulo'))
pi=math.pi
area= round(pi * radio * radio, 2)
perimetro=round(2*pi*radio,2)
print(f'El area del circulo es {area} y el perimetro, {perimetro}') """
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 
""" segundos=int(input('ingresa los segundos'))
horas=round(segundos/3600,2)
print(f'{segundos} segundos en horas es {horas}') """
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.  
""" numero=int(input('ingresa un numero'))
print(f'{numero} * 1 = {numero  * 1}')
print(f'{numero} * 2 = {numero  * 2}')
print(f'{numero} * 3 = {numero  * 3}')
print(f'{numero} * 4 = {numero  * 4}')
print(f'{numero} * 5 = {numero  * 5}')
print(f'{numero} * 6 = {numero  * 6}')
print(f'{numero} * 7 = {numero  * 7}')
print(f'{numero} * 8 = {numero  * 8}')
print(f'{numero} * 9 = {numero  * 9}')
print(f'{numero} * 10 = {numero  * 10}') """
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
""" primerNro=int(input('ingresa un nro entero distino de 0'))
segundoNro=int(input ('ingresa otro nro entero distino de 0'))
suma=primerNro+segundoNro
resta=primerNro - segundoNro
division=float(primerNro/segundoNro)
mutiplicacion= primerNro *  segundoNro
print(f'El resultado de sumar {primerNro} y {segundoNro} es {suma}, de restarlos: {resta}, multiplicarlos. {mutiplicacion} y dividirlos, {division}') """
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:  𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 /(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
""" peso=float(input('ingresa tu peso en kg'))
altura=float(input('ingresa tu altura en mts'))
masaCorporal=print(f'el indice de tu masa corporal es {peso/(altura*altura)}') """
# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
#t𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32
""" temperaturaCelcius=float(input('Ingresa la temperatura en C°'))
temperaturaFarenheit=print(f'{temperaturaCelcius} C° a Farenheit es {(temperaturaCelcius * 1.8)+32}') """
#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.  
nro1=int(input('ingresa el 1er nro entero'))
nro2= int(input('ingresa el segundo nro'))
nro3=int(input('ingresa el 3er nro'))
sumaNros=nro1+nro2+nro3
promedio=print(f'El promedio de los tres nros ingresados es: {sumaNros/3}')