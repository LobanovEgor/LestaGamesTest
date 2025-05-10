class Oar:
    def __init__(self, length, weight):
        self.length = length #m
        self.weight = weight #kg
        self.in_water = False
        self.is_turned = False # Если развернуть весло углублением вперёд -> начнётся торможение

    def turn_oar(self):
        self.is_turned = not self.is_turned