
# Creamos la variable mi_cola donde almacenara los datos.

# creamos la lista vacia nombrada mi_cola
mi_cola = []

# Imprimimos en pantalla
print(mi_cola)

# En la terminal debemos ver los siguiente resultado:

#  []

# Podemos agregar los elementos directamente a la lista

mi_cola = [1,2,3,4,'Grupo4']

# Verificamos si nuestra cola contiene elementos

if not mi_cola:
    print("Cola Vacia!")
else:
    print("Cola con elementos", mi_cola)
    
# Anadir elementos a la cola.

# Para anadir elementos a una cola necesitamos el metodo append()
# Este metodo agrega un elemento al final de una lista.

# aqui agragamos el elemento numero 1 a nuestra cola
# y asi sucecivamente vamos agregamos.

mi_cola.append("Joselito")
mi_cola.append("Chantal")
mi_cola.append("Josue")
mi_cola.append("Mijarex")
mi_cola.append("Francelys")
mi_cola.append("Jochimin")
mi_cola.append("Polanco")

# Mostramos el resultado en pantalla.

print(mi_cola)
