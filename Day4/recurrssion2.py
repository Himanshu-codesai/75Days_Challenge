# def func(n):
#     print("Himanshu \n"*n)

# n = int(input())
# func(n)
def func2(n):
    if n>0:    
        # print("Himanshu")
        func2(n-1)
        print("Himanshu")

n = int(input())
func2(n)