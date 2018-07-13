#Find the description here: https://www.hackerrank.com/challenges/lilys-homework/problem


import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def get_index(array, kind):
    """
    return the index of max or min value in a list
    :return: 
    """
    if kind == "max":
        m = array[0]
        m_idx = 0
        for i in range(len(array)):
            if array[i] > m:
                m = array[i]
                m_idx = i
    if kind == "min":
        m = array[0]
        m_idx = 0
        for i in range(len(array)):
            if array[i] < m:
                m = array[i]
                m_idx = i
    return m_idx


def sort(arr, direction):
    if direction == "forward":
        smallest = min(arr[1:])
        if arr[0] > smallest:
            global count1
            count1 += 1
            min_idx = arr.index(smallest)
            arr[min_idx] = arr[0]
        return arr[1:]
    else:
        smallest = min(arr[:-1])
        if arr[-1] > smallest:
            global count2
            count2 += 1
            min_idx = arr.index(smallest)
            arr[min_idx] = arr[-1]
        return arr[:-1]


def lilysHomework(arr):
    arr2 = arr.copy()
    global count1
    count1 = 0

    while len(arr) != 1:
        print(len(arr))
        arr = sort(arr, direction="forward")

    global count2
    count2 = 0
    while len(arr2) != 1:
        arr2 = sort(arr2, direction="backward")

    return min(count1, count2)


if __name__ == '__main__':

    n = 4
    blocks = []
    file = open("input2.txt")
    strlist = file.read().split(" ")
    arr = [int(x) for x in strlist]

    result = lilysHomework(arr)

    print(result)

