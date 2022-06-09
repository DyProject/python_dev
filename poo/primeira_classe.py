class CountFromBy():
        def __init__(self, valor_inicial: int = 0, incremento: int = 1) -> None:
                self.__valor_inicial = valor_inicial
                self.__valor_atual = valor_inicial
                self.__incremento = incremento

        def __repr__(self) -> str:
                return ("Valor Inicial: " + str(self.__valor_inicial) + ", Valor Atual: " + str(self.__valor_atual) + ", Incremento: " + str(self.__incremento))
                
        def increase(self) -> None:
                self.__valor_atual += self.__incremento

        def decrease(self) -> None:
                self.__valor_atual -= self.__incremento

        def reset(self) -> None:
                self.__valor_atual = self.__valor_inicial

        
	

c = CountFromBy(valor_inicial = 10, incremento = 1)
c.increase()
print("---Print c")
print(c)

print("---Print d")
d = CountFromBy()
d.increase()
d.increase()
print(d)

print("---Print e")
d = CountFromBy(incremento = 15)
d.increase()
d.increase()
print(d)


