import sys
from time import sleep
from gpiostepper import Stepper

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        speed = int(sys.argv[1])
    else:
        speed = 100
    
    print("Speed: {} rpm".format(speed))

    number_of_steps = 32
    
    step_motor3 = Stepper(
        motor_pins=[17, 22, 18, 23], 
        number_of_steps = number_of_steps,
        step_sequence = [[1,0,1,0], [0,1,1,0], [0,1,0,1], [1,0,0,1]]
        )
    step_motor3.set_speed(speed)
    
    # Rotate CCW indefinitely
    print("Counter-clockwise Rotation")
    step_motor3.backward()
