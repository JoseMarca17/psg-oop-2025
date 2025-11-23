class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, fraccion_2):
        nume = self.numerador * fraccion_2.denominador + fraccion_2.numerador * self.denominador
        deno = self.denominador * fraccion_2.denominador
        return Fraccion(nume, deno)

    def __sub__(self, fraccion_2):
        nume = self.numerador * fraccion_2.denominador - fraccion_2.numerador * self.denominador
        deno = self.denominador * fraccion_2.denominador
        return Fraccion(nume, deno)

    def __mul__(self, fraccion_2):
        return Fraccion(self.numerador * fraccion_2.numerador,
                        self.denominador * fraccion_2.denominador)

    def __truediv__(self, fraccion_2):
        return Fraccion(self.numerador * fraccion_2.denominador,
                        self.denominador * fraccion_2.numerador)

    def __eq__(self, fraccion_2):
        return self.numerador * fraccion_2.denominador == fraccion_2.numerador * self.denominador

    def __lt__(self, fraccion_2):
        return self.numerador * fraccion_2.denominador < fraccion_2.numerador * self.denominador

    def __gt__(self, fraccion_2):
        return self.numerador * fraccion_2.denominador > fraccion_2.numerador * self.denominador

    def __ne__(self, fraccion_2):
        return not self.__eq__(fraccion_2)


a = Fraccion(5, 8)
b = Fraccion(1, 4)
c = Fraccion(3, 2)
d = Fraccion(7, 9)

print("Fracciones: ", a,b,c,d)
print(f"Suma: {a} + {b} = ", a + b)
print(f"Resta: {c} - {d} =", c - d)
print(f"Multiplicacion: {a} * {d} = ", a * d)
print(f"Division: {c} / {b}", c / b)
print(f"Igualdad: {d} == {b}: ", d == b)
print(f"Menor que: {a} < {b}: ", a < b)
print(f"Mayor que: {c} > {d}: ", c > d)
print(f"Desigualdad: {a} != {b}: ", b != d)
