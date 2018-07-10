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


def swap(array1, array2, idx1, idx2):
    t = array2[idx2]
    array2[idx2] = array1[idx1]
    array1[idx1] = t


class stopit(Exception):
    pass


def split_n_sort(blocks):
    """
    split each block in blocks into two half, and swap max of block1 and min of block2
    :param blocks: list of block
    :return: 
    """
    global count
    global nblocks
    new_blocks = []
    done = True
    for block in blocks:
        if len(block) == 1:
            continue
        demi = int(len(block)/2)
        block1 = block[:demi]
        block2 = block[demi:]

        if max(block1) > min(block2):
            count += 1
            # print(count)
            b1_max = get_index(block1, "max")
            b2_min = get_index(block2, "min")
            swap(block1, block2, b1_max, b2_min)
            done = False
        new_blocks.append(block1)
        new_blocks.append(block2)
        nblocks = new_blocks.copy()
        print("done: ", done)
    if not done:
        print("newblock: ", new_blocks)
        split_n_sort(new_blocks)
    else:
        raise stopit





def lilysHomework(arr):
    global count
    count = 0
    try:
        blocks, count = split_n_sort([arr])
    except stopit:
        return count


if __name__ == '__main__':

    n = 4
    blocks = []
    file = open("input.txt")
    strlist = file.read().split(" ")
    arr = [int(x) for x in strlist]
    # arr = [2,5,3,1]

    result = lilysHomework(arr)

    print(result)

