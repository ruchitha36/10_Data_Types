"""
Day:Monday
Date:23rd Jan 2023
Topic: Data Types
Description: In python there are several datatypes in which we go through the basic data types like Integer,Float,String.
Integer: specified as int which uses Whole Numbers
Float: specified as float which uses decimal point whole numbers
String: specified as str which are enclosed in single,double quotes or three single,double quotes.

"""

'''INTEGER DATA TYPE'''
# print(type(0))
# print(type(4))
# print(type(-1))
# print(type(-4523454))

'''FLOATING DATA TYPE'''
# print(type(0.2))
# print(type(.9))
# print(type(-3.4))
# print(type(-123234.2324))

'''STRING DATA TYPE'''
# print(type('hi'))
# print(type("hi"))
# print(type('''hi'''))
# print(type("""hi"""))
# print(type('py'))
# print(type('7'))
# print(type('9.4'))

'''More Examples'''

# a=6
# print(a,type(a))
# print(int(a))
# print(float(a))
# print(str(a))

''' Concatenating string and float data types'''
# p='Python' ; v=3.1
# print(type(p))
# print(type(v))
# print(p+v)

'''Concatenating Same Data types'''
# a=4 ; b=6
# print(a+b)
# a=4.8 ; b=6
# print(a+b)
# a=4.8 ; b=6.3
# print(a+b)

'''Converting int data type to str to concatenate with the other string'''
# a=4 ; b='6.3'
# print(str(a)+b)

'''Concatenating same data types'''
# print('hi'+'hey')
# print('4'+'8')

'''Converting one data type to other data type'''
# b=7.4
# c='hi'
# print(int(c))   #string cannot be changed to integer
# print(float(c)) #string cannot be changed to float

'''Type conversion of the data type'''
d='9'
print(int(d))
print(float(d))
e='5.8'
print(float(e))
h=float(e)
print(int(h))