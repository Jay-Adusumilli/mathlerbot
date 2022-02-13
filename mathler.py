import sys
from time import sleep
import os
from sympy import sympify
import re


if len(sys.argv) != 2:
    print("Useage: python mathler.py input.txt")
    quit()
name = sys.argv[1]
with open(name, "r") as fp:
    answer_list = fp.read().splitlines()

chars = []
notchars = []
spaces = len(answer_list[0])
final = [None] * spaces

def printanswers():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nNum guesses: " + str(len(answer_list)) + "\n")
    if len(answer_list) > 60:
        trunc = answer_list[:60] + ["...","...","...","...","...","..."]
        x = 1
    else:
        trun = answer_list
    for a,b,c,d,e,f in zip(trunc[::6],trunc[1::6],trunc[2::6],trunc[3::6],trunc[4::6],trunc[5::6]):
        print ('{:<10}{:<10}{:<10}{:<10}{:<10}{:<}'.format(a,b,c,d,e,f))
        print("")
        sleep(0.05)
    print("")
    

def removeanswers():
    temp_list = []
    new = ""
    [new.join(i) for i in chars]
    x = re.compile('^['+new+']+$')
    for i,index in answer_list:
         if x.match(i) == None:
             answer_list.remove(index)
             index -= 1


while (len(answer_list) > 1):
    try:
        printanswers()
        first = input("Input: ")
        firstc = input("Colors [g/y/r]: ")

        for i in range(len(firstc)):
            if firstc[i] == 'g':
                final[i] = first[i]
                chars.append(first[i])
            if firstc[i] == 'r':
                notchars.append(first[i])
            if firstc[i] == 'y':
                chars.append(first[i])
        print(chars)
        print(notchars)
        print(final)
        print(len(answer_list))

        removeanswers()
        print("here")
        print(len(answer_list))

    except KeyboardInterrupt:
        print("\nQuiting...")
        quit()


