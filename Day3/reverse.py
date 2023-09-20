n = int(input("enter it !!"))
reversednum=0
a=n

while n!=0:
    remainder= n%10
    reversednum=reversednum*10+remainder
    n //=10

print(reversednum)

if reversednum==a:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
# print(2//5)