#  SEMANAS 01 _ 02 
#  Comparación de los lenguajes de programación JAVA, PYTHON y C 
#%% Operaciones Básicas:
# 1. Realiza la suma, resta, multiplicación y división de 

#  PEDIMOS AL USUARIO PARA QUE INGRESE DOS NUMEROS
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# REALIZAMOS LAS OPERACIONES 
suma = num1 + num2   # SUMA
resta = num1 - num2   #RESTA
multiplicacion = num1 * num2  #MULTIPLICACION

if num2 != 0: # ASEGURAMOS QUE EL SEGUNDO NUM SEA DIFERENTE DE SERO
    division = num1 / num2 # DIVIDIMOS AMBOS NUMEROS
else:
    division = "No es posible dividir por cero." # SI EL SEGUNO VALOR ES CERO NOS DEVUELVE ESTE TEXTO

# IMPRIMIMOS LOS RESULTADOS
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#%%  Verificación de Número Par o Impar:
# 2.Solicita un número al usuario y determina si es par o impar.

# PEDIMOS AL USUARION QUE INGRESE UN NUMERO
numero = int(input("Ingresa un número: "))

# DETERMINAMOS SI ES PAR O IMPAR
if numero % 2 == 0:
    print(f"{numero} es un número par.") #IMPRIME QUE ES UN PAR
else:
    print(f"{numero} es un número impar.") #IMPRIME QUE ES UN IMPAR
    
#%% Área de un Triángulo: 
# 3. Pide la base y la altura de un triángulo al usuario y calcula su área. 

# PEDIMOS AL USUARION QUE NOS DE VALIRES PARA LA ALTURA Y BASE  DEL TRIANGULO
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# IMPLEMENTAMOS LA FORMULA PARA HALLAR EL AREA DEL TRIANGULO
area_triangulo = (base * altura) / 2

# IMPRIMIMOS EL RESULTADO
print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo:.2f}")
    

#%% Calculadora de Factorial: 
# 4. Crea una función que calcule la factorial de un número. 

def factorial(n):
    if n == 0 or n == 1: #verificamos si el valor de n es igual a 0 o 1.
        return 1
    else:
        return n * factorial(n-1)# calculamos el factorial de n multiplicándolo por el factorial de n-1

# PEDIMOS UN NUMERO AL USUARIO
numero = int(input("Ingresa un número: "))

# CALCULAMOS EL FACTORIAL Y MOSTRAMOS EL RESULTADO
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#%% Número Primo: 
# 5. Verifica si un número ingresado por el usuario es primo o no.

def es_primo(numero):
    if numero < 2:#Comprueba si el número es menor que 2
        return False #Si el número es menor que 2, devuelve False
    for i in range(2, int(numero**0.5) + 1):#Inicia un bucle for que itera sobre los valores de i desde 2 hasta la raíz cuadrada entera de numero más 1.
        if numero % i == 0:# En cada iteración, verifica si el número es divisible por i
            return False
    return True

# SOLICITAMMOS INGRESAR UN NUMERO
numero_usuario = int(input("Ingresa un número: "))

# VERIFICAMOS SI EL NUMERO ES PRIMO Y NOS IMPRIME EL RESULTADO
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")


#%% Inversión de Cadena:
# 6. Toma una cadena de texto y muestra su inversión. 

def invertir_cadena(cadena):
    cadena_invertida = cadena[::-1]# Utilizamos la notación de rebanado para crear una versión invertida de la cadena
    return cadena_invertida

# PEDIMOS AL USUARIO QUE INGRESE UNA CADENA
cadena_original = input("Ingresa una cadena de texto: ")

# OBTENEMOS LA CADENA INVERTIDA Y NOS MUESTRA EL RESULTADO
resultado = invertir_cadena(cadena_original)
print(f"La cadena invertida es: {resultado}")

#%% Suma de Números Pares: 
# 7.Calcula la suma de los números pares en un
# rango especificado por el usuario.

# PEDIMOS AL USUARIO QUE INGRESE 2 NUMERO CON UN RANGO
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))

# INICIAMOS LA SUMA Y GUARDAMOS EL VALOR EN UN VARIABLE
suma_pares = 0

# CALCULAMOS LA SUMA DE LOS NUMEROS PARES EN EL RANGO ESCRITO
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma_pares += numero

#IMPRIMIMOS EL RESULTADO
print(f"La suma de los números pares en el rango [{inicio}, {fin}] es: {suma_pares}")


