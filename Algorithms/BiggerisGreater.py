#Find the description here: https://www.hackerrank.com/challenges/bigger-is-greater/problem

"""
solution:

convert word to list of number. e.g. "hcdk" -> [4,11,8,3], denoted as A
the question is to find the list B that meets following conditions:
1. share the same numbers as A;
2. there exists t, such that 
    1) B[:t] ==  A[:t]
    2) B[t] > A[t]
    3) B[t] should be as close to A[t] as possible
    4) keep B[t+1:] as small as possible
    
Then comes naturally its solution:
Start from t, find arg(i)min{A[i] | A[i]>A[t]}, swap A[i] and A[t], then sort A[t+1:]
"""

def convert(str, direction):
    arr = list(str)
    if direction == "word2num":
        return [converter[x] for x in arr]
    elif direction == "num2word":
        arr = [alphabet[int(x)-1] for x in arr]
        word = ''
        for i in arr:
            word += i
        return word


def swap(arr, idx1, idx2):
    t = arr[idx2]
    arr[idx2] = arr[idx1]
    arr[idx1] = t
    return arr


def sort(arr):
    j = len(arr) - 1
    while j > 0:
        i = 0
        while i < j:
            if arr[i] > arr[i+1]:
                # swap
                t = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = t
            i += 1
        j -= 1
    return arr


def find_idx(arr, floor):
    minimum = arr[0]
    min_idx = 0
    for i in range(1,len(arr)):
        if floor < arr[i] < minimum:
            minimum = arr[i]
            min_idx = i
    return min_idx


def biggerIsGreater(arr):
    global alphabet
    global converter
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    value = list(range(1,27))
    converter = dict(zip(alphabet, value))

    arr = convert(arr, direction="word2num")
    for i in reversed(range(len(arr)-1)):
        rest_arr = arr[i+1:]
        max_rest = max(rest_arr)
        if arr[i] >= max_rest:
            continue
        else:
            # swap with the smallest element in arr_rest but greater than arr[i]
            idx = find_idx(rest_arr, floor=arr[i]) + i + 1
            arr = swap(arr, i, idx)
            # sort(arr[:i+1], arr[i+1:])
            arr = arr[:i+1] + sort(arr[i+1:])
            return convert(arr, direction="num2word")
    return "no answer"


if __name__ == '__main__':
    file = open("input.txt")
    strlist = file.read().split("\n")
    for word in strlist:
        print(biggerIsGreater(word))







