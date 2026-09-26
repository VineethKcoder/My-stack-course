sum=0
num=int(input("Enter a number : "))
while num:
    a=num%10
    sum+=a
    num=num//10
print(f"Sum of digits is {sum}")