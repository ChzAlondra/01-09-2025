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

    def mostrar(self):
        return self.items


def cajero_automatico():
    cola = Cola()
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Llegada de cliente")
        print("2. Atender cliente")
        print("3. Mostrar fila")
        print("4. Salir")

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


cajero_automatico()
