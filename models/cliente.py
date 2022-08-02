from datetime import date
from utils.helper import date_to_string,string_to_date

class Cliente:
    
    numero_da_conta: int = 1
    
    def __init__(self: object, name: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__conta: int = Cliente.numero_da_conta
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = string_to_date(data_nascimento)
        self.__data_criacao = date.today()
        Cliente.numero_da_conta += 1

    @property
    def conta(self: object) -> int:
        return self.__conta
    
    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return date_to_string(self.__data_nascimento)
    
    @property
    def data_criacao(self: object) -> str:
        return date_to_string(self.__data_criacao)

    def __str__(self: object) -> None:
        return f'Name: {self.name} \nConta: {self.conta} \nEmail: {self.email} \nCPF: {self.cpf} \nData de Criação: {self.data_criacao}'

    

