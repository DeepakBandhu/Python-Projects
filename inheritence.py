class Car:
    wheels = 4
    brakes = True
    propellers = 0
    brand = 'N/A'
#using (Car) gives the child class the parent attributes
class Mustang(Car):
    brand = 'Ford'
    color = 'red'

class Pinto(Car):
    design = 'bad'
    model = '1776'
