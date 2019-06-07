# 选择排序
def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp

def selectionsort(a, left, right):
    for i in range(left, right+1):
        for j in range(i+1, right+1):
            if a[i]>a[j]:
                swap(a, i, j)

if __name__=="__main__":
    a=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    selectionsort(a,0, len(a)-1)
    print(a)
 
