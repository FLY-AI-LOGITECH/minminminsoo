def solution(bandage, health, attacks):
    total= attacks[-1][0]+1 # 마지막 공격 시간
    attacks = dict(attacks) # attacks 딕셔너리로 변경
    MAX = health; success = 0 # 최대 체력, 성공
    time,heal,addheal = bandage # bandage 개별 변수로
    def ismax(x): # 최대 체력 초과 확인 함수
        return min(x,MAX)
    
    for i in range(1,total):
        if i in attacks:# 공격 당할 경우
            health-=attacks[i] # 체력 감소
            success = 0 # 연속 성공 초기화
            if health<=0: # 체력 0 이하면 종료
                return -1
        else: # 공격 안 당하면
            health+=heal# 체력 회복
            health = ismax(health)
            success +=1 # 연속 성공
            if success == time:# 연속 성공이 시전시간과 같으면
                health+=addheal # 추가 체력 회복
                health = ismax(health)
                success = 0
    return health