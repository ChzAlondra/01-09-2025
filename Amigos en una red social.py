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


def sugerir_amigos(grafo, persona):
    if persona not in grafo.vertices:
        return []

    amigos = set(grafo.vertices[persona])
    sugerencias = set()

    for amigo in amigos:
        for amigo_de_amigo in grafo.vertices.get(amigo, []):
            if amigo_de_amigo != persona and amigo_de_amigo not in amigos:
                sugerencias.add(amigo_de_amigo)

    return list(sugerencias)


# ---------- Menú para red social ----------
def red_social():
    grafo = Grafo()
    print("Agrega amistades (deja vacío para terminar):")
    while True:
        p1 = input("Persona 1: ")
        if p1 == "":
            break
        p2 = input("Persona 2: ")
        if p2 == "":
            break
        grafo.agregar_arista(p1, p2)

    persona = input("Ingresa la persona para sugerencias de amigos: ")
    sugerencias = sugerir_amigos(grafo, persona)
    if sugerencias:
        print(f"Sugerencias de amigos para {persona}: {', '.join(sugerencias)}")
    else:
        print(f"No hay sugerencias para {persona}")


# Ejecutar ejemplo
red_social()
