class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def agregar_arista(self, v1, v2, peso, bidireccional=True):
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)
        self.vertices[v1].append((v2, peso))
        if bidireccional:
            self.vertices[v2].append((v1, peso))


def dijkstra(grafo, inicio):
    # Inicializar distancias
    distancias = {v: float("inf") for v in grafo.vertices}
    distancias[inicio] = 0
    visitados = set()

    while len(visitados) < len(grafo.vertices):
        # Elegir el nodo no visitado con la distancia mínima
        no_visitados = {v: distancias[v] for v in grafo.vertices if v not in visitados}
        if not no_visitados:
            break
        actual = min(no_visitados, key=no_visitados.get)
        visitados.add(actual)

        for vecino, peso in grafo.vertices[actual]:
            if distancias[actual] + peso < distancias[vecino]:
                distancias[vecino] = distancias[actual] + peso

    return distancias


# ---------- Menú para Dijkstra ----------
def dijkstra_menu():
    grafo = Grafo()
    print("Agrega aristas con peso (deja vacío para terminar):")
    while True:
        v1 = input("Nodo origen: ")
        if v1 == "":
            break
        v2 = input("Nodo destino: ")
        if v2 == "":
            break
        peso = input("Peso (número positivo): ")
        if peso == "":
            break
        grafo.agregar_arista(v1, v2, float(peso))

    inicio = input("Nodo origen para Dijkstra: ")
    if inicio not in grafo.vertices:
        print("Nodo inexistente en el grafo.")
        return

    distancias = dijkstra(grafo, inicio)
    print(f"Distancias mínimas desde {inicio}:")
    for nodo, distancia in distancias.items():
        print(f"{nodo}: {distancia}")


# Ejecutar ejemplo
dijkstra_menu()
