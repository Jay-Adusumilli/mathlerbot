from queue import Empty
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
usablechars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']
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
    yeschars = chars[:]
    yeschars.extend(usablechars)
    x = re.compile('^['+"".join(notchars).replace('-','\-')+']+$')
    y = re.compile('^['+"".join(yeschars).replace('-','\-')+']+$')
    for i in range(0,len(answer_list)):
        if i<len(answer_list):
            if re.search(x,answer_list[i]) or not re.search(y,answer_list[i]):
                answer_list.remove(answer_list[i])
                i -= 1


while (len(answer_list) > 1):
    try:
        printanswers()
        first = input("Input: ")
        firstc = input("Colors [g/y/r]: ")

        for i in range(len(firstc)):
            if first[i] in usablechars:
                if firstc[i] == 'g':
                    final[i] = first[i]
                    chars.append(first[i])
                    usablechars.remove(first[i])
                elif firstc[i] == 'y':
                    chars.append(first[i])
                    usablechars.remove(first[i])
                elif firstc[i] == 'r':
                    notchars.append(first[i])
                    usablechars.remove(first[i])
            
        print(chars)
        print(notchars)
        print(final)
        print(usablechars)
        print(len(answer_list))

        removeanswers()
        print("here")
        print(len(answer_list))

    except KeyboardInterrupt:
        print("\nQuiting...")
        quit()
    if usablechars is Empty:
        break


