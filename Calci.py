# BLL
import operator
import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# PL
while (1):
    x = int(input("Enter First No:"))
    y = int(input("Enter Second No:"))
    ch = input("Enter Choice +, -, *, /, pow, log:")
    if (ch == "+"):
        r = operator.add(x, y)
        print("Result:", r)
    elif (ch == "-"):
        r = sub(x, y)
        print("Result:", r)
    elif (ch == "*"):
        r = mul(x, y)
        print("Result:", r)
    elif (ch == "/"):
        r = div(x, y)
        print("Result:", r)
    elif (ch == "pow"):
        r = operator.pow(x, y)
        print("Result:", r)
    elif (ch == "log"):
        r = math.log(x, y)
        print("Result:", r)
    else:
        print("Incorrect Choice")
