# Al ejecutar el programa nos da como resultado la ruta absoluta
# en la que se encuentra como primer output. Hay que tener esto claro
# para entender los índices que le vamos a ir colocando al código.

import sys

if len(sys.argv) == 3: # Si los argumentos son igual a 3..
    texto = sys.argv[1] # Aquí por índices se almacena en variable el primer argumento.
    repeticiones = int(sys.argv[2]) # Y aquí el segundo, lo convertimos en int para poder operar

# Ahora iteramos: por cada repetición en el rango de repeticiones, 
# es decir por el número introducido como argumento en linea de comandos
# saca por pantalla el texto(que corresponde al primer argumento)

    for r in range(repeticiones):
        print(texto)

# Si los argumentos no están bien escritos dejamos un mensaje
# aclaratorio
else:
    print("Error - introduce correctamente los argumentos")
    print("Ejemplo: repeticiones.py \"Texto\" 25")