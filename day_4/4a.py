def solve(arr):
    inp=arr.split("|")
    win=inp[0].split(" ")
    d={}
    for i in win:
        if i!="":
            d[i]=1
    seq=inp[1].split(" ")
    n=len(seq)
    m=len(seq[-1])
    seq[n-1]=seq[n-1][:m-1] 
    # print(seq)
    cnt=0
    d2={}
    for i in range(len(seq)):
        if seq[i] in d and seq[i] not in d2:
            cnt+=1
            d2[seq[i]]=1
    return int(2**(cnt-1))

        
def main():
    f=open("input.txt","r")
    ans=0
    for s in f:
        arr=s.split(':')
        ans+=solve(arr[1])
    print(ans)


if __name__=="__main__":
    main()
