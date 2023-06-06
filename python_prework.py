#Problem 1
#Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    message = "hello_" + user_name + "!"
    print(message)

#Problem 1 Test
hello_name("ABRAKADABRA")



#Problem 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for i in range(1,101,1):
        if i%2 != 0:
            print(i)
    return(None)

first_odds()



#Problem 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    x = a_list[0]
    for i in a_list:
        if x < i:
            x = i
    return(x)

#Problem 3 Test
a_list = [123456,2,3,4,5,12345]
print(max_num_in_list(a_list))

a_list = [-2,-3,-1,0,-6,-123]
print(max_num_in_list(a_list))



#Problem 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return(True)
        elif a_year % 400 == 0:
            return(True)
        else:
            return(False)
    else:
        return(False)

#Problem 4 Test    
print(is_leap_year(2004))
print(is_leap_year(2001))
print(is_leap_year(2100))
print(is_leap_year(2400))



#Problem 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    a_list_length = len(a_list)
    for i in range(1,a_list_length):
        if a_list[i-1] + 1 == a_list[i]:
            return(True)
        else:
            return(False)

#Problem 5 Test
a_list = [-2,0,1,123245]
print(is_consecutive(a_list))

a_list = [-2,-1,0,1,2,3,4,5]
print(is_consecutive(a_list))