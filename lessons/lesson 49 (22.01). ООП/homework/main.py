from abc import ABC, abstractmethod

class DiscountPolicy(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply(self, price: float):
        pass

    def clamp_price(self, price: float):
        if price < 0:
            return 0
        else:
            return price


class PercentDiscount(DiscountPolicy):
    def __init__(self, name, percent):
        super.__init__(name)
        self.percent = percent

    def apply(self, price: float):
        price = super().clamp_price(price)
        return price * (1 - self.percent / 100)


class FixedDiscount(DiscountPolicy):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

    def apply(self, price: float):
        price = super().clamp_price(price)
        new_price = price - self.amount
        return super().clamp_price(new_price)


class MinPriceDiscount(DiscountPolicy):
    def __init__(self, name, min_price, percent):
        super().__init__(name)
        self.min_price = min_price
        self.percent = percent

    def apply(self, price):
        price = super().clamp_price(price)
        if price < self.min_price:
            return price
        else:
            return price * (1 - self.percent / 100)


class PriceCalculator:
    def __init__(self, policies: list[DiscountPolicy]):
        self.policies = policies

    def calculate(self,price: float):
        pass


fix_discount = FixedDiscount('1000', 1000)
perc_discount = PercentDiscount('20%', 20)
price_1 = 20000
price_2 = 3000
price_3 = 0
itog1 = calculate(price_1)
itog2 = calculate(price_2)
itog3 = calculate(price_3)