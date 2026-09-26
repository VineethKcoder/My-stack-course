array=[]
n=int(input("Enter the no of elements in the array : "))
for i in range(n):
    a=int(input("Enter the number : "))
    array.append(a)
print(f"Before : {array}")
i=0
a=[]
while i<n:
    if i==0:
        a.append(array[i])
    else:
        array[i]+=array[i-1]
        a.append(array[i])
    i+=1
print(f"After : {a}")