import random

class DadosDeLaSuerte:
    """Clase que implementa la logica del juego de dados segun reglas de suma."""

    def lanzar_dados(self) -> tuple[int, int]:
        """Simula el lanzamiento de dos dados.

        Returns:
            tuple[int, int]: Un par de enteros entre 1 y 6.
        """
        return random.randint(1, 6), random.randint(1, 6)

    def jugar(self) -> None:
        """Ejecuta el flujo principal del juego y evalua en base a las reglas 
            de victoria/derrota."""
        jugando: bool = True
        
        while jugando:
            dado1, dado2 = self.lanzar_dados()
            suma: int = dado1 + dado2
            print(f"Lanzamiento: {dado1} + {dado2} = {suma}")

            if suma in (7, 11):
                print("¡Ganaste!")
                jugando = False
            elif suma in (2, 3, 12):
                print("Perdiste.")
                jugando = False
            else:
                respuesta: str = input("No ganaste ni perdiste. ¿Quieres lanzar de nuevo? (SI/NO): ").upper()
                if respuesta != "SI":
                    print(f"Juego terminado. Resultado final: {suma}")
                    jugando = False

if __name__ == "__main__":
    juego = DadosDeLaSuerte()
    juego.jugar()