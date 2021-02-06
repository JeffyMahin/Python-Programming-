class Computer:
    def __init__(self):
        self.__maxprice = 9000

    def sell(self):
        print("Price is {}" .format(self.__maxprice))

    def max_price(self, price):
        self.__maxprice = price


obj = Computer()
obj.sell()

obj.__maxprice = 2000
obj.sell()


obj.max_price(2000)
obj.sell()