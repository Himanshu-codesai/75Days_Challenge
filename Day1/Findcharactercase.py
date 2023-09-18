def Findcharactercase(a):
    if a.isupper():
        return '1'
    elif a.islower():
        return '0'
    else:
        return '-1'
ab = input()
print(Findcharactercase(ab))    

# Another way to solve
# fcc=input()
# if fcc.isupper():
#     print('1')
# elif fcc.islower():
#     print('0')
# else:
#     print('-1')
