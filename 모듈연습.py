def binary_search(arr,start,end,s):
    mid = (start+end)//2
    if(start>end):
        return None
    
    elif(arr[mid]==s):
        return mid

    elif(arr[mid]>s):
        return binary_search(arr,start,mid-1,s)

    else:
        return binary_search(arr,mid+1,end,s)

arr = [1,3,5,6,7,8,10,15]

print(binary_search(arr,0,len(arr)-1,17))
