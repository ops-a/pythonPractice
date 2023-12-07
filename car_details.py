# model, regno
# Three ways to do it

# FIRST
class Car:
    def __init__(self, model, regno):
        self.model = model
        self.regno = regno

# SECOND
class Car:
    def setCarValues(self, model, regno):
        self.model = model
        self.regno = regno

    def getModel(self):
        print(self.model)
        return self.model


    def setCarValues(self, model, regno):
        self.model = model
        self.regno = regno

    def getModel(self):
        print(self.model)
        return self.model


car1 = Car()
car1.setCarValues("abc", "1234")
# car1.setCarValues("abc", "1234")

print('Car 1 details: ', car1.model, car1.regno)
