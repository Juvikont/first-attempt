print('Welcome to Autohouse!')


class Auto(object):

    def __init__(self, body, color, transmission, engine, capacity, year):
        self.color = color
        self.transmission = transmission
        self.engine = engine
        self.type = body
        self.year = year
        self.capacity = capacity


class Car(Auto):
    def __init__(self):
        self.tittle = None
        self.model = None
        self.make = None

    def __init__(self, make, model, tittle):
        self.make = make
        self.model = model
        self.tittle = tittle

    def info(self):
        print(self.make, self.model, self.tittle, self.type, self.color, self.transmission, self.engine, self.year,
              self.capacity)


def output(cars):
    for cars in cars:
        cars.info()


def search_car(cars):
    model = input('Please provide model: ')
    for car in cars:
        if car.model.lower() == model.lower():
            car.info()


def delete_car(cars):
    model = input('Please provide model: ')
    for car in cars:
        if car.model.lower() == model.lower():
            cars.remove(car)
            return cars


def add_car():
    make = input('Make: ')
    model = input('Model: ')
    tittle = input('Tittle:')
    car = Car(make, model, tittle)
    car.type = input('Type: ')
    car.color = input('Color: ')
    car.transmission = input('Transmission: ')
    car.engine = input('Engine: ')
    car.capacity = input('Capacity: ')
    car.year = input('Year: ')
    return car


Accord = Car(make='Honda', model='Accord', tittle="Salvage")
Accord.type = 'Sedan'
Accord.color = 'Red'
Accord.transmission = 'Automatic'
Accord.capacity = '3.0'
Accord.engine = 'Gas'
Accord.year = '2018'

Passat = Car(make='Volkswagen', model='Passat', tittle='Clean')
Passat.type = 'Sedan'
Passat.color = 'Brown'
Passat.transmission = 'Manual'
Passat.capacity = '2.0'
Passat.engine = 'Diesel'
Passat.year = '2012'

Golf = Car(make='Volkswagen', model='Golf', tittle='Clean')
Golf.type = 'Hatchback'
Golf.color = 'Grey'
Golf.transmission = 'Manual'
Golf.capacity = '2.5'
Golf.engine = 'Diesel'
Golf.year = '2012'

Mustang = Car(make='Ford', model='Mustang', tittle="Salvage")
Mustang.type = 'Sport-Coupe'
Mustang.color = 'Blue'
Mustang.transmission = 'Automatic'
Mustang.capacity = '5.6'
Mustang.engine = 'Gas'
Mustang.year = '2018'

x = [Accord, Passat, Golf, Mustang]

while True:
    print('Menu: ')
    print('1. Show auto\'s: ')
    print('2. Vehicle finder: ')
    print('3. Add car: ')
    print('4. Delete car: ')
    choice = input("What you want to do?: ")
    if choice == '1':
        output(x)
    elif choice == '2':
        search_car(x)
    elif choice == '3':
        x.append(add_car())
    elif choice == '4':
        delete_car(x)


# for i in x:
#     if i.make == 'Volkswagen':
#         i.info()

# for i in x:
#     a = str(input())
#     if a == 'Delete Golf':
#         x.remove(Golf)
#     elif a == 'Delete Passat':
#         x. remove(Passat)
#     elif a == 'Delete Mustang':
#         x. remove(Mustang)
#     for i in x:
#         i.info()
