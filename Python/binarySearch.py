def binary_Search(arr,x):
    low=0
    high= len(arr)-1
    mid=0

    while low<=high:

        mid=(high+low) // 2

        if arr[mid]<x:
            low=mid+1

        elif arr[mid]>x:
            high=mid-1

        else:
            return mid

    return -1

  

arr=[2,4,34,56,78,67]
x = 78

result =binary_Search(arr,x)

if result == -1:
    print("Element in not present array")

else:
    print("Eliment is present in index",str(result))



            