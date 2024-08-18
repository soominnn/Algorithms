N = int(input())
tshirts = list(map(int, input().split()))
T, P = map(int, input().split())
shirt_count = 0 

for tshirt in tshirts:
    if tshirt % T == 0:
        shirt_count += tshirt // T
    else:
        shirt_count += tshirt // T + 1    
print(shirt_count)
print(N // P, N % P)
