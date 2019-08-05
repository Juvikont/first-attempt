class Things:
    pass


class Animate(Things):
    def animal(self):
        print('Я животное')
    def hungry(self):
        print('Я голодный')



class Dog(Animate):
    def action(self):
        self.animal()
        self.hungry()
        print('Я гавкаю')



class Cat(Animate):
    def action(self):
        self.animal()
        self.hungry()
        print('Я мяукаю')


leopold = Cat()
reginald = Dog()


reginald.action()
reginald.action()