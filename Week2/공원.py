# GPT 도움 받음..... ㅠ
def solution(mats, park):
    mats.sort()
    mats = mats[::-1]
    def is_subarray(a, b):
        rows_a = len(a);cols_a = len(a[0])
        rows_b = len(b);cols_b = len(b[0])
    # b를 순회하면서 a의 첫 행과 일치하는 부분 찾기
        for i in range(rows_b - rows_a + 1):
            for j in range(cols_b - cols_a + 1):
            # b의 현재 부분과 a 비교
                match = True
                for k in range(rows_a):
                    if b[i + k][j:j + cols_a] != a[k]:
                        match = False
                        break
                if match:
                    return True
        return False
    for _ in mats:
        x = [['-1']*_]*_
        if is_subarray(x,park) == True:
            return _
    return -1