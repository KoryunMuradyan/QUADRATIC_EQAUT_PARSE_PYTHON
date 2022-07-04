#!/usr/bin/python3

import re
import cmath
import sys
import argparse 

def arg_parse_foo():
    linear_parse=argparse.ArgumentParser(description="this script takes a file\
            as an argument from command line in which in ideal shold be an\
            quadric  equation and creates another file containing the solution\
            of the given equation and as a feedback compares the got solution\
            with right solution")
    linear_parse.add_argument('-f', "--file", required = True)
    arguments = linear_parse.parse_args()
    return arguments.file

def read_from_file():
    try:
        with open(arg_parse_foo()) as my_file:
            equat_str = my_file.read()
        equat_str = equat_str.split("\n")[0]
        return equat_str
    except :
        print("File not exist")
        sys.exit()


def get_abc(arg_str):
    arg_str = arg_str.replace(' ', '')
    expr = arg_str.replace('-', ' -')
    a = 0
    b = 0
    c = 0
    members = re.split(' |\+|\=', expr)
    for each in members:
        if '' == each:
            continue
        if '^' in each:
            if '' == each[:-3]:
                a += 1.0
            else:
                if each[0] == '-' and 4 == len(each):
                        a += -1.0
                else:
                    a += float(each[:-3])
        elif each[-1].isnumeric():
            c += float(each)
        elif not each[-1].isnumeric():
            if '' == each[:-1]:
                b += 1.0
            else:
                if 2 == len(each):
                    b += -1.0
                else:
                    b += float(each[:-1])
    return a, b, c

def solve_quad_equation(arg_members):
    a = arg_members[0]
    b = arg_members[1]
    c = arg_members[2]
    dis = (b**2) - (4 * a*c)
    ans1 = (-b-cmath.sqrt(dis))/(2 * a)
    ans2 = (-b + cmath.sqrt(dis))/(2 * a)
    return ans1.real, ans2.real 

def test(x_1, x_2):
    try:
        with open("golden.txt") as golden_num_f:
            golden_num_str = golden_num_f.read()
        golds = golden_num_str.split()
        if (x_1 == float(golds[0]) or x_1 == float(golds[1])) and \
                        (x_2 == float(golds[0]) or x_2 == float(golds[1])):
            print(f"{x_1, x_2} solution is right!\n")
        else:
            print(f"solution is wroong!!!  should be {golden_num_str} \n")
    except IOError:
        print("Golden file not exist")
        sys.exit()

def create_output_file(roots):
    roots_str = str(roots[0]) + ' ' + str(roots[1])
    with open('output.txt', 'w') as output_f:
        output_f.write(roots_str)

def main():
    try:
        #expr = '-x^2 - 4x+4=0'
        expr = read_from_file()
        result = get_abc(expr)
        roots = solve_quad_equation(result)
        create_output_file(roots)
        test(roots[0], roots[1])
    except TypeError:
        print("File arguments are not correct ")


if __name__ == '__main__':
    main()
