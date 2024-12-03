# Идея такая, есть автобусный маршрут состоящий из 20 остановок поездка стоит 20 рублей, с каждой 5 остановкой
# цена увеличивается на 5 рублей. Если едет ребенок проезд для него бесплатный, если пенсионер у него скидка 50%
# на поездку. Обычный взрослый платит всю стоимость маршрута.

class BusRoute:
    def __init__(self, stops=20, base_fare=20):
        self.stops = stops
        self.base_fare = base_fare

    def calculate_fare(self, stop):
        fare = self.base_fare + stop // 5 * 5
        return fare

    def calculate_discounted_fare(self, stop, passenger_type):
        base_fare = self.calculate_fare(stop)
        if passenger_type == "ребенок":
            return 0
        elif passenger_type == "пенсионер":
            return base_fare * 0.5
        else:
            return base_fare


class Passenger:
    def __init__(self, name, passenger_type):
        self.name = name
        self.passenger_type = passenger_type

    def get_fare(self, bus_route, stop):
        fare = bus_route.calculate_discounted_fare(stop, self.passenger_type)
        print(f"{self.name} {self.passenger_type} заплатит {fare} рублей за проезд {stop} остановок.")


bus = BusRoute()

passenger1 = Passenger("Иван", "взрослый")
passenger2 = Passenger("Алена", "ребенок")
passenger3 = Passenger("Виктор", "пенсионер")

passenger1.get_fare(bus, 18)
passenger2.get_fare(bus, 8)
passenger3.get_fare(bus, 15)
