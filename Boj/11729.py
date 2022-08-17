n = int(input())
def hanoi(n,fro,by,to):
    if n == 1:
        print(fro, to)

    else:
        hanoi(n-1,fro,to,by)
        print(fro, to)
        hanoi(n-1,by,fro,to)
print(2**n-1)
hanoi(n,1,2,3)