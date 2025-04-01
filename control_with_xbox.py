from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.iodevices import XboxController
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.tools import wait

hub = PrimeHub()
motor_A = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_B = Motor(Port.B, Direction.CLOCKWISE)
motor_C = Motor(Port.C, Direction.CLOCKWISE)
motor_D = Motor(Port.D, Direction.CLOCKWISE)

controller = XboxController()

# תקרת מהירות
MAX_SPEED = 1050
speed_factor = MAX_SPEED / 10 # 100% speed == MAX_SPEED

while True:
    pressed_buttons = controller.buttons.pressed()
    x, y = controller.joystick_left()
    lt, rt = controller.triggers()

    lt_pressed = lt > 0
    rt_pressed = rt > 0
    rb_pressed = Button.RB in pressed_buttons
    lb_pressed = Button.LB in pressed_buttons

    right = y - x / 3
    left = y + x / 3

    motor_A.run(left * speed_factor)
    motor_B.run(right * speed_factor)

    # Motor D
    if lt_pressed:
        motor_D.run(MAX_SPEED)
    elif lb_pressed:
        motor_D.run(-MAX_SPEED)
    else:
        motor_D.stop()

    # Motor C
    if rt_pressed:
        motor_C.run(MAX_SPEED)
    elif rb_pressed:
        motor_C.run(-MAX_SPEED)
    else:
        motor_C.stop()

    wait(20)