#%% Lista de Cuadrados:
# 8.  Crea una lista de los cuadrados de los primeros 10 números naturales.

# CREAMOS LA LISTA DE LOS 10 PRIMEROS NUMERO CALCULANDO SUS CUADRADOS
cuadrados = [n**2 for n in range(1, 11)]

# IMPRIMIMOS LOS RESULTADOS
print("Lista de cuadrados de los primeros 10 números naturales:")
print(cuadrados)


#%% Contador de Vocales: 
# 9. Cuenta el número de vocales en una cadena de texto. 

# SOLCITAMOS AL USUARIO QUE INGRESE UN TEXTO
cadena = input("Ingresa una cadena de texto: ")

# INICIAMOS EL CONTADOR DE LAS VOCALES
contador_vocales = 0

# DEFINIMOS LAS VOCALES MAYUSCULAS O MINUSCULAS
vocales = "aeiouAEIOU"

# CONTAMOS EL NUMERO DE VOCALES EN LA CADENA
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

# IMPRIMIMOS EL RESULTADO
print(f"El número de vocales en la cadena es: {contador_vocales}")



#%% Números de la Serie Fibonacci:
# 10.Genera los primeros 10 números de la serie Fibonac

#CREMOS LA FUNCION PARA GENERAR LOS PRIMEROS N NUMERO DE FIBONACCI
def fibonacci(n):
    fib_series = [0, 1]  # Inicializamos la serie con los primeros dos números
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# OBTENEMOS LOS 10 PRIMEROS NUMEROS

primeros_10_fibonacci = fibonacci(10)

# MOSTRANMOS EL RESLTADO IMPRIMIENDONOS LA RESPUESTA

print("Primeros 10 números de la serie Fibonacci:")
print(primeros_10_fibonacci)

#%% Ordenamiento de Lista: 
#11.Ordena una lista de números ingresados por el usuario de menor a mayor.

# PEDIMOS AL USUARIO QUE INGRESE NUMEROS
entrada_usuario = input("Ingresa una lista de números: ")

# CONVERTIMOS LOS NUMEROS INGRESADOS EN UNA LISTA
numeros = [float(numero) for numero in entrada_usuario.split()]

# ORDENAMOS LOS NUMERO DE LA LINSTA DE MENOR A MAYOR
numeros_ordenados = sorted(numeros)

# IMPRIMIMOS LA RESPUESTA
print("Lista ordenada de menor a mayor:", numeros_ordenados)

#%% Palíndromo: 
# 12. Verifica si una palabra ingresada por el usuario es un palíndromo. 


def es_palindromo(palabra):
    palabra = palabra.lower()  # Convierte la cadena de entrada a minúsculas
    palabra_invertida = palabra[::-1]   # Crea una versión invertida de la cadena
    
    return palabra == palabra_invertida

# SOLICITAMOS AL USUARIO QUE INGRESE UNA PALABRA
palabra_usuario = input("Ingresa una palabra: ")

# VEREFICAMOS SI LA PALABRA ES UN PALINDROMO Y MOSTRAMOS EL RESULTADO
if es_palindromo(palabra_usuario):
    print(f"{palabra_usuario} es un palíndromo.")
else:
    print(f"{palabra_usuario} no es un palíndromo.")
    
    
#%% Generador de Tablas de Multiplicar: 
# 13. Crea un programa que genere la tabla de multiplicar 
#     de un número ingresado por el usuario.

# PEDIMOS AL USUARIO QUE INGRESE UN NUMERO
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11): #Esto inicia un bucle
    resultado = numero * i #: En cada iteración del bucle, calcula el resultado de la multiplicación del número dado
    print(f"{numero} x {i} = {resultado}")




#%% Cálculo del Área de un Círculo: 
# 14. Pide el radio de un círculo al usuario y calcula su área. 

import math

# PIDE UN RADIO AL USUARIO
radio = float(input("Ingresa el radio del círculo: "))

# CALCULAMOS EL AREA DEL CIRCULO CON LA FORMULA
area_circulo = math.pi * radio**2

# IMPRIME EL RESULTADO
print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")


#%% Suma de Dígitos: 
# 15.  Toma un número entero y calcula la suma de sus dígitos.

# PEDIMOS AL USUARION QUE INGRESE UN NUMERO ENTERO
numero = int(input("Ingresa un número entero: "))

# CALCULAMOS LA SUMA DE LOS DIGITOS
suma_digitos = sum(int(digito) for digito in str(abs(numero)))

# IMPRIME EL RESULTADO
print("La suma de los dígitos es:", suma_digitos)


