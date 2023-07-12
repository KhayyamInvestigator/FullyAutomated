#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all relevant libraries
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import sys
from sympy import *
from sympy import sympify
from spb import plot_implicit

# A function to algebraically solve the two equations and return an array of the roots
def find_intersection(F,G):
    # Simultaneously solve the two equations and save the array to a variable called result
    result = sym.solve([F,G],(x,y))
    # return the array of solutions
    return result

# A function to check that the roots are real and positive
def check_roots(roots):
    # declare some useful variables
    i=0
    discarded_roots = 0
    # A while loop which can run 3 times for each set of roots
    while i < 3:
        # Individually assign x and y from their array
        rx, ry = roots[i]
        # Check if the x root is real
        if sympify(rx).is_real == True:
            # Check if the x root is positive
            if rx > 0:
                # return the positive x root with its y component
                return rx, ry
                # break the loop as only the first positive root is needed
                break
            # if root isnt positive it needs to be discarded
            else:
                #leave a line for readability
                print
                # print why root i was discarded 
                print('Root ', i+1 ,  ' was discarded for being negative')
                # add 1 to discarded root count
                discarded_roots = discarded_roots +1 
        else:
            #leave a line for readability
            print('')
            # print why root i was discarded 
            print('Root ', i+1,  ' was discarded for being complex')
            # add 1 to discarded root count
            discarded_roots = discarded_roots +1 
        # move while loop to the next root
        i+=1  
    # if statement to check if all roots were discarded 
    if discarded_roots == 3:
        #leave a line for readability
        print('')
        # if all 3 roots were discarded then there are no solutions
        print("There are no solutions by Khayyam's method")
        # exit program as no solutions can be plotted
        sys.exit()
        
# some functions induce a spurious root that needs to be discarded
# function has an extra variable input (s) compared to the regular check roots function
def check_spurious(roots, s):
    # most of the functions works the same as check_roots
    i=0
    discarded_roots = 0
    while i < 3:
        rx, ry = roots[i]
        if sympify(rx).is_real == True:
            if rx > 0:
                # Here is where the difference is
                # spurious solution will occure at +-s
                # check if x root = +-s
                if rx == s or rx == -s:
                    # leave a line for readability
                    print('')
                     # if yes then print that the spurious solution has been discarded and move on to the next root
                    print('Discarded spurious solution')
                else:
                    # if no then return the root
                    return rx, ry
                    break
            else:
                print('')
                print('Root ', i+1 ,  ' was discarded for being negative')
                discarded_roots = discarded_roots +1
        else:
            print('')
            print('Root ', i+1,  ' was discarded for being complex')
            discarded_roots = discarded_roots +1
        i+=1  
    if discarded_roots == 3:
        print('')
        print("There are no solutions by Khayyam's method")
        sys.exit()
        
# a function to plot the two conic sections
# input of 2 equations and the x and y roots
def plot_solution(F, G, xroot, yroot):
    # convert the a and y roots to floats
    newxroot = float(xroot)
    newyroot = float(yroot)
    # declare x and y as symbolic
    x, y = symbols('x y')
    # declare an equation which is a vertical line at the x root
    intersection_line = Eq(x, newxroot)
    # plot the three equations where the intersection will be in the centre of the plot
    plot_implicit(F, G, intersection_line, (x,0,2*newxroot), (y,0,2*newyroot))
    # print the approximate solution (exact solution rounded to 1 d.p.)
    print('Approximate x1 solution is: ', round(newxroot,1))
    # print the exact solution as a comparison
    print('Exact x1 solution is: ', newxroot)

# print all the cubic forms for the user to choose from
print('Solving cubics using two conic sections in the sytle of Omar Khayyam')
print('')
print('Cubic forms:')
print(' 0: Cancel program')
print(' 1: x^3 + bx = c')
print(' 2: x^3 + c = bx')
print(' 3: x^3 + c = ax^2')
print(' 4: x^3 + ax^2 = c')
print(' 5: x^3 = bx + c')
print(' 6: x^3 = ax^2 + c')
print(' 7: x^3 = ax^2 + bx + c')
print(' 8: x^3 + ax^2 = bx + C')
print(' 9: x^3 = ax^2 + bx + c')
print('10: x^3 + bx = ax^2 + c')
print('11: x^3 + bx + c = ax^2')
print('12: x^3 + ax^2 + bx = c')
print('13: x^3 + ax^2 + c = bx')

print('')

# take the user's choice of cubic 
userchoice = input('Please choose the form of your cubic or press 0 to cancel: ')

print('')

# an option to cancel the program
if userchoice == '0':
    sys.exit('You have chosen to cancel the program')
#
if userchoice == '1':
    # (for testing) good choice is 14, 55
    # take user input for the coefficients of their cubic
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # parabola equation
    eq1 = sym.Eq(x**2/math.sqrt(b),y)
    # semicircle equation
    eq2 = sym.Eq(b*x**2 + b*y**2, c*x)
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)

