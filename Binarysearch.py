def Binarysearch(arr,target):
    n=len(arr)
    start=0
    end=n-1
    while(start<=end):
        middle=(start+end)//2
        mid_num=arr[middle]
        if(target==mid_num):
            print("True,at index",middle)
            return
        elif(target>mid_num):
            start+=1 
        else:
            end-=1 
    return(-1)
Binarysearch([1,2,3,4,5],4)