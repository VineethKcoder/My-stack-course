number=int(input("Enter a number : "))
dup=number
i=0
rev=0
while number>0:
    r=number%10
    rev=rev*10+r
    number=number//10
if rev==dup:
    print("Palindrome")
else:
    print("Not Palindrome")