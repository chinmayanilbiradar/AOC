def solve(time,record):
    ways=0
    for i in range(1,time):
        dist=i*(time-i)
        if dist>record:
            ways+=1
    return ways


def main():
    file = open("input.txt",'r')
    time=[]
    dist=[]
    for s in file:
        if "Time:" in s:
            curr=s.split(":")
            for j in curr[1].split(" "):
                if j!="":
                    time.append(j)
            time[-1]=time[-1][:-1]
        if "Distance:" in s:
            curr=s.split(":")
            for j in curr[1].split(" "):
                if j!="":
                    dist.append(j)
    ans=1
    for i in range(len(time)):
        ans*=solve(int(time[i]),int(dist[i]))
    print(ans)


if __name__=="__main__":
    main()