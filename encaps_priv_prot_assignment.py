""" Create a class
    Use private attrib/function
    Use protected attrib/function
    Create obj that utilises both private and protected
    Comment
"""
#defining Protected as a class
class Protected:
    def __init__(self):
        #setting initial values for both protected and private var
        self._protVar = 0
        self.__privVar = 12
        
    def getPrivate(self):
        #basic function to print protected var value
        print(self.__privVar)
        
    def setPrivate(self, private):
        #basic function to change protected variable's value
        self.__privVar = private
        
        
x = Protected()
print(x._protVar)
x._protVar = 234
print(x._protVar)

y = Protected()
y.getPrivate()
y.setPrivate(23)
y.getPrivate()
