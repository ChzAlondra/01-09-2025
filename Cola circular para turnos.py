class ColaCircular:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.indice = 0

    def siguiente_turno(self):
        jugador = self.jugadores[self.indice]
        self.indice = (self.indice + 1) % len(self.jugadores)
        return jugador


def juego_turnos():
    jugadores = input("Ingresa los nombres de los jugadores separados por coma: ").split(",")
    jugadores = [j.strip() for j in jugadores]
    cola = ColaCircular(jugadores)

    while True:
        input("\nPresiona ENTER para siguiente turno (o escribe 'salir' para terminar)...")
        print(f"Turno de: {cola.siguiente_turno()}")


juego_turnos()
