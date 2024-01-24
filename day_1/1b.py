def solve(s,values):
    # print("called")
    n = len(s)
    arr=[]
    i=0
    while i<n:
        curr=""
        if s[i].isnumeric()==True:
            arr.append(int(s[i]))
        else:
            j=i
            while j<n:
                curr+=s[j]
                if curr in values:
                    arr.append(values[curr])
                    break
                else:
                    j+=1
        i+=1
    # print(arr)
    val = (arr[0]*10)+arr[-1]
    # print(val)
    return val
        
            
def main():
    # print("here")
    ans=0
    values={
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    f=open("input2.txt",'r')
    for s in f:
        ans+=solve(s,values)
    print(ans)


if __name__=="__main__":
    main()