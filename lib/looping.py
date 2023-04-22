#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    new_list = []
    for num in int_list:
        new_num = num ** 2
        new_list.append(new_num)
    return new_list


def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
        if (i % 5 == 0) and (i % 3 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
        i += 1
