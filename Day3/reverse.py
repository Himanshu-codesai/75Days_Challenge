n = int(input("enter it !!"))
reversednum=0

while n!=0:
    remainder= n%10
    reversednum=reversednum*10+remainder
    n //=10

print(reversednum)

print(2//5)