import sys
import json
from tabulate import tabulate


def messages():
    print(f"1. Add new task\n2. See tasks\n3. Delete task\n4. Reset tasks\n0. Exit ")


def choose(m):
    if m == 1:
        make_new_task()
    elif m == 2:
        read_new_tasks()
    elif m == 3:
        delete_new_tasks()
    elif m == 4:
        reset_tasks()
    elif m == 0:
        exit()
    else:
        print("Idk, pls repeate")


def make_new_task():
    tasks_take = input("Enter your task: ")
    description_take = input("Enter your description for task: ")
    with open("tasks.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
        data[tasks_take] = description_take
    with open("tasks.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def read_new_tasks():
    with open("tasks.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
        table_data = [(key, value) for key, value in data.items()]
        print(tabulate(table_data, headers=["Tasks:", "Description"], tablefmt="fancy_grid"))
        print(data)


def delete_new_tasks():
    tasks_take_del = input("Enter your task for delete: ")
    with open("tasks.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
        del data[tasks_take_del]
    with open("tasks.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def reset_tasks():
    base = {}
    with open("tasks.json", mode="w", encoding="utf-8") as file:
        json.dump(base, file)
    print("Cleared!")


def exit():
    print("Goodbye!")
    sys.exit()
