# bagage problem 0,1

N=int(input('input n : '))
v=list(map(int,input('input values : ').split()))
w=list(map(int,input('input weights : ').split()))
S=int(input('input bagage\'s weight : '))


'''
d=[[0]*(S+1) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1, S+1):
        if j<w[i-1]:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j], d[i-1][j-w[i-1]]+v[i-1])

print(d[N][S])



'''
d=[0]*(S+1) 
for i in range(1,N+1):
    for j in range(S, -1,-1):
        if j<w[i-1]:
            d[j]=d[j]
        else:
            d[j]=max(d[j], d[j-w[i-1]]+v[i-1])

print(d[S])