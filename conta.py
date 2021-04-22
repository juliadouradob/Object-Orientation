
class Conta:
    #funcão construtora
    #coloando __ na frente da variável, voce transforma ela em private
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #region GET
    #monstrando 2 jeitos de fazer, sendo o segundo setando como property
    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular.title()

    def get_numero(self):
        return self.__numero

    #endregion

    # region SET
    # monstrando 2 jeitos de fazer, sendo o segundo setando como property
    def set_limite(self, valor):
        self.__limite = valor

    @titular.setter
    def titular(self, nome):
        self.__titular = nome

    # endregion

    def __validar_saque(self, valor):
        return self.__saldo < valor

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if (self.__validar_saque(valor)):
            print("Voce não possui saldo suficiente.")
        else:
            self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
