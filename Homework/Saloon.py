from datetime import date as d

print('Welcome to Saloon!')


class Journal(object):
    def __init__(self, date, name, service, cash):
        self.service = service
        self.date = date
        self.name = name
        self.cash = cash

    def info(self):
        print(self.name, self.date, self.service, self.cash)


class Services(object):

    def __init__(self, sex, service, price, name):
        self.sex = sex
        self.service = service
        self.price = price
        self.name = name

    def info(self):
        print(self.sex, self.service, self.price, self.name)


def add_journal():
    name = input('Your name: ')
    service = input('Type of service: ')
    cash = input('Amount: ')
    date = d.today()
    customer = Journal(name, service, date, cash)
    customer.info()
    return customer


def output(services):
    for services in services:
        services.info()


def money(incomes):
    _sum = 0
    for income in incomes:
        _sum = income.cash
        return _sum


def search_service(services):
    service = input('Please provide the service you want to find: ')
    for __type in services:
        if __type.service.lower() == service.lower():
            __type.info()


def add_service():
    sex = input('Gender: ')
    service = input('Type of the service: ')
    name = input('Name of the service: ')
    price = input('Price: ')
    value = Services(sex, service, name, price)
    return value


def money(incomes):
    _sum = 0
    for income in incomes:
        int(income.cash)
        _sum = sum(income.cash)
    return _sum


Box_Haircut = Services(sex='Men\'s', service='Haircut', name='"Box"', price='50$')
Half_Box_Haircut = Services(sex='Men\'s', service='Haircut', name='"Half-Box"', price='45$')
Natural_Coloring = Services(sex='Female\'s', name='"Natural"', service='Coloring', price='75$')
Blond_Coloring = Services(sex='Female\'s', name='"Blond"', service='Coloring', price='30$')
Strong_Bob = Services(sex='Female\'s', service='Haircut', name='"Strong-Bob"', price='70$')
Honolulu = Services(sex='Female\'s', service='Haircut', name='"Honolulu"', price='60$')
Classic_Massage_30_minutes = Services(sex='Body', service='Massage', name='30 Minutes', price='30$')
Classic_Massage_60_minutes = Services(sex='Body', service='Massage', name='60 Minutes', price='55$')

Service_Names = [Box_Haircut, Half_Box_Haircut, Natural_Coloring, Blond_Coloring, Strong_Bob, Honolulu,
                 Classic_Massage_30_minutes, Classic_Massage_60_minutes]

Customers = []

while True:
    print('Our service\'s ')
    print('1. Men\'s Haircut\'s ')
    print('2. Women\'s Haircut\'s ')
    print('3. Coloring ')
    print('4. Massage ')
    print('5. Search service')
    print('6. Add the service')
    print('7. Add customer  ')
    print('8. Customers book')
    print('9. End of the day')
    choice = input("What you want to do?: ")
    if choice == '1':
        print('1.1 Box Haircut')
        Box_Haircut.info()
        print('1.1 Half-Box Haircut')
        Half_Box_Haircut.info()
    if choice == '2':
        print('2.1 Strong Bob')
        Strong_Bob.info()
        print('2.2 Honolulu')
        Honolulu.info()
    if choice == '3':
        print('3.1 Natural Coloring')
        Natural_Coloring.info()
        print('3.2 Blond Coloring')
        Blond_Coloring.info()
    if choice == '4':
        print('4.1 30min Massage')
        Classic_Massage_30_minutes.info()
        print('4.2 60min Massage')
        Classic_Massage_60_minutes.info()
    if choice == '5':
        search_service(Service_Names)
    if choice == '6':
        Service_Names.append(add_service())
    if choice == '7':
        Customers.append(add_journal())
    if choice == '8':
        output(Customers)
    if choice == '9':
        money(Customers)
