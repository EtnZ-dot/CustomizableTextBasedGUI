# Remember to import gui!
import gui

gui.window("gui.window can print strings in cool looking windows like this!")

gui.window("it can also print without the top of the border by adding a number like so:", 1)

gui.window("1 makes the top border not print and 2 both not print, like this:", 2)

gui.window("it can also make text be centered", 0, "center")

gui.window("or to the right", 0, "right")

# Customization
gui.border[0] = "+=--<-->--<-->--<-->--=+"
gui.border[1] = "[ "
gui.border[2] = " ]"

gui.window("it's also very customizable!")

gui.window("and has it's own choice function!")
gui.window("[1] that's cool af", 2)
gui.window("[2] that's dope af", 1)
userInput = gui.choice(2)
if userInput == 1:
    gui.window("cool right?")
if userInput == 2:
    gui.window("dope right?")
gui.window("and it's own confirm function!", 1)
userInput = gui.confirm("You sure you wanna leave?")
if userInput:
    gui.window("cya later!")
if not userInput:
    gui.window("too bad you're gonna have to")
