class Calculator:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    def add(self)->int:
        return self.number1+self.number2
    