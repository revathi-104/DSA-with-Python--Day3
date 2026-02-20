a = [10, 5, 20, 8, 15]
largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
print("Largest number is:", largest)