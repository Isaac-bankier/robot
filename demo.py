#Just a simple file to test out the powers of the motors
from math import *

def motor_strength(Vlinear, direction, Vangular, wheel):
    wheels = [0, 120, 240] #Placement of each wheel
    wheelAngle = wheels[wheel] #The angle of the target wheel
    Vrx = Vlinear * cos(direction) #The X movement of the robot
    Vry = Vlinear * sin(direction) #The Y movement of the robot
    Vwx = Vrx * cos(wheelAngle) #The X movement of the wheel
    Vwy = Vry * - sin(wheelAngle) #The Y movement of the wheel
    Vw = Vlinear * (cos(direction) * cos(wheelAngle) - sin(direction) * sin(wheelAngle)) + Vangular #The combined strength for the wheel
    return Vw 

test_data = [[1.0, 0.0, 0.0], [1000.0, 0.0, 0.0], [5.0, 0.0, 0.0], [5.0, 180.0, 0.0], [5.0, 90.0, 0.0], [5.0, 270.0, 90.0]]

for test in test_data:
    print("\n\n\n-------------------------------")
    print("Linear speed   :    "+str(test[0]))
    print("Direction      :    "+str(test[1]))
    print("Angular speed  :    "+str(test[2]))
    print("Motor 1 power  :    "+str(motor_strength(test[0], test[1], test[2], 0)))
    print("Motor 2 power  :    "+str(motor_strength(test[0], test[1], test[2], 1)))
    print("Motor 3 power  :    "+str(motor_strength(test[0], test[1], test[2], 2)))
