def solve(s,values):
    vals=s.split(" ")
    # print(vals)
    red_max=0
    blue_max=0
    green_max=0
    for i in range(len(vals)):
        if vals[i]=='red,' or vals[i]=='red;' or vals[i]=='red\n':
            if int(vals[i-1])>red_max:
                red_max=int(vals[i-1])
        if vals[i]=='green,' or vals[i]=='green;' or vals[i]=='green\n':
            if int(vals[i-1])>green_max:
                green_max=int(vals[i-1])
        if vals[i]=='blue,' or vals[i]=='blue;' or vals[i]=='blue\n':
            if int(vals[i-1])>blue_max:
                blue_max=int(vals[i-1])
    return red_max*blue_max*green_max
        
def main():
    ans=0
    values={
        "red,":12,
        "green,":13,
        "blue,":14,
        "red;":12,
        "green;":13,
        "blue":14,
        'red\n':12,
        'green\n':13,
        'blue\n':14
    }
    f = open("input.txt","r")
    val=1
    for s in f:
        arr=s.split(":")
        ans+=solve(arr[1],values)
    print(ans)

if __name__=="__main__":
    main()