arr=[1,2,2,3,1,4,3]
d=[]                           #r=2  #d=[] #for i in range(len(arr)) #if arr[i]!=r: #d.append(arr[i])
for i in range(len(arr)):
    if arr[i]!=2:
        d.append(arr[i])
print("Array  : ",d)