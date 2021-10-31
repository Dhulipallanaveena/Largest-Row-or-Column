'''
def largestrowsum(li):
    n=len(li)
    m=len(li[0])
    max_sum=-1
    max_index=-1
    for i in range(n):
        sum=0
        for j in range(m):
            sum=sum+li[i][j]
        if sum> max_sum:
            max_index=i
            max_sum=sum
        elif sum==max_sum:
            if max_index>i:
                max_index=i
                max_sum=sum
    return max_index,max_sum
def largestcolsum(li):
    n=len(li)
    m=len(li[0])
    max_sum=-1
    max_index=-1
    for j in range(m):
        sum=0
        for i in range(n):
            sum=sum+li[i][j]
        if sum>max_sum:
            max_index=j
            max_sum=sum
    return max_index,max_sum
m,n=[int(i) for i in input().split(" ")]
l=[int(i) for i in input().strip( ).split(' ')]
arr=[[l[(j*n)+i] for i in range(n)] for j in range(m)]
row=largestrowsum(arr)
col=largestcolsum(arr)
if row[1]> col[1]:
    print('row',end=' ')
    print(row[0],end=' ')
    print(row[1],end=" ")
elif col[1]>row[1]:
    print('column',end=" ")
    print(col[0],end=" ")
    print(col[1],end=" ")
else:
    print('row',end=" ")
    print(row[0],end=" ")
    print(row[1],end=" ")
