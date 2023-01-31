matrix=input()
x,y=(matrix.split())
# print(x)
# print(y)
m=int(x)
n=int(y)

array=[input().split() for i in range(m)]
# print(array)
sum=0
for i in range(m):
    for j in range(n):
        if i==0:
            sum=sum+int(array[i][j])
        elif i==m-1:
            sum=sum+int(array[i][j])
        else:
            if(j==n-1):
                
            
                # print(array[i][0])
                # print(array[i][n-1])
                sum=sum+int(array[i][0])+int(array[i][n-1])
                break

            
print(sum)
