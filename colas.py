
# Creamos la variable mi_cola donde almacenara los datos.

# creamos la lista vacia nombrada mi_cola
mi_cola = []

# Imprimimos en pantalla
print(mi_cola)
    
mi_cola[2]
# El Resultado sera "Josue", porque los arreglos comienzan en cero.

mi_cola[5]
# El Resultado sera "Jochimin", porque los arreglos comienzan en cero.
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
# Resultado sera:
['Joselito', 'Chantal', 'Josue', 'Mijarex', 'Francelys', 'Jochimin', 'Polanco']


# Para Leer un elemento en una cola.
# en ese caso utilizaremos los index del arreglo
# de nuestra lista, para acceder a dicho indice utilizamos
# los corchetes y dentro de estos assignamos el numero del indice que queremos.

mi_cola[0] # Este indice muestra la posicion en la lista
mi_cola[3] # El Resultado sera "Joselito", porque los arreglos comienzan en cero.
# El Resultado sera "J", porque los arreglos comienzan en cero.


# Para realizar algo mas dinamico con las listas
# crearemos una clase llamada Cola y agregaremos metodos
# para interactuar y personalizar los metodos ya existentes de las listas.



# Creamos la clase Cola
class Cola:

    # Inicializamos nuestra clase y creamos una variable
    # llamada mi mi_cola que es una lista vacia.
    
    def _init_(self):
        self.mi_cola = []


    # Verificamos si la lista esta vacia
    # En caso de no estar vacia nos devuelve los elementos que 
    # los componen.

    def esta_vacia(self):
        if not self.mi_cola:
            print("Cola Vacia")
        else:
            print("Cola con elementos", self.mi_cola)
