def solution(numbers):
    tmp = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            tmp.add(numbers[i]+numbers[j])
    return sorted(list(tmp))