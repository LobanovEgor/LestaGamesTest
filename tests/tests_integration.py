import pytest
from src.Boat import *


def test_turn_oar_integration():
    boat = Boat(1)

    boat.row()
    assert boat.speed == 1
    boat.oars['left'].is_turned = True # Разворачиваем одно весло

    boat.row()
    assert boat.speed == 0

def test_turn_our_long():
    boat = Boat(1)

    boat.oars['left'].is_turned = True
    boat.oars['right'].is_turned = True

    for _ in range(2):
        boat.row()

    assert boat.oars['left'].is_turned == True
    assert boat.oars['right'].is_turned == True