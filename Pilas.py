class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None


# ---------- 1. Paréntesis balanceados ----------
def parentesis_balanceados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter == "(":
            pila.apilar(caracter)
        elif caracter == ")":
            if pila.esta_vacia():
                return False
            pila.desapilar()
    return pila.esta_vacia()


# ---------- 2. Conversión decimal a binario ----------
def decimal_a_binario(numero):
    pila = Pila()
    if numero == 0:
        return "0"
    while numero > 0:
        pila.apilar(numero % 2)
        numero //= 2
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    return binario


# ---------- 3. Editor de texto con Deshacer ----------
class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.historial = Pila()

    def escribir(self, nuevo_texto):
        self.historial.apilar(self.texto)  # Guardar estado actual
        self.texto += nuevo_texto

    def deshacer(self):
        if not self.historial.esta_vacia():
            self.texto = self.historial.desapilar()

    def mostrar(self):
        print("Texto actual:", self.texto)


# ---------- Menú principal ----------
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Verificar paréntesis balanceados")
        print("2. Convertir número decimal a binario")
        print("3. Editor de texto (con deshacer)")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            expresion = input("Ingresa una expresión matemática: ")
            if parentesis_balanceados(expresion):
                print("✅ Los paréntesis están balanceados")
            else:
                print("❌ Los paréntesis NO están balanceados")

        elif opcion == "2":
            numero = int(input("Ingresa un número decimal: "))
            print("Binario:", decimal_a_binario(numero))

        elif opcion == "3":
            editor = EditorTexto()
            while True:
                print("\n--- EDITOR DE TEXTO ---")
                print("1. Escribir")
                print("2. Deshacer")
                print("3. Mostrar texto")
                print("4. Volver al menú principal")
                subopcion = input("Elige una opción: ")

                if subopcion == "1":
                    nuevo = input("Escribe algo: ")
                    editor.escribir(nuevo)
                elif subopcion == "2":
                    editor.deshacer()
                    print("Última acción deshecha.")
                elif subopcion == "3":
                    editor.mostrar()
                elif subopcion == "4":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


# Ejecutar menú
menu()
