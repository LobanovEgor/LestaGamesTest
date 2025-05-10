import pytest
from src.Boat import Boat



def test_flooding(): # Сценарий затопления
    boat = Boat(4)
    # Нормальное состояние
    boat.row()
    assert boat.speed > 0

    # Имитируем попадание воды
    boat.water_level = 0.7

    # Попытка гребли при затоплении
    with pytest.raises(RuntimeError) as e:
        boat.row()
    assert "Мы тонем!" in str(e.value)

    # Проверка остановки
    assert boat.speed == 0

def test_max_speed():
    boat = Boat(1)
    for _ in range(10): #Гребём 10 раз
        boat.row()

    assert boat.speed == 6.0

def test_passengers_speed():
    boat = Boat(4)
    for _ in range(2): # Заполняем пассажирами
        boat.embark()

    boat.row()

    assert boat.speed == 0.5

def test_disembark():
    boat = Boat(4)
    for _ in range(2): # Заполняем пассажирами
        boat.embark()

    boat.water_level = 1
    #Пытаемся грести
    with pytest.raises(RuntimeError) as e:
        boat.row()
    assert "Мы тонем!" in str(e.value)

    for _ in range(3):
        boat.disembark()

    assert boat.speed == 0
    assert boat.passengers == 0

def test_long_exploitation():
    boat = Boat(6)

    for _ in range(99):
        for _ in range(3):
            boat.embark()

        boat.row()
        for _ in range(3):
            boat.disembark()

    assert 0 < boat.speed <= 6
    assert boat.passengers == 1 # должен остаться только гребщик