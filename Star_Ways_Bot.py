# Stars Wars Bot
# Author: Ubial
# Date: 16 October 2023

print("I will decide if you can join the Dark Side.")

qt_1 = input("Is red your favourite color?")
qt_2 = input("Do you like capes?")

fave_color = ("no")
like_capes = ("no")

fave_color_an2 = ("yes", "no")
like_capes_an2 = ("yes", "no")


if qt_1.lower().strip(",.?! ") in fave_color and qt_2.lower().strip(",.?!") in like_capes:
    print("Light side, I see.")

elif qt_1.lower().strip(",.?! ") in fave_color_an2 and qt_2.lower().strip(",.?!") in like_capes_an2:
    print("Dark side it is!")

else:
    print("Light side, I see.")   




