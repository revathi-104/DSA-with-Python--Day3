arr=[1,2,3,4,5]
temp=0
for i in range(len(arr)):
    if i==0:
        temp=arr[i]
        arr[i]=arr[len(arr)-1]
        arr[len(arr)-1]=temp
print("Swipped array: ",arr)
        
