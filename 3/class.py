class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        print(result)
    def minus(self):
        result = self.num1 - self.num2
        print(result)

    def multiply(self):
        result = self.num1 * self.num2
        print(result)

    def divide(self):
        result = self.num1 / self.num2
        print(result)

cal1=Calculator(1,2)
cal1.add()

cal2=Calculator(2,3)
cal2.add()
cal1.add()
cal1.minus()
cal1.multiply()
cal1.divide()