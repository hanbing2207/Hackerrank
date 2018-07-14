# Find the description here: https://www.hackerrank.com/challenges/absolute-permutation/problem

def square(k):
    # return list with len of 2k
    return list(range(k+1,2*k+1)) + list(range(1,k+1))


def absolutePermutation(n, k):

    if k ==0:
        return list(range(1,n+1))
    elif n%(2*k) != 0:
        return [-1]
    else:
        nsquare = int(n/(2*k))
        res = []
        for i in range(nsquare):
            res += [(x+2*k*i) for x in square(k)]
        return res


print(absolutePermutation(8,2))