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

    x = "s" 
    while x == "s" or x=="S":
        print(f"Turno de: {cola.siguiente_turno()}")
        x = input("\nEscribe 's' para siguiente turno o cualquier otro caracter para terminar: ").strip().lower()

juego_turnos()
