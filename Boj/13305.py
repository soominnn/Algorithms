n= int(input())
min = 1000000000
road_length = list(map(int,input().split()))
city_price= list(map(int,input().split()))
sum = 0
for i in range(len(city_price)-1):
    if city_price[i] < min:
        min = city_price[i]
        sum += city_price[i] * road_length[i]
    elif city_price[i] >= min:
        sum += min * road_length[i]
print(sum)