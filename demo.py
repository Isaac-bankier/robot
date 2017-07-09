#Just a simple file to test out the powers of the motors
from math import *

def motor_strength(Vlinear, direction, Vangular, wheel):
    wheels = [0.0, 120.0, 240.0]
    wheelAngle = wheels[wheel]
    Vrx = Vlinear * cos(direction)
    Vry = Vlinear * sin(direction)
    Vwx = Vrx * cos(wheelAngle)
    Vwy = Vry * - sin(wheelAngle)
    Vw = Vlinear * (cos(direction) * cos(wheelAngle) - sin(direction) * sin(wheelAngle)) + Vangular
    return Vw
test_data = [[1, 0 ,0], [1000, 0 ,0], [5, 0 ,0], [5, 180 ,0], [5, 90 ,0], [5, 270 ,90]]

for test in test_data:
    print("\n\n\n-------------------------------")
    print("Linear speed   :    "+str(test[0]))
    print("Direction      :    "+str(test[1]))
    print("Angular speed  :    "+str(test[2]))
    print("Motor 1 power  :    "+str(motor_strength(test[0], test[1], test[2], 0)))
    print("Motor 2 power  :    "+str(motor_strength(test[0], test[1], test[2], 1)))
    print("Motor 3 power  :    "+str(motor_strength(test[0], test[1], test[2], 2)))
