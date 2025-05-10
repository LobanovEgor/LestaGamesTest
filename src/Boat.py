from src.Oar import Oar


class Boat:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.passengers = 0
        self.speed = 0.0
        self.direction = 0.0
        self.sinking = False
        self.oars = {
            "left": Oar(2.5, 'wood'),
            "right": Oar(2.5, 'wood')
        }
