def solution(park, routes):
    row = len(park);col = len(park[0]) # row,col 지정
    move = {'E': [0, 1], 'W': [0, -1], 'N': [-1, 0], 'S': [1, 0]} # 방향 지정
    for r in range(row): # 시작 위치 찾기
        for c in range(col):
            if park[r][c] == 'S':
                SR, SC = r, c
                break # 찾는 순간 바로 종료

    for route in routes:
        X, Y = route.split()
        Y = int(Y)  

        # 경로의 모든 칸이 유효한지 확인
        valid = True
        for step in range(1, Y + 1):
            tmpr = SR + move[X][0] * step
            tmpc = SC + move[X][1] * step

            # 유효성 검사
            if not (0 <= tmpr < row and 0 <= tmpc < col) or park[tmpr][tmpc] == 'X':
                valid = False
                break

        # 경로가 유효하면 이동 반영
        if valid:
            SR += move[X][0] * Y
            SC += move[X][1] * Y

    return SR, SC