class Veiculo:
    def __init__(self, modelo, ano, marca):
        self.__modelo = modelo.title()
        self.__ano = ano
        self.__marca = marca.title()

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def __str__(self): ## base do polimorfismo, para cada uma das subclasses vai ter essa base
        return f'Modelo: {self.__modelo} -- Ano: {self.__ano} -- Marca: {self.__marca}'
    

class Carro(Veiculo):
    def __init__(self, modelo, ano, marca, cv):
        super().__init__(modelo, ano, marca)
        self.__cv = cv
    
    @property
    def cv(self):
        return self.__cv
    
    @cv.setter
    def cv(self, cv):
        self.__cv = cv

    def __str__(self):
        # Usando os métodos da classe base para acessar atributos
        # Polimorfismo respondendo 'diferente' da base com cv acrescentado
        return f'{super().__str__()} -- CV: {self.__cv}'
    

class Moto(Veiculo):
    def __init__(self, modelo, ano, marca, cc):
        super().__init__(modelo, ano, marca)
        self.__cc = cc
    
    @property
    def cc(self):
        return self.__cc
    
    @cc.setter
    def cc(self, cc):
        self.__cc = cc

    def __str__(self):
        # Usando os métodos da classe base para acessar atributos
        # Polimorfismo respondendo 'diferente' da base com cc acrescentado
        return f'{super().__str__()} -- CC: {self.__cc}'


# Testando as classes
carro1 = Carro('Civic', 2012, 'honda', 150)
moto1 = Moto('XRE', 2012, 'honda', 300)

print(carro1.__str__())
print(moto1.__str__())
