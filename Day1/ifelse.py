# def compareifelse(a:int,b:int):
#     if (a>b):
#         print("Greater")
#     elif (a<b):
#         print("Smaller")
#     else:
#         print("equal")
    
def compareifelse(a:int,b:int):
    if (a>b):
        return "Greater"
    elif (a<b):
        return "Smaller"
    else:
        return "equal" 
a = input()
b=input()
print(compareifelse(a,b))

# if __name__=="__main__":
#     a = input()
#     b=input()
#     print(compareifelse(a,b))
