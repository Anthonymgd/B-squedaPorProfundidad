# Se importa la librería de Lifo y Fifo
# Queue: módulo que implementa colas multi-productor y multi-consumidor.
from queue import Queue

class Grafo:
    """
    Una clase que representa a un grafo.

    ...
    
    Argumentos
    ----------
    num_nodos: entero
        Es usado para determinar el número de nodos.
    dirigido: booleano
        Determina si el nodo es dirigido. Valor por defecto "Verdadero".

    Atributos
    ---------
    matriz_num_nodos : entero
        Número de nodos en el grafo.
    matriz_nodos : entero
        Clave del nodo generado.
    matriz_dirigido : booleano
        Determina si el nodo es dirigido.
    matriz_lista_adyacencia: diccionario
        Almacena los nodos como  un conjunto no ordenado de pares clave-valor.

    Métodos
    -------
    agregar_arista(self, nodo1, nodo2, peso=1):
        Agrega una arista o arco entre dos nodos a la representación del grafo.

    imprimir_lista_adyacencia(self):
        Imprime la lista de adyacencia como representación del grafo.

    bpp(self, nodo_inicial):
        Imprime el recorrido del algoritmo de búsqueda por profunidad desde un nodo dado hasta un nodo objetivo.
    """
    # Se establece el constructor de la clase
    def __init__(self, num_nodos, dirigido=True):
        """
        Contructor con todos los atributos necesarios para la clase grafo.

        Parámetros
        ----------
        matriz_num_nodos : entero
            Número de nodos en el grafo.
        matriz_nodos : entero
            Clave del nodo generado.
        matriz_dirigido : booleano
            Determina si el nodo es dirigido.
        matriz_lista_adyacencia: diccionario
            Almacena los nodos como  un conjunto no ordenado de pares clave-valor.
        """
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
        """
        Agrega una arista o arco entre dos nodos a la representación del grafo.

        El último argumento, peso, tiene como valor asignado 1.

        Parámetros
        ----------
        nodo1 : entero
            Almacena el valor para el primer nodo.
        nodo2 : entero
            Almacena el valor para el segundo nodo.
        nodo1 : entero
            Almacena el peso de los arcos, línea que une los nodos. Valor por defecto 1. 

        Retorna
        -------
        A un index del diccionario establecido, matriz_lista_adyacencio[clave], se le 
        añadirá su nodo adyacente, nodo# y el peso. 
        """
        # Añade una arista del nodo 1 al 2 con peso por defecto 1
        self.matriz_lista_adyacencia[nodo1].add((nodo2, peso))
        # Si la matriz no es dirigida, añade una arista del nodo 2 al 1 con peso por defecto 1
        if not self.matriz_dirigido:
            self.matriz_lista_adyacencia[nodo2].add((nodo1, peso))
   
    # Función que imprime la lista de adyacencia
    def imprimir_lista_adyacencia(self):
        """
        Imprime la lista de adyacencia como representación del grafo.

        Parámetros
        ----------
        Ninguno

        Retorna
        -------
        Una cadena de texto con la matriz de adyacencia generada.
        """
        for key in self.matriz_lista_adyacencia.keys():
            print("node", key, ": ", self.matriz_lista_adyacencia[key])
 
    # Función que imprime el recorrido de la busqueda por anchura de un vértice fuente dado.
    def bpp(self, nodo_inicial, nodo_objetivo, camino = [], visitado = set()):
        """
        Imprime el recorrido del algoritmo de búsqueda por profunidad desde un nodo dado hasta un nodo objetivo.

        Parámetros
        ----------
        nodo_inicial : entero
            Representa al nodo raíz del grafo generado.
        nodo_objetivo : entero
            Representa al nodo objetivo a encontrar en grafo generado.
        camino : lista
            Almacena el camino requerido para llegar al objetivo en caso de existir.
        visitado : colección
            Almacena los nodos que han sido visitados.

        Retorna
        -------
        Una lista del camino generado desde un nodo origen hasta el nodo objetivo.
        """
        # Se inicializa la lista añdiendo el nodo inicial al camino
        camino.append(nodo_inicial)
        # Se marca como visitado al nodo inicial
        visitado.add(nodo_inicial)
        # Si el nodo inicial es igual que le nodo objetivo retorna el camino como respuesta
        if nodo_inicial == nodo_objetivo:
            return camino
        # Recorrer cada nodo vecino, con su peso, presentes en la lista de adyacencia con la clave nodo incial 
        for(vecino, peso) in self.matriz_lista_adyacencia[nodo_inicial]:
            # Si el nodo adyacente encontrado no ha sido visitado
            if vecino not in visitado:
                # Se genera la recursividad del algoritmo bpp
                # con el nuevo nodo descubierto 
                resultado = self.bpp(vecino, nodo_objetivo, camino, visitado)
                # Si el nodo adyacente del nodo descubierto no existe retorna el camino y continúa con la otra rama del grafo.
                if resultado is not None:
                    return resultado
        # Presenta la información de la lista y la vacía
        camino.pop()
        # No retorna nada
        return None
if __name__ == "__main__":
    #Ejecución del algoritmo búsqueda por anchura
    #Se instancia la clase
    # Primer caso
    grafo = Grafo(7, dirigido=False)
 
    # Añade las aristas con peso por defecto 1
    grafo.agregar_arista(0, 1)
    grafo.agregar_arista(0, 2)
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(1, 4)
    grafo.agregar_arista(2, 3)
    grafo.agregar_arista(2, 5)
    grafo.agregar_arista(3, 4)
    grafo.agregar_arista(3, 5)
    grafo.agregar_arista(4, 5)
    grafo.agregar_arista(4, 6)
    grafo.agregar_arista(5, 6)

    # Imprime la lista de adyacencia como tipo de dato "diccionario": {(nodo, peso)}
    grafo.imprimir_lista_adyacencia()
    # Imprime el recorrido con el algoritmo de búsqueda por profundidad
    camino_resultante = []
    camino_resultante = grafo.bpp(0, 6)
    print(f"El camino obtenido desde el nodo 0 hasta el 6 es: {camino_resultante}")

    # Se da un salto de línea
    print()
