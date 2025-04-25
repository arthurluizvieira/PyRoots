# Este código que fiz é um exemplo didático onde busquei utilizar todos as "etapas" de POO.
# Contém as três principais características de um POO: Herança, Polimorfismo e Encapsulamento.

class Veiculo:      # Criando a classe "mãe", a classe PRINCIPAL
    def __init__(self, marca:str, modelo:str, ano: int) -> None:
        self.__marca = marca  # Encapsulamento Privado
        self.__modelo = modelo  # Encapsulamento Privado
        self.__ano = ano        # Encapsulamento Privado
    

    # Aqui começa a setar os getters e setters 

    @property
    def marca(self) -> str:
        return self.__marca
    
    @marca.setter
    def marca(self, marca:str)->None:
        self.__marca = marca
    
    @property
    def modelo(self)-> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo:str)->None:
        self.__modelo = modelo
    
    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano(self, ano:int)->None:
        self.__ano = ano

    # Aqui termina de setar os getters e setters
    

    # Aqui começa o Polimorfismo onde um mesmo nome vai se comportar de maneiras diferentes.
    def exibirInformacoes(self):
        print(f''' ------------ 
Informações Do Veículo
------------
Marca: {self.__marca}
Modelo: {self.__modelo}
Ano: {self.__ano}''')


class Carro(Veiculo):    # Herdando os valores da classe mãe
    def __init__(self, marca, modelo, ano, cv):
        super().__init__(marca,modelo,ano)
        self.__cv = cv
    
    @property
    def cv(self):
        return self.__cv
    

    # Reescrevendo o Polimorfismo nas classes filhas
    # Aqui onde irá se comportar diferente dependendo do objeto (Carro ou Moto)

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Cavalos: {self.__cv}\n------------")  


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cc):
        super().__init__(marca,modelo,ano)
        self.__cc = cc
    
    @property
    def cc(self):
        return self.__cc

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Cilindradas: {self.__cc}\n------------")

carro1 = Carro('Chevrolet', 'Astra', 2010, 140)
carro1.exibirInformacoes()

moto1 = Moto('Honda', 'Africa Twin', 2015, 99)
moto1.exibirInformacoes()