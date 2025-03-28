from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.iodevices import XboxController
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.tools import wait

hub = PrimeHub()
motor_A = Motor(Port.A, Direction.CLOCKWISE)
motor_B = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_C = Motor(Port.C)
motor_D = Motor(Port.D)
controller = XboxController()

# תקרת מהירות
MAX_SPEED = 1050

while True:
    buttons = controller.buttons.pressed()

    # קבלת ערכי הג'ויסטיק השמאלי
    x, y = controller.joystick_left()
    right_x, right_y = controller.joystick_right()

    # חישוב מהירות לכל מנוע לפי נוסחת טנק
    right = y + x / 3
    left = y - x / 3

    # קנה מידה למהירות המקסימלית
    motor_A.run(left * 10.5)
    motor_B.run(right * 10.5)

    # שליטה במנוע C עם RT (קדימה) ו-RB (אחורה)
    if right_y > 0:
        motor_C.run(right_y * MAX_SPEED)
    elif right_y < 0:
        motor_C.run(-MAX_SPEED)
    else:
        motor_C.stop()

    # שליטה במנוע D עם LT (קדימה) ו-LB (אחורה)
    if Button.RB > 0:
        motor_D.run(MAX_SPEED)
    elif Button.LB in buttons:
        motor_D.run(-MAX_SPEED)
    else:
        motor_D.stop()

    # סיום בלחיצת כפתור התפריט
    if Button.MENU in buttons:
        hub.speaker.beep()
        print("Goodbye!")
        break

    wait(20)
