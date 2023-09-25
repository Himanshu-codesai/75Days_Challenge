def count_elements_in_array(n):
    dictes={}

    for i in n:
        if i in dictes:
            dictes[i]=dictes[i]+1
        else:
            dictes[i]=1
    # for a,b in dictes.items():
    #     # print(a)
    #     print(b)
    print(dictes)

n=input()
count_elements_in_array(n)

# # a = input()
# # print(type(a))
# # for i in a:

# #     print(i)

a = {}
for i in range(2):
    # if i in a:
    a[i]=1

print(a)