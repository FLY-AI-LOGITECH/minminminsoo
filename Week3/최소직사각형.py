def solution(sizes):
    [i.sort() for i in sizes]
    return max(list(zip(*sizes))[0])*max(list(zip(*sizes))[1])