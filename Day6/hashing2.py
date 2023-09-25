# def hashing2(n,a):
def hashing2(n):
    dictnary={}


    for i in n:
        if i in dictnary:
            dictnary[i]=dictnary[i]+1
        else:
            dictnary[i]=1
    
    lists=[]
    for i in dictnary.values():
        lists.append(i)
    # print(lists)
    print("Maximum occuring value(s):", end=" ")
    for key, value in dictnary.items():
        if value == max(lists):
            print(f"{key}", end=", ")

    print("\nMinimum occuring value(s):", end=" ")
    for key, value in dictnary.items():
        if value == min(lists):
            print(f"{key}", end=", ")
    # for key,value in dictnary.items():
    #     if value==max(lists):
    #         print("max is - ",key)
    #     elif value==min(lists):
    #         print("min is - ",key)


#     # print(dictnary.values())

n=input() 
# a=input()  
hashing2(n)
# hashing2(n,a)
# my_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 1,'rwe':2}
# for key,values in my_dict.items():
#     if values==2:
#         print(key)
