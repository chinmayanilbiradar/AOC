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
    num1,num2="",""
    for i in range(len(time)):
        num1+=time[i]
        num2+=dist[i]
    ans=solve(int(num1),int(num2))
    print(ans)


if __name__=="__main__":
    main()
