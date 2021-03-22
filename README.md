# RaspberryPi Stepper Motor

This implements a `Stepper` class currently missing in [**gpiozero**](https://gpiozero.readthedocs.io/en/stable/)'s API [4].
This code is somewhat an adaptation of Arduino's built-in Stepper class [1,2].

Tested and works on unipolar stepper motor **28BYJ-48** with **UL2003AN** driver. However, during tests, higher rpm settings (>1600) caused motor to intermittently stop. Motor seem to work fine however with about 1500 rpm, or about 1.25ms delay.

## Usage
**Example 1**: Setting rotation speed and doing full or half turn

```python
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
```

**Example 2**: Setting step sequence and rotating indefinitely

```python
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
    
    step_motor2 = Stepper(
        motor_pins=[17, 22, 18, 23], 
        number_of_steps = number_of_steps,
        step_sequence = [[1,0,1,0], [0,1,1,0], [0,1,0,1], [1,0,0,1]]
        )
    step_motor2.set_speed(speed)
    
    # Rotate CW indefinitely
    print("Clockwise Rotation")
    step_motor2.forward()
```
*Important!* With the step sequence similar to [2], you need to specify the output pins in 1-3-2-4 sequence. This video [3] explains why it's so: https://youtu.be/0qwrnUeSpYQ?t=1068

## References

1. **Stepper Library.** https://www.arduino.cc/en/Reference/Stepper
2. **Stepper.cpp.** https://github.com/arduino-libraries/Stepper/blob/master/src/Stepper.cpp
3. **Stepper Motors with Arduino - Controlling Bipolar & Unipolar stepper motors.** https://www.youtube.com/watch?v=0qwrnUeSpYQ
4. **Add Stepper Motor.** https://github.com/gpiozero/gpiozero/issues/144



