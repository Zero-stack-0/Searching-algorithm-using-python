def linearsearch(arr,target):
    n=len(arr)
    for i in range(n):
        if(arr[i]==target):
            print("True the target is at",i)
            return
    return(-1)
linearsearch([1,2,3,4,5,6],5)