from itertools import product
from sympy import sympify
from tqdm import tqdm
import multiprocessing as mp
import os

chars = "0123456789+-*/"
spaces = 6
answer = 8
oper = ["+", "-", "*", "/"]
non_zeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

answer_list = []


def isValid(exp):
    has_ops = 0
    if exp[0] == "0":
        return None
    if exp[0] in oper or exp[spaces - 1] in oper:
        return None
    for i in range(len(exp) - 1):
        if exp[i] in oper:
            has_ops = 1
        if exp[i] in oper and exp[i + 1] in oper:
            return None
        if exp[i] in oper and exp[i + 1] == "0":
            return None
    if has_ops == 0:
        return None
    return exp
    

def equalsAnswer(temp):
    if sympify(temp) == answer:
        return temp


if __name__ == "__main__":
    all_valid = []
    total = (len(chars) ** spaces)
    cores = mp.cpu_count()
    print("\nFiltering all valid strings:")
    with mp.Pool(processes=cores) as pool:
        for p in tqdm(pool.imap_unordered(func = isValid,iterable = product(chars, repeat = spaces), chunksize = 500000), total = total):
            if p != None:
                all_valid.append(p)

    #all_valid[:] = ["".join(x) for x in all_valid if x != None]

    print("\nGetting all answers to " + str(answer) + ":")
    with mp.Pool(processes=cores) as pool:
        for a in tqdm(pool.imap_unordered(func = equalsAnswer,iterable = all_valid, chunksize = 1000), total = len(all_valid)):
            answer_list.append(a)

    answer_list[:] = [x for x in answer_list if x != None]
    name = str(answer) + "_" + str(spaces) + "_valid_exp.txt"
    fp = open(name, "w")
    print("\nOutputting file: ")
    for i in tqdm(answer_list, total = len(answer_list)):
        temp = i + "\n"
        fp.write(temp)

    fp.close()
