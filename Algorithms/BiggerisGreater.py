#Find the description here: https://www.hackerrank.com/challenges/bigger-is-greater/problem

alphabet = list("abcdefghijklmnopqrstuvwyz")
value = list(range(1,25))
converter = dict(zip(alphabet, value))


def convert(str, direction):
    arr = list(str)
    if direction == "word2num":
        return [converter[x] for x in arr]
    elif direction == "num2word":
        return [alphabet[int(x)-1] for x in arr]


# str = "dkhc"
# print(convert(str, direction="word2num"))
#
#
# convert([4,3,8,11], direction="num2word")
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


def NextWord(arr):
    arr = convert(arr, direction="word2num")
    for i in reversed(range(len(arr)-1)):
        rest_arr = arr[i+1:]
        max_rest = max(rest_arr)
        max_idx_in_arr = rest_arr.index(max_rest) + i + 1
        if arr[i] >= max_rest:
            continue
        else:
            # swap
            print(i)
            arr = swap(arr, i, max_idx_in_arr)
            # sort(arr[:i+1], arr[i+1:])
            arr = arr[:i+1] + sort(arr[i+1:])
            return convert(arr, direction="num2word")

arr = "dkhc"
print(NextWord(arr))



