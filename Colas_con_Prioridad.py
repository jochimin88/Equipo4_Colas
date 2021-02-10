#cometarios #
#MODULO queue El módulo estándar Queue o queue (Python 2 o 3, respectivamente) permite crear y trabajar con colas de manera sencilla. 
#Es generalmente utilizado en programas multi-hilo, ya que provee una forma de intercambiar información entre threads de manera segura.

#Priority Queue (cola de prioridad): el ítem de menor valor es el primero en ser retornado.
from queue import PriorityQueue


def eliminaMayorPrioridad(self):
    self.queue = self.queue[1:]


PriorityQueue.eliminaMayorPrioridad = eliminaMayorPrioridad

class Curso():#Creando una clase llamada curso#
    
    def __init__(self, prioridad, nombre):# Aqui creamos un iniciador colocamos a self con los siguientes parametros#
        self.prioridad = prioridad  #  Tenemos una atributo llamado prioridad y le agsinamos el contenido del parametro prioridad# 
        self.nombre = nombre #  Tenemos una atributo llamado nombre y le agsinamos el contenido del parametro nombre#
    
    def __lt__(self, otro):#metodo lestar como menor que ,Siendo necesario devolver el objeto resultante de la operación o el resultado en el caso de ser una operación lógica#
        return self.prioridad < otro.prioridad # retornamos la siguiente expresion prioridad es menor a la prioridad del otro elemento .
    
#comentarios#
# el metodo put inserta item en la cola ,En las colas de prioridad los ítems generalmente se insertan como una tupla#
#indicando el número en el primer lugar y los datos en el segundo. Por ejemplo#
    
cursos = PriorityQueue() # creamos una variables de nombre curso instanciando la libreria PriorityQueue#
cursos.put(Curso(3, 'Python'))#agregando las colas con el metodo put#
cursos.put(Curso(10, 'C++'))#agregando las colas con el metodo put#
cursos.put(Curso(1, 'java'))#agregando las colas con el metodo put#

cursos.eliminaMayorPrioridad()

while not cursos.empty():# haciendo un ciclo preguntando si esta vacio#
    c = cursos.get()
    print(c.prioridad,c.nombre)# Imprimos la prioridad y el nombre del curso#
