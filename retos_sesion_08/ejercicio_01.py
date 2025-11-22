class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otro):
        if isinstance(otro, Fraccion):
            nume = self.numerador * otro.denominador + otro.numerador * self.denominador
            deno = self.denominador * otro.denominador
            return Fraccion(nume, deno)
        return NotImplemented

    def __sub__(self, otro):
        if isinstance(otro, Fraccion):
            nume = self.numerador * otro.denominador - otro.numerador * self.denominador
            deno = self.denominador * otro.denominador
            return Fraccion(nume, deno)
        return NotImplemented

    def __mul__(self, otro):
        if isinstance(otro, Fraccion):
            return Fraccion(self.numerador * otro.numerador, self.denominador * otro.denominador)
        return NotImplemented

    def __truediv__(self, otro):
        if isinstance(otro, Fraccion):
            return Fraccion(self.numerador * otro.denominador, self.denominador * otro.numerador)
        return NotImplemented

    def __eq__(self, otro):
        if isinstance(otro, Fraccion):
            return self.numerador * otro.denominador == otro.numerador * self.denominador
        return False

    def __lt__(self, otro):
        if isinstance(otro, Fraccion):
            return self.numerador * otro.denominador < otro.numerador * self.denominador
        return False

    def __gt__(self, otro):
        if isinstance(otro, Fraccion):
            return self.numerador * otro.denominador > otro.numerador * self.denominador
        return False

    def __ne__(self, otro):
        return not self.__eq__(otro)

a = Fraccion(1, 2)
b = Fraccion(3, 4)

print(a, b)
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicacion:", a * b)
print("Division:", a / b)
print("Igualdad:", a == b)
print("Menor que:", a < b)
print("Mayor que:", a > b)
print("Desigualdad:", a != b)
