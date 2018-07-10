#Find the question here: https://www.hackerrank.com/challenges/queens-attack-2/problem


n, k, r_q, c_q, obstacles = (5,3,4,3,[[5,5],[4,2],[2,3]])


def substract(obs, queen):
    #obs - queen
    return (obs[0]-queen[0], obs[1]-queen[1])

def compare(d, distance):
    #from direction from 1 to 8
    if d[0] > 0 and d[1]==0:
        distance["1"] = d[0]-1 if d[0]-1<distance["1"] else distance["1"]
    elif d[0]==d[1] and d[0]>0:
        distance["2"] = d[0]-1 if d[0]-1 < distance["2"] else distance["2"]
    elif d[1] > 0 and d[0] == 0:
        distance["3"] = d[1]-1 if d[1]-1 < distance["3"] else distance["3"]
    elif d[0] == -d[1] and d[0] < 0:
        distance["4"] = d[1]-1 if d[1]-1 < distance["4"] else distance["4"]
    elif d[1] == 0 and d[0] < 0:
        distance["5"] = -d[0]-1 if -d[0]-1 < distance["5"] else distance["5"]
    elif d[0] == d[1] and d[0] < 0:
        distance["6"] = -d[0]-1 if -d[0]-1 < distance["6"] else distance["6"]
    elif d[1] < 0 and d[0] == 0:
        distance["7"] = -d[1]-1 if -d[1]-1 < distance["7"] else distance["7"]
    elif d[0] == -d[1] and d[0] > 0:
        distance["8"] = d[0]-1 if d[0]-1 < distance["8"] else distance["8"]



#dict containing smallest distance from queen in each direction
# direction 1~8: from north, to northeast ... clockwise
direction = list("12345678")
value = [n-r_q, min(n-r_q, n-c_q), n-c_q, min(n-c_q,r_q-1), r_q-1, min(r_q-1,c_q-1), c_q-1, min(c_q-1,n-r_q)]
distance = dict(zip(direction, value))

queen = (r_q, c_q)
for obs in obstacles:
    d = substract(obs, queen)
    compare(d, distance)

ans = sum(list(distance.values()))
print(ans)


