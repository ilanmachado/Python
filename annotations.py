class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'

p = Pessoa(nome='Ilan Machado', idade=38, peso=118.7)

print(p.__dict__)

# print(p.__annotations__) Não tem annotations

print(p.andar.__annotations__)

print(p.__init__.__annotations__)
