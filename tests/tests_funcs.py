import pytest
from src.Boat import *


@pytest.fixture(autouse=True) # Создаём объект лодки, чтобы каждый раз не создавать новый
def test_boat():
    return Boat(2)

def test_embark(test_boat):
    boat = test_boat
    boat.embark()
    assert boat.passengers == 2

def test_disembark(test_boat):
    boat = test_boat
    boat.disembark()
    assert boat.passengers == 0

def test_turning_oar(test_boat):
    oar = Oar(2.5, 2)
    oar.turn_oar()

    assert oar.is_turned == True

def test_row(test_boat):
    boat = test_boat
    init_speed = boat.speed
    boat.row()

    assert init_speed < boat.speed

def test_slowdown(test_boat):
    boat = test_boat

    boat.row()
    normal_speed = boat.speed

    boat.oars['left'].turn_oar()
    boat.row()

    assert normal_speed > boat.speed