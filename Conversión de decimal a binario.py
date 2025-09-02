class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if self.items else None

    def esta_vacia(self):
        return len(self.items) == 0


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


# ---------- Menú ----------
def convertir_binario():
    numero = int(input("Ingresa un número decimal: "))
    print("Binario:", decimal_a_binario(numero))


convertir_binario()
