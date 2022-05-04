from MotorModule import Motor
import keyPressModule as kp

##########################################
##########################################
# THIS IS THE CLASS FROM THE MotorModule
##########################################
##########################################

in1 = 24
in2 = 23
in3 = 17
in4 = 27

motor = Motor(in1, in2, in3, in4)


##########################################
##########################################
# THIS IS THE CLASS FROM THE keyPress
##########################################
##########################################
def main():
    if(kp.getKey('UP')):
        motor.moveForward()
    elif(kp.getKey('DOWN')):
        motor.moveBackward()
    elif(kp.getKey('LEFT')):
        motor.moveLeft()
    elif(kp.getKey('RIGHT')):
        motor.moveRight()
    else:
        motor.stop()
    
kp.init()

if __name__ == '__main__':
    while True:
        main()
