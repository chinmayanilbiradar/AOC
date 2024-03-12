def main():
    file = open('input.txt','r')
    dirs = []
    values = []
    for line in file:
        line = line.strip()
        arr = line.split(' ')
        dirs.append(arr[0])
        values.append(int(arr[1]))

    path = [(0,0)]
    
    ind_i = 0
    ind_j = 0

    # finding the path of tunnel
    for i in range(len(dirs)):
        if dirs[i] == 'D':
            for x in range(1, values[i]+1):
                path.append((ind_i + x, ind_j))
            ind_i = path[-1][0]
        elif dirs[i] == 'U':
            for x in range(1, values[i]+1):
                path.append((ind_i - x, ind_j))
            ind_i = path[-1][0]
        elif dirs[i] == 'R':
            for x in range(1, values[i]+1):
                path.append((ind_i, ind_j + x))
            ind_j = path[-1][1]
        if dirs[i] == 'L':
            for x in range(1, values[i]+1):
                path.append((ind_i, ind_j - x))
            ind_j = path[-1][1]
    # print(path)
    path.pop()
    
    start_i = start_j = float('inf') 
    end_i = end_j = float('-inf')

    #finding top left and bottom right indices of grid
    for i in path:
        if i[0] < start_i:
            start_i = i[0]
        if i[0] > end_i:
            end_i = i[0]
        if i[1] < start_j:
            start_j = i[1]
        if i[1] > end_j:
            end_j = i[1]
    


    delCol = [0,-1,0,1]
    delRow = [1,0,-1,0]
    vis = set()
    q = [(1, 1)]
    while q:
        curr = q.pop(0)
        print(curr)
        if curr in vis:
            continue
        else:
            vis.add(curr)
            # print(curr[0], curr[1])
            for i in range(4):
                row = curr[0] + delRow[i]
                col = curr[1] + delCol[i]
                # print(row, col)
                if row <= end_i and col <= end_j and (row, col) not in vis and (row, col) not in path:
                    q.append((row, col))
    print(vis)
    print(len(path) + len(vis))

    

if __name__ == "__main__":
    main()