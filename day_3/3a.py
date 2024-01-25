def calc(mat,x,y,vis):
    m = len(mat[0])-1
    curr=mat[x][y]
    z=y-1
    while z>=0 and mat[x][z].isdigit()==True:
        curr=mat[x][z]+curr
        vis[x][z]=1
        z-=1
    z=y+1
    while z<m and mat[x][z].isdigit()==True:
        curr+=mat[x][z]
        vis[x][z]=1
        z+=1
    return int(curr)

def solve(mat):
    n=len(mat)
    m=len(mat[0])-1
    vis=[[0 for _ in range(m)] for _ in range(n)]
    x_alt=[-1,+1,-1,+1,-1,1,0,0]
    y_alt=[-1,+1,+1,-1,0,0,-1,1]
    temp=0
    for i in range(n):
        for j in range(m):
            if mat[i][j].isdigit()==False and mat[i][j]!='.':
                for k in range(8):
                    # print(i+x_alt[k])
                    # print(j+y_alt[k])
                    if i+x_alt[k]>=0 and i+x_alt[k]<n and j+y_alt[k]>=0 and j+y_alt[k]<m and mat[i+x_alt[k]][j+y_alt[k]].isdigit()==True and vis[i+x_alt[k]][j+y_alt[k]]==0:
                        # print("enter")
                        temp+=calc(mat,i+x_alt[k],j+y_alt[k],vis)
    return temp

                    
    
def main():
    f = open("input.txt","r")
    ans=0
    mat=[]
    for s in f:
        mat.append(s)
    # print(len(mat))
    # print(len(mat[0]))
    # print(mat)
    ans=solve(mat)
    print(ans)


if __name__=="__main__":
    main()
