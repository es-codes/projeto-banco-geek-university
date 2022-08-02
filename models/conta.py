from cliente import Cliente
from utils.helper import float_to_string

class Conta:
    
    numero_conta = 1001
    
    def __init__(self: object, cliente: Cliente) -> None:
        self.__cliente: Cliente = cliente
        self.__conta: int = Conta.numero_conta
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self.calcula_saldo_total
        Conta.numero_conta += 1

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def conta(self: object) -> int:
        return self.__conta

    @property
    def saldo(self: object) -> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor
    
    @property
    def calcula_saldo_total(self: object) -> float:
        return self.limite + self.saldo

    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
            print('Saque realizado com sucesso')
        else:
            print('Saque não realizado. Saldo insuficiente.')

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self.calcula_saldo_total
            print('Deposito realizado com sucesso.')
        else:
            print('Deposito não realizado. Valor insuficiente.')


    def tranferir(self: object, destino: object, valor: float) -> None:
        if valor > 0 and valor <= self.saldo_total:
            if valor <= self.saldo_total:
                if valor <= self.saldo:
                    self.saldo = self.saldo - valor
                    destino.saldo = destino.saldo + valor
                    destino.saldo_total = destino.calcula_saldo_total
                    self.saldo_total = self.calcula_saldo_total
                else:
                    restante: float = self.saldo - valor
                    self.limite = self.limite + restante
                    self.saldo = 0
                    destino.saldo = destino.saldo + valor
                    destino.saldo_total = destino.calcula_saldo_total
                    self.saldo_total = self.calcula_saldo_total
                print('Transferência realizada com sucesso')
                print('-----------------------------------')

        else:
            print('Tranferência não realizada. Saldo insuficiente.')

    def __str__(self: object) -> None:
        return f'Cliente: {self.cliente.name} \nConta: {self.conta} \nSaldo Total: {float_to_string(self.saldo_total)}'
