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


def impresora():
    cola = Cola()
    while True:
        print("\n--- IMPRESORA COMPARTIDA ---")
        print("1. Enviar documento")
        print("2. Imprimir documento")
        print("3. Mostrar cola de impresión")
        print("4. Salir")

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


impresora()
