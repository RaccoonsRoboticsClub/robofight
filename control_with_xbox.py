from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.iodevices import XboxController
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.tools import wait

hub = PrimeHub()
motor_A = Motor(Port.A, Direction.CLOCKWISE)
motor_B = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_C = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_D = Motor(Port.D, Direction.COUNTERCLOCKWISE)

controller = XboxController()

# תקרת מהירות
MAX_SPEED = 1050

while True:
    buttons = controller.buttons.pressed()

    # קבלת ערכי הג'ויסטיק השמאלי
    lt , rt = controller.triggers()
    # xl, yl = Button.RJ()

    # חישוב מהירות לכל מנוע לפי נוסחת טנק

    # קנה מידה למהירות המקסימלית
    motor_C.run(rt * 10.5)
    motor_D.run(lt * 10.5)

    # סיום בלחיצת RB
    if Button.RB in buttons:
        hub.speaker.beep()
        print("Goodbye!")
        break

    wait(20)
