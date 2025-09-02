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


def caminos_dfs(grafo, inicio, fin, camino=[]):
    camino = camino + [inicio]
    if inicio == fin:
        return [camino]
    if inicio not in grafo.vertices:
        return []
    caminos = []
    for vecino in grafo.vertices[inicio]:
        if vecino not in camino:
            nuevos = caminos_dfs(grafo, vecino, fin, camino)
            for c in nuevos:
                caminos.append(c)
    return caminos


# ---------- Menú para mapa de rutas ----------
def mapa_rutas():
    grafo = Grafo()
    print("Agrega las aristas del grafo (deja vacío para terminar):")
    while True:
        v1 = input("Ciudad origen: ")
        if v1 == "":
            break
        v2 = input("Ciudad destino: ")
        if v2 == "":
            break
        grafo.agregar_arista(v1, v2)

    inicio = input("Ciudad de inicio: ")
    fin = input("Ciudad de destino: ")

    caminos = caminos_dfs(grafo, inicio, fin)
    if caminos:
        print("Caminos posibles entre", inicio, "y", fin, ":")
        for c in caminos:
            print(" → ".join(c))
    else:
        print("No hay caminos posibles entre esas ciudades.")


# Ejecutar ejemplo
mapa_rutas()
