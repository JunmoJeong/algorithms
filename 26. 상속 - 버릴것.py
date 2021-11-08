class Car:
       def move(self):
           print("바퀴로 움직인다")
        

class Truck(Car):
    def load(self):
        print("짐을 싣고 달린다")


        
t=Truck()
t.move()
t.load()


class CampCar(Truck):
    def sleep(self):
        print("잘 수 있다")

cc=CampCar()
cc.move()
cc.load()
cc.sleep()


#------------
class Car:
       def move(self):
           print("바퀴로 움직인다")
        
class Truck():
    def load(self):
        print("짐을 싣고 달린다")
 
class CampCar(Car, Truck):
    def sleep(self):
        print("잘 수 있다")

cc=CampCar()
cc.move()
cc.load()
cc.sleep()
