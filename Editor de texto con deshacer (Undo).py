class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if self.items else None

    def esta_vacia(self):
        return len(self.items) == 0


class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.historial = Pila()

    def escribir(self, nuevo_texto):
        self.historial.apilar(self.texto)
        self.texto += nuevo_texto

    def deshacer(self):
        if not self.historial.esta_vacia():
            self.texto = self.historial.desapilar()

    def mostrar(self):
        print("Texto actual:", self.texto)


# ---------- Menú ----------
def editor_con_undo():
    editor = EditorTexto()
    while True:
        print("\n--- EDITOR DE TEXTO ---")
        print("1. Escribir")
        print("2. Deshacer")
        print("3. Mostrar texto")
        print("4. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            texto = input("Escribe algo: ")
            editor.escribir(texto)
        elif opcion == "2":
            editor.deshacer()
            print("Última acción deshecha.")
        elif opcion == "3":
            editor.mostrar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


editor_con_undo()
