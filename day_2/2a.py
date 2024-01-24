def solve(s,values):
    vals=s.split(" ")
    # print(vals)
    for i in range(len(vals)):
        if vals[i]=='red,' or vals[i]=='red;' or vals[i]=='red\n':
            if int(vals[i-1])>12:
                return False
        if vals[i]=='green,' or vals[i]=='green;' or vals[i]=='green\n':
            if int(vals[i-1])>13:
                return False
        if vals[i]=='blue,' or vals[i]=='blue;' or vals[i]=='blue\n':
            if int(vals[i-1])>14:
                return False
    return True
        
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
        if solve(arr[1],values)==True:
            ans+=val
        val+=1
    print(ans)

if __name__=="__main__":
    main()
