# what is loop?
# A loop is used to repeat a block of code multiple times until a condition is  not .

#range() function is commonly used to generate a sequences of numbers.

#range comes with 3 parameters.
#1. start (inclusive)
#2. stop (exclusive)
#3. step (optional,default is 1)

#Types of loops in python 

# 1.for loop : #Used when we know how many times we want to repeat
#syntax:
#for variable in sequence:
     #code

# for i in range(1,6):
#     print(i)

# key points:
# 1.range (start ,stop) generates numbers
# 2.loop runs fixed numbers of times

# 2.while loop: used when we repeat until a comdition becomes False

# syntax:
# while condition:
#     ConnectionAbortedError

# ex:
# i=1
# while i<=5:
#     print(i)
#     i+=1
# o/p=1,2,3,4,5

#TAsk 1:
# print numbers from 1 to 10 :
# for i in range(1,11):
#     print(i)

#Task 2
#print even numbers from 1 to 20
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

#task 3
#print odd numbers from 1 to 15
# for i in range(1,16,2):
#         print(i)

#Task 4
#print each character of python in string
# text="python"
# for char in text:
#     print(char)
#outpuy
# p
# y
# t
# h
# o
# n

#Task 5:
#print all items in the list.

# data = ["Data","Science","Ai"]
# for item in data:
#     print(item)

#output
# Data
# Science
# Ai

#Task 6:
# Find the sum of numbers 1 to 10.
# total =0
# for i in range(1,11):
#     total += i
# print(total)
#output
#55

#Task 7:
#multiplication of table of 5.
# for i in range(1,11):
#     print("5 x" , i ,"=",5*i)
#output

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

#Task 8
#count how many vowel is a string
# text="Hello world"
# vowels="aeiou"
# count=0
# for ch in text:
#     if ch in vowels:
#         count += 1
#         print(count)
# #output 
# 3

#task 9
# print numbers in reverse order from 10 to 1.
# for i in range (10,0,-1):
#     print(i)

#output
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

#task 10:
# print square of numbers from 1 to 5.
# for i in range(1,6):
#     print(i*i)

#output
# 1
# 4
# 9
# 16
# 25

    

