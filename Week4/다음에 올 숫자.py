def solution(common):
    if common[1]*2 == common[0]+common[2]:
        return common[-1]+ common[1]-common[0]
    return common[-1]*common[1]//common[0]