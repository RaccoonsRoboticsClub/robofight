from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.iodevices import XboxController
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.tools import wait

hub = PrimeHub()
motor_A = Motor(Port.A, Direction.CLOCKWISE)
motor_B = Motor(Port.B, Direction.COUNTERCLOCKWISE)
controller = XboxController()

# תקרת מהירות
MAX_SPEED = 1050

while True:
    buttons = controller.buttons.pressed()

    # קבלת ערכי הג'ויסטיק השמאלי
    x, y = controller.joystick_left()

    # חישוב מהירות לכל מנוע לפי נוסחת טנק
    right = y + x / 3
    left = y - x / 3

    # קנה מידה למהירות המקסימלית
    motor_A.run(left * 10.5)
    motor_B.run(right * 10.5)

    # סיום בלחיצת RB
    if Button.RB in buttons:
        hub.speaker.beep()
        print("Goodbye!")
        break

    wait(20)
