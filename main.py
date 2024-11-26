from lib_for_program import *


def motor():
    while True:
        messages()
        m = int(input("choose the comand:"))
        choose(m)


motor()
