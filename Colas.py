class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def frente(self):
        return self.items[0] if not self.esta_vacia() else None

    def mostrar(self):
        return self.items


# ---------- 4. Simulación de cajero automático ----------
def cajero_automatico():
    cola = Cola()
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Llegada de cliente")
        print("2. Atender cliente")
        print("3. Mostrar fila")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            transaccion = input("Tipo de transacción (retiro/deposito/consulta): ")
            cola.encolar((nombre, transaccion))
            print(f"Cliente {nombre} agregado a la fila.")
        elif opcion == "2":
            cliente = cola.desencolar()
            if cliente:
                print(f"Atendiendo a {cliente[0]} - Transacción: {cliente[1]}")
            else:
                print("No hay clientes en la fila.")
        elif opcion == "3":
            print("Fila actual:", cola.mostrar())
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


# ---------- 5. Cola circular para turnos ----------
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
        input("\nPresiona ENTER para siguiente turno...")
        print(f"Turno de: {cola.siguiente_turno()}")


# ---------- 6. Impresora compartida ----------
def impresora():
    cola = Cola()
    while True:
        print("\n--- IMPRESORA COMPARTIDA ---")
        print("1. Enviar documento")
        print("2. Imprimir documento")
        print("3. Mostrar cola de impresión")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            doc = input("Nombre del documento: ")
            tam = input("Tamaño del documento (páginas): ")
            cola.encolar((usuario, doc, tam))
            print(f"Documento '{doc}' de {usuario} agregado a la cola.")
        elif opcion == "2":
            documento = cola.desencolar()
            if documento:
                print(f"Imprimiendo '{documento[1]}' de {documento[0]} ({documento[2]} páginas)")
            else:
                print("No hay documentos en la cola.")
        elif opcion == "3":
            print("Cola de impresión:", cola.mostrar())
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


# ---------- Menú principal ----------
def menu():
    while True:
        print("\n=== MENÚ COLAS ===")
        print("4. Simulación de cajero automático")
        print("5. Cola circular para turnos")
        print("6. Impresora compartida")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "4":
            cajero_automatico()
        elif opcion == "5":
            juego_turnos()
        elif opcion == "6":
            impresora()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


# Ejecutar menú
menu()
