"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Riley Callahan.
"""
########################################################################
# TODO: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 2)
blue_turtle.speed = 10  # Fast
size = 300
for k in range(25):
    blue_turtle.draw_square(size)
    blue_turtle.pen_up()
    blue_turtle.left(45)
    blue_turtle.forward(11)
    blue_turtle.right(45)
    blue_turtle.pen_down()
    size = size - 12

red_turtle = rg.SimpleTurtle('arrow')
red_turtle.pen = rg.Pen('red', 2)
red_turtle.speed = 10  # Fast
red_turtle.pen_up()
red_turtle.left(45)
red_turtle.backward(450)
red_turtle.right(45)
red_turtle.pen_down()
size2 = 300
for k in range(25):
    red_turtle.draw_square(size2)
    red_turtle.pen_up()
    red_turtle.left(45 + (25 - k))
    red_turtle.forward(11)
    red_turtle.right(45)
    red_turtle.pen_down()
    size2 = size2 - 12

window.close_on_mouse_click()
