class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}"
        elif wheels == 3:
            return f"Это трицикл марки {self.name}"
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}"
        else:
            return f"Я не знаю таких ТС марки {self.name}"

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо {self.name} можно брать."
        elif 50001 <= self.mileage <= 100000:
            return f"{self.name} надо внимательно проверить."
        elif 100001 <= self.mileage <= 150000:
            return f"{self.name} надо провести полную диагностику."
        else:
            return f"{self.name} лучше не покупать."


vehicles_by_wheels = {
    2: [Vehicle("BMW", 40000)],
    4: [Vehicle("Mercedes", 90000), Vehicle("Ford", 250000)],
    5: [Vehicle("Toyota", 200000)],
    3: [Vehicle("Audi", 140000)],

}

for wheels, vehicles in vehicles_by_wheels.items():
    for vehicle in vehicles:
        print(vehicle.get_vehicle_type(wheels))
        print(vehicle.get_vehicle_advice())
