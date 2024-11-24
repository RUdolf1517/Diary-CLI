from lib_for_program import *


def motor():
    while True:
        start_message()
        m = int(input("choose the comand:"))
        choose(m)


motor()