import math

def get_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    parking = dict()
    stack = dict()
    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)
        
        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car]
    
    for car, minute in parking.items():
        try:
            stack[car] += 23 * 60 + 59 - minute
        except:
            stack[car] = 23 * 60 + 59 - minute
        
    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key = lambda x : x[0])]