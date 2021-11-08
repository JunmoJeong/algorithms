class Car1:
    model="SM3"
    price=2000

    def sale(self,price):
        self.price=self.price-price
    
new_car1= Car1()
new_car1.price=1500
print(new_car1.price)

new_car1.sale(200)
print(new_car1.model, new_car1.price)


class Car1_1:

    def __init__(self):
        self.model="SM5"
        self.price=3000
        
    def sale(self,price):
        self.price=self.price-price
    
new_car1_1= Car1_1()
new_car1_1.sale(200)
print(new_car1_1.model, new_car1_1.price)



class Car2:

    def __init__(self, model, price):
        self.model=model
        self.price=price
        
    def sale(self,price):
        self.price=self.price-price

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price


new_car2= Car2("Sonata", 2500 )
new_car2.sale(200)
print(new_car2.get_model(), new_car2.get_price())
# print(new_car2.model) 

'''
class Car:


    def
    '''
