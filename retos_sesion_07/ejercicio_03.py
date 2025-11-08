class Romano:
    def __init__(self, valor_romano):
        self.valor_romano = valor_romano
        self.valor_entero = self.convertir_a_entero(valor_romano)

    def convertir_a_entero(self, valor):
        valores_enteros = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000
        }
        total = 0
        anterior = 0

        for romano in reversed(valor):
            actual = valores_enteros[romano]
            if actual < anterior:
                total -= actual
            else:
                total += actual
            anterior = actual

        return total

    def convertir_a_romano(self, numero):
        valores_romanos = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        resultado = ""

        for entero, romano in valores_romanos:
            while numero >= entero:
                resultado += romano
                numero -= entero

        return resultado

    def __add__(self, segundo_valor):
        resultado_entero = self.valor_entero + segundo_valor.valor_entero
        resultado_romano = self.convertir_a_romano(resultado_entero)
        return Romano(resultado_romano)

    def __str__(self):
        return self.valor_romano

num_1 = Romano("X")  
num_2 = Romano("V")   
resultado = num_1 + num_2
print(resultado)   
num_1 = Romano("V")  
num_2 = Romano("IV")   
resultado = num_1 + num_2
print(resultado) 
num_1 = Romano("L")  
num_2 = Romano("IL")   
resultado = num_1 + num_2
print(resultado) 