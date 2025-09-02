class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def agregar_arista(self, v1, v2, bidireccional=True):
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)
        self.vertices[v1].append(v2)
        if bidireccional:
            self.vertices[v2].append(v1)


def bfs_distancia_minima(grafo, inicio, fin):
    visitados = set()
    cola = [(inicio, 0)]  # cada elemento: (nodo, distancia)

    while cola:
        actual, dist = cola.pop(0)  # desencolar
        if actual == fin:
            return dist
        if actual not in visitados:
            visitados.add(actual)
            for vecino in grafo.vertices.get(actual, []):
                cola.append((vecino, dist + 1))
    return None


# ---------- Menú para camino más corto ----------
def camino_mas_corto():
    grafo = Grafo()
    print("Agrega las aristas del grafo (deja vacío para terminar):")
    while True:
        v1 = input("Nodo origen: ")
        if v1 == "":
            break
        v2 = input("Nodo destino: ")
        if v2 == "":
            break
        grafo.agregar_arista(v1, v2)

    inicio = input("Nodo inicio: ")
    fin = input("Nodo destino: ")

    distancia = bfs_distancia_minima(grafo, inicio, fin)
    if distancia is not None:
        print(f"La distancia mínima entre {inicio} y {fin} es: {distancia} aristas")
    else:
        print("No hay conexión entre esos nodos.")


# Ejecutar ejemplo
camino_mas_corto()
