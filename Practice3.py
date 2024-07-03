import re

a = "2"
b = "3"
print(a+b)
x = [1, 3, 4, 9, 5, 7, 1]
print(f"1.) {sum(x)}")

sum_list = 0
for i in range(len(x)):
    sum_list += x[i]

print(f"2.) {sum_list}")

import math
x = [1, 34, 23.5, 7]
sum_lis_1 = math.fsum(x)

sum_lis_2 = 0
for place, value in enumerate(x):
    sum_lis_2 += value

print(f"option 1.) {sum_lis_1} \n"f"option 2.){sum_lis_2}")

x = [12, "cat", 23.0, True]
enum_list = []
for_list = []

for i in range(len(x)):
    for_list.append(x[i])

for place, item in enumerate(x):
    enum_list.append(item)

print(f"enumerate list: {enum_list} \n"f"for_list: {for_list}")

def convert_to_binary(n):
    if n > 1:
        convert_to_binary(n//2)
    print(n % 2, end='')

dec = 34
convert_to_binary(dec)

print(f"\n{bin(dec)[2:1]}")

list1 = []
for i in range(10):
    list1.append(i**2)

list2 = [i**2 for i in range(10)]

print(f"1.) {list1}\n"f"2.) {list2}")
import math

num = 144
print(f"1.) {num**(1/2)}\n"f"2.) {math.sqrt(num)}")

import numpy as np

x = [12, 34, 12, 67, 23, 98, 3, 18, 33, 41, 52, 75]
print(f"1.) {np.average(x)}\n"f"2.) {sum(x)/len(x)}")

import numpy as np

x = [12.5, 23.24, 45.98, 19.2, 12]

print(f"1.) {np.median(x)}")

x.sort()

print(f"2.) {x[int(len(x)/2)]}")

import numpy as np
new_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(new_matrix)

myTuple = ("A", "B", "C")

print(f"1.) {''.join(myTuple)}")

x = ""
for i in range(len(myTuple)):
    x = x + myTuple[i]
print(f"2.) {x}")

x =8
y = 3
print(f"1.) {x * y}")

count = 0
for i in range(y):
    count += x
print(f"2.) {count}")

a, b = 1, 3
a, b = b, a
print(f"a:) {a}, b:{b}")

l1 = ["a", "b"]
l2 = ["z", "x"]

for l1, l2 in zip(l1, l2):
    print(f"2.){l1, l2}")


list = [0,1,3,4,5,6,7,8,9]
print(list[::-2])

s1 = {10,20,30}
s2 = {50,20,"10"}

s3 = s1.union(s2)
print(s3)

list = [[]]*3
list[1].append(5)
print(list)

value = 5
def func():
    value = 15
    print(value, end=" ")
    func()
    print(value)

    

