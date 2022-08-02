from models.cliente import Cliente
from models.conta import Conta
from time import sleep
from typing import List

contas: List[Conta] = []

def main() -> None:
    return menu()

def menu() -> None:
    print('=====================================')
    print('============== ATM ==================')
    print('=========== Geek Bank ===============')
    print('=====================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()

def criar_conta() -> None:
    print(f'Me informe o Cliente para ser criada a conta no banco: ')
    nome: str = input('Nome: ')
    email: str = input('Email: ')
    cpf: str = input('CPF: ')
    data: str = input('Data de Nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data)

    conta: Conta = Conta(cliente)

    contas.append(conta)
    
    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('----------------')
    print(conta)
    sleep(1)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        num = int(input('Informa o número da conta para ser efetuado o saque: '))

        conta: Conta = buscar_conta(num)

        if conta:
            print(f'Me informe o valor do saque.')
            n: float = float(input())

            conta.sacar(n)
            
        else:
            print('Número de conta inválido')
            print('------------------------')
    else:
        print('Ainda nenhuma conta cadastrada ainda no Banco.')
        print('----------------------------------------------')
    sleep(1)
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        num = int(input('Informa o número da conta para ser efetuado o deposito: '))

        conta: Conta = buscar_conta(num)

        if conta:
            print(f'Me informe o valor do deposito.')
            n: float = float(input())

            conta.depositar(n)
        else:
            print('Número de conta inválido')
            print('------------------------')
    else:
        print('Ainda nenhuma conta cadastrada ainda no Banco.')
        print('----------------------------------------------')
    sleep(1)
    menu()

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        n1: float = float(input(('Informe o número da conta a ser retirado o valor: ')))
        conta1: Conta = buscar_conta(n1)
        
        if conta1:
            n2: float = float(input(('Informe o número da conta a ser transferido o valor: ')))
            conta2: Conta = buscar_conta(n2)
            
            if conta2:
                valor: float = float(input('Informe o valor a ser transferido: '))
                conta1.tranferir(conta2, valor)
            
            else:
                print(f'A conta de número {n2} não foi encontrada')
                print('------------------------------------------')

        else:
            print(f'A contade de número {n1} não foi encontrada')
            print('--------------------------------------------')


    else:
        print('Não existe nenhuma conta cadastrada no Banco.')
        print('---------------------------------------------')
    sleep(1)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de Contas: ')
        
        for conta in contas:
            print('---------------------')
            print(conta)
            print('---------------------')
            sleep(1)
    
    else:
        print('Não existe nenhuma conta cadastrada no Banco.')
        print('---------------------------------------------')
    sleep(1)
    menu()

def buscar_conta(valor: int) -> Conta:
    conta: Conta = None
    for cont in contas:
        if valor == cont.conta:
            conta = cont
            
    return conta

if __name__ == '__main__':
    main()