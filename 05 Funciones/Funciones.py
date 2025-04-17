"""  1. Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal 

def imprimir_hola_mundo():
  print('Hola mundo!')

imprimir_hola_mundo()

2- Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
 principal solicitando el nombre al usuario. """
""" 
def saludar_usuario(nombre):
  return f'Hola {nombre}'

saludo=saludar_usuario(input('Ingresa tu nombre: '))
print(saludo)

 3. Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados """

""" def informacion_personal(nombre, apellido, edad, residencia):
  print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

nombre=input('ingresa tu nombre: ')
apellido=input('ingresa tu apellido: ')
edad=input('ingresa tu edad: ')
residencia=input('Ingresa tu residencia: ')
informacion_personal(nombre, apellido, edad, residencia)

 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados """
""" 
import math
radio=float(input('Ingresa el radio del circulo: '))

def  calcular_area_circulo(radio):
    area = round(math.pi*(radio**2), 2)
    return f'El area del circulo es: {area}'


def calcular_perimetro_circulo(radio):
  perimetro = round(2 * math.pi * radio, 2)
  return f'El perimetro del circulo es: {perimetro}'


mensaje_perimetro_circulo=calcular_perimetro_circulo(radio)
mensaje_area_circulo=calcular_area_circulo(radio)
print(mensaje_area_circulo)
print(mensaje_perimetro_circulo)

5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función. """

""" segundos=int(input('Ingresa los segundos a convertir: '))

def segundos_a_horas(segundos):
  horas=round(segundos/3600, 2)
  print(f'Los segundos ingresados ({segundos}) son {horas} hs.')

segundos_a_horas(segundos) 


6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción.
 """
""" numero=int(input('Ingresa el numero que uqeres multiplicar: '))

def tabla_multiplicar_numero(numero):
  for i in range(1, 10+1):
    print(f'{numero} * {i} = {numero*i}')

tabla_multiplicar_numero(numero)     """
""" 
7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara. """
""" 
primer_numero=int(input('Ingresa el primer numero: '))
segundo_numero=int(input('ingresa el segundo numero: '))

def operaciones_basicas(a, b):
  suma= primer_numero + segundo_numero
  resta= primer_numero - segundo_numero
  multiplicacion= primer_numero* segundo_numero
  division=round(float(primer_numero/segundo_numero), 2)
  return suma, resta, multiplicacion, division

resultado=operaciones_basicas(primer_numero, segundo_numero)

print(f'*************************************')
print('El resultado de las operaciones es :')
print(f'*************************************')
print(f'SUMA: {primer_numero} + {segundo_numero} = {resultado[0]}')
print(f'RESTA: {primer_numero} - {segundo_numero} = {resultado[1]}')
print(f'MULTIPLICACION: {primer_numero} * {segundo_numero} = {resultado[2]}')
print(f'DIVISION: {primer_numero} / {segundo_numero} = {resultado[3]}')

 """
""" 
 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales """


""" peso=float(input('ingresa tu peso: '))
altura=float(input('Ingresa tu altura: '))

def calcular_imc(peso, altura):
  imc=round(peso/(altura**2),2)

  return imc
resultado=calcular_imc(peso, altura)

print(f'El indice de tu masa corporal es {resultado}') """

"""  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función """

""" temperaturaCelcius=float(input('Ingresa la temperatura en C°: '))

def celsius_a_fahrenheit(celsius):
   conversion=(celsius*1.8)+32
   return conversion

resultado=celsius_a_fahrenheit(temperaturaCelcius)
print(f'{temperaturaCelcius} C° a Farenheit es: {resultado}') """

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función. """

""" a=float(input('Ingresa el primer numero: '))

b=float(input('Ingresa el segund numero: '))

c=float(input('Ingresa el tercer numero: '))


def calcular_promedio(a, b, c):
  promedio= (a+b+c)/3
  return promedio

resultado=calcular_promedio(a,b,c)
print(f'El promedio de sumar {a}, {b} y {c} es {resultado}') """