def datatype(inputs):
    if inputs=="Integer":
        return 4
    elif inputs=="Long":
        return 8
    elif inputs=="Float":
        return 4
    elif inputs=="Double":
        return 8
    elif inputs=="Character":
        return 1
    
if __name__ == "__main__":
    a = input()
    print(datatype(a))
    