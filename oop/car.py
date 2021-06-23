from vehicle import Vehicle

class Car(Vehicle):
    def brag(self):
        print('Look at how cool my car is.')

car1 = Car()
car1.drive()

car1.add_warnings('Hello')

print(car1)

car2 = Car(200)
car2.drive()
print(car2.get_warnings())

car3 = Car(300)
car3.drive()
print(car3.get_warnings())