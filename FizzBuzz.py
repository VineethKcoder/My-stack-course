f,b="fizz","Buzz"
for i in range(1,101):
    if i%5==0 and i%3==0:
        print(f + b)
    elif i%3==0:
        print(f)
    elif i%5==0:
        print(b)
    else:
        print(i)