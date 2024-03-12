from heapq import heappush, heappop 
def main():
    file = open('sample.txt','r')
    grid=[]
    for line in file:
        line = line.strip()
        grid.append(line)
    for i in range(len(grid)):
        grid[i]=list(grid[i])

    grid[0][0]='0'
    m = len(grid[0])
    n = len(grid)
    vis = set()
    q = [(0,0,0,0,0,1),(0,0,0,0,1,0)]
    row_del = [0,1,-1,0]
    col_del = [1,0,0,-1]


    while q:
        heatloss, i, j, steps, idir, jdir = heappop(q)

        if i == n-1 and j == m-1:
            if steps < 4:
                continue
            break
        if (i, j, steps, idir, jdir) in vis:
            continue

        vis.add((i, j, steps, idir, jdir))

        for k in range(4):
            row = i + row_del[k]
            col = j + col_del[k]
            if row >= 0 and row < n and col >=0  and col < m:
                if row_del[k] == -(idir) and col_del[k] == -(jdir):
                    continue
                if row_del[k] == idir and col_del[k] == jdir:
                    if steps < 4:
                        heappush(q, (heatloss + int(grid[row][col]), row, col, steps + 1, row_del[k], col_del[k]))
                        continue
                    if steps >=4 and steps < 10:
                        heappush(q, (heatloss + int(grid[row][col]), row, col, steps + 1, row_del[k], col_del[k]))
                if not(row_del[k] == idir and col_del[k] == jdir) and steps >= 4:
                    heappush(q, (heatloss + int(grid[row][col]), row, col, 1, row_del[k], col_del[k]))
    print(heatloss)


if __name__=="__main__":
    main()