#main
X,Y = (4,4)
data = []
# fundamental_data.append([[0,0],[0,1],[1,0],[2,0]])
# fundamental_data.append([[0,0],[0,1],[1,1]])
# fundamental_data.append([[0,0],[1,0]])
# fundamental_data.append([[0,0],[0,1],[0,2]])
# fundamental_data.append([[0,0],[1,0],[1,1],[2,1]])
data.append([[0,0],[0,1],[1,1]])
data.append([[0,0],[1,0],[1,1],[2,0],[3,0]])
data.append([[0,0],[0,1],[0,2],[1,0]])
data.append([[0,0],[0,1],[1,1],[2,1],[3,1]])
data.append([[0,0],[0,1],[1,0]])
data.append([[0,0],[1,0],[1,1],[1,2],[0,2]])
X,Y = (5,5)



class BreakIT(Exception):
    pass


def next_path(path):
    nexts = []
    #get occupied:
    occupied = []
    for i in range(len(path)):
        block = data[i]
        for point in block:
            point_mv = [point[0]+path[i][0], point[1]+path[i][1]]
            occupied.append(point_mv)
    #for next block
    block = data[len(path)]
    for x in range(X):
        for y in range(Y):
            occu = False
            for point in block:
                if point[0]+x>=X or point[1]+y>=Y:
                    occu = True
                    break
                for ref in occupied:
                    if point[0]+x==ref[0] and point[1]+y==ref[1]:
                        occu = True
            if not occu:
                nexts.append([x,y])
    return nexts


def add_paths(current_paths,i):
    global res
    new_paths = []
    for path in current_paths:
        for new in next_path(path):
            new_paths.append(path+[new])

    if i+1 == len(data)-1:
        res.append(new_paths)
        raise BreakIT
    else:
        add_paths(new_paths,i+1)


try:
    res = []
    init_paths = next_path([])
    init_paths = [[x] for x in init_paths]
    add_paths(init_paths,0)
except BreakIT:
    print("Optimal path:\n",res)

