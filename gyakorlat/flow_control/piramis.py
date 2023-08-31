"""
Knáb István Gellért
SZTAKI
2023.08.01.
"""
import math
import numpy

# Onallo feladat
# Todo: Készíts egyszerű programot ami egy piramist rajzol
#  ki, úgy, hogy a feljebbi szintekről mindig 2-vel több egyes jelenik meg.
#  Ennek méretét induláskor lehessen megadni

size = int(input("Mekkora legyen?"))
original_size = size
size = size + 10

if size % 2 ==0:
    size += 1
else:
    size = size

list_of_zeros = numpy.zeros(size)
middle = math.floor(size -size/2)

for i in range(original_size):
    list_of_zeros[middle] = 1
    if i == 0:
        print(list_of_zeros)
        continue
    for j in range(size):
        if list_of_zeros[j] == 1 :
            if j == 0 or j == size-1:
                break
            list_of_zeros[j-1] = 1
            list_of_zeros[size-j] = 1


    print(list_of_zeros)

