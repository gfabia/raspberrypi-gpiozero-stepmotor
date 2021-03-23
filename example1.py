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

    step_motor1 = Stepper(motor_pins=[17, 18, 22, 23], number_of_steps = number_of_steps)
    step_motor1.set_speed(speed)
    
    amount_of_gear_reduction = 64
    number_of_steps_per_revolution_geared_output = number_of_steps * amount_of_gear_reduction
    
    # Do a full CW rotation
    print("One Full Clockwise Rotation")
    step_motor1.step(number_of_steps_per_revolution_geared_output)
    
    sleep(1)
    
    # Do a half CCW rotation
    print("Half Counter-clockwise Rotation Slowly")
    step_motor1.set_speed(speed/3)
    step_motor1.step(-number_of_steps_per_revolution_geared_output/2)
