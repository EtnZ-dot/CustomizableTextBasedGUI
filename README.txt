Customizable Text-Based GUI by EtnZ

How to install module into your project:
1. Drag gui.py into your project folder.
2. Write 'import gui' at the beginning of your code.
3. Ruin the stock market?

How to use:
gui.window("What you want to say")
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
| What you want to say                                          |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+

gui.window("1 = Top off", 1)
| 1 = Top off                                                   |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+

gui.window("2 = Top and bottom off", 2)
| 2 = Top and bottom off                                        |

gui.window("change alignment", 0, "center")
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
|                        change alignment                       |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+

gui.window("and to the right", 0, "right")
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
|                                              and to the right |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+

gui.choice(num)
num = how many options the user has
this will let them pick between 1-num
and return the number they picked
ex:
gui.window("Awesome Game title", 0, "center")
gui.window("[1] Sign in", 2)
gui.window("[2] Create account", 2)
gui.window("[3] Quit", 1)
userInput = gui.choice(3)
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
|                       Awesome Game title                      |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
| [1] Sign in                                                   |
| [2] Create account                                            |
| [3] Quit                                                      |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
> 

if you picked 3,
userInput would've equaled to 3
if you pick something that isnt on the list, it retries until you pcik something that is valid.

gui.confirm("basically just gui.choice(2) but it returns with true", num)
num is which confirmation it will pick, from the gui.confirms list
ex:
if gui.confirm("Are you sure you want to exit?"):
	quit()
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
|                 Are you sure you want to exit?                |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
|                  [1] Yes               [2] No                 |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
> 

if you select 1 it will quit the program.


Customization:
you can change these variables and the script will use your designs
gui.border[0] = "The top and bottom of the border"
gui.border[1] = "the left of it"
gui.border[2] = "the right of it"
gui.confirms.append("put something here and if you gui.confirm("blah", 3) it will select the third string in the list (this one)")
gui.inputPrompt("changes the > when you select something")
gui.inputInvalid("changes what it says when you put in something invalid as an input")

Hope you enjoy using my module!