if userchoice == '2':
    # (for testing) good choice is 15, -14
    # take user input for the coefficients of their cubic
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # parabola equation
    eq1 = sym.Eq(x**2,y)
    # hyperbola equation
    eq2 = sym.Eq(x*y + c, b*x)
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)

if userchoice == '3':
    # (for testing) good choice is 15,-14
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # parabola equation
    eq1 = sym.Eq(x**2,y)
    # hyperbola equation
    eq2 = sym.Eq(x*y + c, a*y)
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)

if userchoice == '4':
    # (for testing) good choice is 15, -14
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # parabola equation
    eq1 = sym.Eq(x**2,y)
    # hyperbola equation
    eq2 = sym.Eq(x*y + a*y, c)
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '5':
    # (for testing) good choice is 15, -14
    # take user input for the coefficients of their cubic
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # parabola equation
    eq1 = sym.Eq(x**2,y)
    # hyperbola equation
    eq2 = sym.Eq(x*y, b*x + c)
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '6':
    # (for testing) good choice is 15, 19
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # parabola equation
    eq1 = sym.Eq(x**2,y)
    # hyperbola equation
    eq2 = sym.Eq(x*y, a*y + c)
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '7':
    # (for testing) good choice is 15, 19
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # hyperbola equation
    eq1 = sym.Eq((x-a)*(x+(c/b)), y**2)
    # hyperbola equation
    eq2 = sym.Eq(x*y, math.sqrt(b)*x + (c/math.sqrt(b)))
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)

if userchoice == '8':
    # (for testing) good choice is 15, 19
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # hyperbola equation
    eq1 = sym.Eq((x+a)*(x+(c/b)), y**2)
    # hyperbola equation
    eq2 = sym.Eq(x*y, math.sqrt(b)*x + (c/math.sqrt(b)))
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '9':
    # (for testing) good choice is 15, 19
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # hyperbola equation
    eq1 = sym.Eq((x-a)*(x-(c/b)), y**2)
    # hyperbola equation
    eq2 = sym.Eq(x*y, math.sqrt(b)*x - (c/math.sqrt(b)))
    
    exact_sols = find_intersection(eq1,eq2)
    xsol, ysol = check_roots(exact_sols)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '10':
    # (for testing) good choice is 2, 5, 36
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))
    
    # change user inputs to useful variables
    h = math.sqrt(b)
    s = c/b
    
    x, y = sym.symbols('x y')
    # circle equation
    eq1 = sym.Eq((a-x)*(x-s), (h-y)**2)
    # hyperbola equation
    eq2 = sym.Eq(h*(x-s), x*(h-y))
    
    # call functions in order find roots, check roots, plot
    exact_sols = find_intersection(eq1,eq2)
    # in this case we need to use check_spurious
    xsol, ysol = check_spurious(exact_sols, s)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '11':
    # (for testing) good choice is 2, 5, -36
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))
    
    # change user inputs to useful variables
    h = math.sqrt(b)
    s = c/b

    x, y = sym.symbols('x y')
    # circle equation
    eq1 = sym.Eq((a-x)*(x+s), (h-y)**2)
    # hyperbola equation
    eq2 = sym.Eq(h*(x+s), x*(h-y))
    
    # call functions in order find roots, check roots, plot
    exact_sols = find_intersection(eq1,eq2)
    # in this case we need to use check_spurious
    xsol, ysol = check_spurious(exact_sols, s)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '12':
    # (for testing) good choice is 2, 5, -36
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))
    
    # change user inputs to useful variables
    h = math.sqrt(b)
    s = c/b

    x, y = sym.symbols('x y')
    # circle equation
    eq1 = sym.Eq((-a-x)*(x+s), (h-y)**2)
    # hyperbola equation
    eq2 = sym.Eq(h*(x+s), x*(h-y))
    
    # call functions in order find roots, check roots, plot
    exact_sols = find_intersection(eq1,eq2)
    # in this case we need to use check_spurious
    xsol, ysol = check_spurious(exact_sols, s)
    plot_solution(eq1, eq2, xsol, ysol)
    
if userchoice == '13':
 # (for testing) good choice is -13, 8, -2
    # take user input for the coefficients of their cubic
    a = float(input('Enter your a value: '))
    b = float(input('Enter your b value: '))
    c = float(input('Enter your c value: '))

    x, y = sym.symbols('x y')
    # hyperbola equation
    eq1 = sym.Eq((x+a)*(x-(c/b)), y**2)
    # hyperbola equation
    eq2 = sym.Eq(x*y, math.sqrt(b)*b - c/math.sqrt(b))
    
    # call functions in order find roots, check roots, plot
    exact_sols = find_intersection(eq1,eq2)
    # in this case we need to use check_spurious
    xsol, ysol = check_spurious(exact_sols, s)
    plot_solution(eq1, eq2, xsol, ysol)


# In[ ]:




