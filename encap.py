class Bird:

    def __init__(self):
        self.__liftOff()

    def fly(self):
        print('flying')

    def __liftOff(self):
        print('The bird is')

bluebird = Bird()
bluebird.fly()
