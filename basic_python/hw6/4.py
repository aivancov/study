class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'[INFO] {self.name}: GO GO GO !!!')

    def stop(self):
        print(f'[INFO] {self.name}: STOP!')

    def turn(self, direction):
        print(f'[INFO] {self.name}: turn {direction}')

    def show_speed(self):
        print(f'[INFO] {self.name}: current speed {self.speed} km/h.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'[INFO] {self.name}: Speed limit exceeded! Current speed {self.speed} km/h')
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'[INFO] {self.name}: Speed limit exceeded! Current speed {self.speed} km/h')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.is_police = True



general_car = Car(70, 'red', 'Toyota Corolla', False)
town_car = TownCar(80, 'green', 'Nissan Almera', False)
sport_car = SportCar(160, 'grey', 'Subaru Impreza', False)
work_car = WorkCar(50, 'blue', 'Lada Vesta', False)
police_car = PoliceCar(130, 'white', 'Ford Focus')

car_list = [general_car, town_car, sport_car, work_car, police_car]
for car in car_list:
    print('====================================')
    print('Attributes:')
    print(f'{car.name}, {car.color}, Is police: {car.is_police}')
    print('------------------------------------')
    car.go()
    car.turn('left')
    car.turn('right')
    car.show_speed()
    car.stop()
