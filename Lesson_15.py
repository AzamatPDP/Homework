class Avto:
    def __init__(self, model, color, karobka, price):
        self.model = model
        self.color = color
        self.karobka = karobka
        self.price = price
        self.kilometr = 0

    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def get_karobka(self):
        return self.karobka
    def get_price(self):
        return self.price
    def get_info(self):
        return f"Car model {self.model}, color {self.color}, engine box {self.karobka}, kilometr:{self.kilometr} and price {self.price}$"
    def update_km(self,km):
        self.kilometr += km
    def update_model(self,newModel,price):
        self.model = newModel
        self.price = price
avto = Avto("BMW X7","black","automatic", 120_000)
print(avto.get_model())
print(avto.get_info())
avto.update_km(40)
avto.update_km(50)
print(avto.get_info())
avto.update_model('BMW X6 NEW',125_000)
print(avto.get_info())


class Avtosalon:
    def __init__(self, car_showroom, adress):
        self.car_showroom = car_showroom
        self.adress = adress
        self.cars = []
        self.carsCount = 0

    def add_car(self, car):
        self.cars.append(car)
        self.carsCount += 1
    def get_carCount(self):
        pass
    def cars_info(self):
        return [car.get_info() for car in self.cars]

liderCarSalon = Avtosalon("Lider group", "Xorazm, Urgench")
avto1 = Avto("BMW X7","black","automatic", 120_000)
avto2 = Avto("BMW X6","green","automatic", 110_000)
avto3 = Avto("BMW X5","white","automatic", 100_000)
liderCarSalon.add_car(avto1)
liderCarSalon.add_car(avto2)
liderCarSalon.add_car(avto3)
print(f"Avtosalondagi mashinalar soni: {liderCarSalon.carsCount}")
print(liderCarSalon.cars_info())



