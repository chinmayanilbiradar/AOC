def main():
    vertices = [(0, 0)]
    dirr = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    b = 0
    for line in open('input.txt', 'r'):
        _, _, x = line.split()
        x = x[2:-1]
        dr, dc = dirr["RDLU"[int(x[-1])]]
        n = int(x[:-1], 16)
        b += n
        r, c = vertices[-1]
        vertices.append((r + dr*n, c + dc*n))
    a = abs(sum(vertices[i][0] * (vertices[i-1][1] - vertices[(i + 1) % len(vertices)][1]) for i in range(len(vertices)))) // 2
    i = a - b // 2 + 1
    print(i + b)
    
    



if __name__ == "__main__":
    main()