from src.Oar import Oar


class Boat:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.speed = 0.0
        self.passengers = 1 # Одно место занимает тот кто гребёт

        #Высчитываем ускорение с помощью пассажиров, больше вместимость -> больше начальное ускорение
        self.speed_increment = 1 # чем меньше пассажиров тем больше будет скорость
        self.sinking = False
        self.water_level = 0.0
        self.oars = {
            "left": Oar(2.5, 2),
            "right": Oar(2.5, 2)
        }

    def row(self):
        if self.check_sinking():
            self.speed = 0
            raise RuntimeError('Мы тонем!')


        #Погружаем оба весла в воду
        self.oars['left'].in_water = True
        self.oars['right'].in_water = True


        if not self.oars['left'].is_turned and not self.oars['right'].is_turned:
            if self.speed <= 6: #Не даём превысить среднюю скорость весельной лодки
                self.speed += self.speed_increment # Добавляем скорости
            else:
                self.speed = 6
        else: # Если вёсла развёрнуты, то скорость будет снижаться
            if self.speed >= 0: # Не даём уйти в отрицательную скорость
                self.speed -= self.speed_increment
            else:
                self.speed = 0

        self.oars['left'].in_water = False
        self.oars['right'].in_water = False

    def embark(self):
        if self.passengers + 1 <= self.capacity:
            self.passengers += 1
            self.speed_increment -= self.passengers / 10
        else:
            raise ValueError('Места кончились!')

    def disembark(self):
        if self.passengers - 1 >= 0:
            self.passengers -= 1
            self.speed_increment += 1 - self.passengers / 10
        else:
            raise ValueError('Количество пассажиров не может быть меньше нуля!')

    def check_sinking(self):
        if self.water_level > 0.5:
            return True
        return False

