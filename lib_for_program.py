import sys
import json
from tabulate import tabulate


def start_message():
    m1 = print(f"1. Add new task\n2. See tasks\n3. Delete task\n4. Exit ")


def choose(m):
    if m == 1:
        make_new_task()
    elif m == 2:
        read_new_tasks()
    elif m == 3:
        delete_new_tasks()
    elif m == 4:
        exit()
    else:
        print("Idk, pls repeate")



def make_new_task():
    tasks_take = input("Enter your task:")
    description_take = input("Enter your description for task")
    with open("tasks.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)

        data["Tasks:"][tasks_take] = ""
        data["Description"][description_take] = ""

        print(data)

def read_new_tasks():
    with open("tasks.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
        print(tabulate(data, headers="keys", tablefmt="grid"))
        print(data)


def delete_new_tasks():
    pass


def exit():
    print("Goodbye!")
    sys.exit()