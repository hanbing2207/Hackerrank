# Find the description here: https://www.hackerrank.com/challenges/larrys-array/problem

"""
solution:

another understanding of "rotation": 
    Every time a rotation happens, means that one number jumps forward or backward by 2 units

So we only have to count the Inversion of permutation.
"""

A = [1,3,4,2]

def larrysArray(A):
    count = 0
    for i in range(1,len(A)):
        for j in range(i):
            if A[j] > A[i]:
                count += 1

    if count%2 == 0:
        return "YES"
    else:
        return "NO"

print(larrysArray(A))