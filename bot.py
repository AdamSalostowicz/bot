#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def greetings(name, year):
    print("Hello! My name is {}.".format(name))
    print("I was created in {}".format(year))


def remind_name():
    name = input("Please, remind me your name.\n")
    print("What a great name you have, {}!".format(name))


def age_guessing():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3 = int(input("remainder by 3 "))
    remainder5 = int(input("remainder by 5 "))
    remainder7 = int(input("remainder by 7 "))
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print("Your age is {}; that's a good time to start programming!".format(
        your_age))


def counting():
    print("Now I will prove to you that I can count to any number you want.")
    number = int(input())
    counter = 0
    while counter <= number:
        print("{} !".format(counter))
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 0
    while answer != 2:
        answer = int(input())
        if answer == 2:
            print("Completed, have a nice day!")
        else:
            print("Please, try again.")


greetings("Andrew", 2021)
remind_name()
age_guessing()
counting()
test()
print("Congratulations, have a nice day!")
