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


# ---------- Menú ----------
def verificar_parentesis():
    expresion = input("Ingresa una expresión matemática: ")
    if parentesis_balanceados(expresion):
        print("✅ Los paréntesis están balanceados")
    else:
        print("❌ Los paréntesis NO están balanceados")


verificar_parentesis()
