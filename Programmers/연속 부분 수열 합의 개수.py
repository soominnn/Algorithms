def solution(elements):
    length = len(elements)
    elements *= 2
    case = set()
    for i in range(1, length + 1):
        for start in range(len(elements) // 2):
            total = sum(elements[start: start + i])
            case.add(total)
  
    return len(case)