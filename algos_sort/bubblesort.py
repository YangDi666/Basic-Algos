#冒泡排序
def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp

def bubblesort(a, left, right):
    for i in range(0, right-left):
        for j in range(left, right-i):
            if a[j]>a[j+1]:
                swap(a, j, j+1)

if __name__=="__main__":
    a=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    bubblesort(a,0, len(a)-1)
    print(a)
 
