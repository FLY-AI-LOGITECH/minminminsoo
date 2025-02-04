def solution(array, commands):
    answer = []
    for i in commands:
        start,end,num = i
        tmp = array[start-1:end]
        tmp.sort()
        answer.append(tmp[num-1])
    return answer