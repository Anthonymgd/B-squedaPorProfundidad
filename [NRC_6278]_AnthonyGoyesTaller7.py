# Se importa la librería de Lifo y Fifo
# Queue: módulo que implementa colas multi-productor y multi-consumidor.
from queue import Queue

class Grafo:
    # Se establece el constructor de la clase
    def __init__(self, num_nodos, dirigido=True):
 
        # Se inicializan los atributos de la clase
        # Atributo: número de nodos
        self.matriz_num_nodos = num_nodos
        # Se establece que el nodo debe estar en el rango permitido
        self.matriz_nodos = range(self.matriz_num_nodos)
        # Atributo: dirigido. Por defecto "Verdadero"
        self.matriz_dirigido = dirigido
        #Representación gráfica con una lista de adyacencia
        #Se genera un diccionario y se settea todos los nodos con un ciclo repetitivo "para"
        self.matriz_lista_adyacencia = {nodo: set() for nodo in self.matriz_nodos}    
         
    #  Función que agrega una arista o arco entre dos nodos a la representación del grafo
    def agregar_arista(self, nodo1, nodo2, peso=1):
        # Añade una arista del nodo 1 al 2 con peso por defecto 1
        self.matriz_lista_adyacencia[nodo1].add((nodo2, peso))
        # Si la matriz no es dirigida, añade una arista del nodo 2 al 1 con peso por defecto 1
        if not self.matriz_dirigido:
            self.matriz_lista_adyacencia[nodo2].add((nodo1, peso))
   
    # Función que imprime la lista de adyacencia
    def imprimir_lista_adyacencia(self):
        for key in self.matriz_lista_adyacencia.keys():
            print("node", key, ": ", self.matriz_lista_adyacencia[key])
 
    # Función que imprime el recorrido de la busqueda por anchura de un vértice fuente dado.
    def dfs(self, nodo_inicial, nodo_objetivo, camino = [], visitado = set()):
        camino.append(nodo_inicial)
        visitado.add(nodo_inicial)
        if nodo_inicial == nodo_objetivo:
            return camino
        for(vecino, peso) in self.matriz_lista_adyacencia[nodo_inicial]:
            if vecino not in visitado:
                resultado = self.dfs(vecino, nodo_objetivo, camino, visitado)
                if resultado is not None:
                    return resultado
 
        camino.pop()
        return None
if __name__ == "__main__":
