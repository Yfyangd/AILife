def alive(x,i,j):
    n=x.shape[0];m=x.shape[1]
    if(i>=0):
        if(i<=n-1):
            if(j>=0):
                if(j<=m-1):
                    return x[i,j]
    if(i<0):
        return 0
    if(j<0):
        return 0
    if(i>n-1):
        return 0
    if(j>m-1):
        return 0
  
def play(x,x2):
    n=x.shape[0];m=x.shape[1]
    for i in range(n-1):
        for j in range(m-1):
            s=alive(x,i+1,j)+alive(x,i+1,j+1)+alive(x,i+1,j-1)+alive(x,i,j-1)+alive(x,i,j+1)+alive(x,i-1,j)+alive(x,i-1,j-1)+alive(x,i-1,j+1)
            s=int(s)
            #print(int(s))
            x2[i,j]=s
        
    for i in range(n-1):
        for j in range(m-1):
            if(x[i,j]==1):
                if(x2[i,j]!=2):
                    if(x2[i,j]!=3):
                        x[i,j]=0

    for i in range(n-1):
        for j in range(m-1):
            if(x[i,j]==0):
                if(x2[i,j]==3):
                    x[i,j]=1
    return(x)