def solve(num,arr,cards):
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
    cards[num]=cnt

        
def main():
    f=open("input.txt","r")
    ans=0
    cards={}
    freq={}
    num=1
    for s in f:
        arr=s.split(':')
        solve(num,arr[1],cards)
        num+=1
    for i in cards.keys():
        freq[i]=1
    for i in freq.keys():
        for j in range(freq[i]):
            for k in range(i+1,cards[i]+i+1):
                # ans+=1
                if k in freq:
                    freq[k]+=1
    for i in freq.keys():
        ans+=freq[i]
    print(ans)
    



if __name__=="__main__":
    main()