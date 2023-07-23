entero=200
doble=2.45
flotante=2.16
caracter="D"
booleano=True
cadena="strings"
resultado=" el dato de tipo entero es: "+ str(entero)+ "\n el dato de tipo doble es: " + str(doble)+\
    "\nel dato de tipo flotante es: "+str(flotante)+"\nel dato de tipo caracter es: "+str(caracter)+\
        "\nel daato de tipo booleanos es: "+str(booleano)+"\nel dato de tipo cadena es: "+str (cadena)
        
print(resultado)

"""Límite inferior y superior para tipos de datos enteros: En Python 2, los enteros tienen un límite determinado 
por la arquitectura de la máquina, y los límites típicos son aproximadamente -2,147,483,648 a 2,147,483,647 
para sistemas de 32 bits. En Python 3, los enteros son de precisión arbitraria y no tienen un límite fijo."""

"""Límite inferior (más cercano a cero) en los tipos de datos flotantes : El valor más pequeño que se puede representar en Python como número de 
punto flotante es aproximadamente ±2.2250738585072014 x 10^-308. Cualquier valor más pequeño que este se considerará 
como cero. ese numero es aproximadamente el ±0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000022250738585072014"""

"""Límite superior (más cercano a infinito) en los tipos de dato flotante: El valor más grande que se puede representar en Python como número de
punto flotante es aproximadamente ±1.7976931348623157 x 10^308. Cualquier valor más grande que este se considerará 
como infinito (positivo o negativo). este numero seria muy grande """

print(" ")
n= int(input("ingrese la cantidad de pares que desea sumar"))

# formula para hallar el valor de la suma de los primeros n numeros pares 
sumatoria=n * (n+1)

# ahora imprimimos el resultado
print (" el resultado de la suma de los pares es : "+ str(sumatoria))




