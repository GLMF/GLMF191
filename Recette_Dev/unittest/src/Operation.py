class Operation:

    def __init__(self, valueA, valueB):
        self.__a = valueA
        self.__b = valueB

    def add(self):
        return self.__a + self.__b

    def div(self):
        return self.__a / self.__b

if __name__ == '__main__':
    op = Operation(4, 2)
    print('Valeurs : 4 et 2')
    print('Addition :', op.add())
    print('Division :', op.div())
