#상속
class Dad:
       def sing(self):
              print("노래를 잘 한다")
        
class Child(Dad):
       def dance(self):
              print("춤을 잘 춘다")
      
c=Child()
c.sing()
c.dance()


#다중 상속
class Dad:
       def sing(self):
           print("노래를 잘 한다")

class Mom:
       def math(self):
           print("수학을  잘 한다")
        
class Child(Dad,Mom):
    def dance(self):
        print("춤을 잘 춘다")
      
c=Child()
c.sing()
c.math()
c.dance()

#메소드 오버라이딩
class Dad:     
     def sing(self):
           print("노래를 잘 한다")
        
class Child(Dad):
    def sing(self):
        super().sing()
        print("랩을 잘 한다.")
      
c=Child()
c.sing()



