"""
        Class containts one abstract and one regular method
        - create child class that defines the implementation of parent method
        - create obj that utilizes both parent and child methods
        - comment
"""

   
from abc import ABC, abstractmethod

## Code copied from pg 279 for personal understanding
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
        
class cardPayment(car):
    def payment(self, amount):
        print("Your purchase of {} exceeds your $100 limit.".format(amount))
        
obj = cardPayment()
obj.paySlip("$400")
obj.payment("$350")



##Code example used from outside source for further comprehension
class animal(ABC):
    def move(self):
        print("This animal has legs.")
        pass
    def overWrite(self):
        pass
    
    ##Need an abstract method
    
class horse(animal):
    def legs(self, name):
        print("This {} has 4 legs.".format(name))
    def overWrite(self):
        print("Overwriting the parent method.")
        
    ##need to overwrite the abstract method with implementation of method
        


x = horse()
x.legs('horse')
x.move()
x.overWrite()

y = animal()
y.move()
y.overWrite()


