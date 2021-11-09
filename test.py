from abc import *


class DeliveryStore(metaclass=ABCMeta):
    @abstractmethod
    def set_order_list(self, order_list):
        pass

    @abstractmethod
    def get_total_price(self):
        pass


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 밑에 괄호 안에 DeliveryStore가 들어가야 함


class PizzaStore(DeliveryStore):
    def __init__(self):
        menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
        menu_prices = [11100, 12600, 13300, 21000, 19500]
        self.menu_lsit = []
        for i in range(5):
            self.menu_list.append(Food(menu_names[i], menu_prices[i]))

        self.order_list = []

    # 함수 이름이 set_order_list
    def set_order_list(self, order_list):
        for order in order_list:
            self.order_list.append(order)

    def get_total_price(self):
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_lsit:
                if order == menu.name:
                    total_price += menu.price
        return total_price


def solution(order_list):
    delivery_store = PizzaStore()
    delivery_store.set_order_list(order_list)

    total_price = delivery_store.get_total_price()
    return total_price


order_list = ["Cheese", "Pineapple", "meatball"]
ret = solution(order_list)


print("Solution: return value of the function is", ret, ".")
