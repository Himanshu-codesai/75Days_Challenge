def isarmstrongno(n):
    numstr=str(n)
    numstrlength=len(numstr)
    sumofpowers=0
    for digitstr in numstr:
        digit=int(digitstr)
        sumofpowers= sumofpowers+ digit**numstrlength
    if sumofpowers==n:
        print("it is armstrong number")
    else:
        print("not")

n = int(input())
isarmstrongno(n)