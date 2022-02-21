from collections import deque


def bfs(begin, target, board, visited):
    
    visited[begin][begin] = True
    q = deque([(begin, 0)])
    
    while q:
        begin, dis = q.popleft()
        if begin == target: return dis
        print(begin, target)
        for j in range(len(board)):
            if board[begin][j] == True:
                if visited[begin][j] == False:
                        q.append((j, dis+1))
                        visited[begin][j] = True
    return 0

def solution(begin, target, words):
    answer = 0
    
    if begin not in words:
        words.append(begin)
    if target not in words:
        words.append(target)
    
    board = [[True] * len(words) for _ in range(len(words))]
    # 변환 가능한 경우를 True로 표현하는 2차원 맵을 그리자
    for idx, word1 in enumerate(words):
        for jdx, word2 in enumerate(words):
            cnt = 0
            for k in range(len(word1)):
                if word1[k] != word2[k]: cnt += 1
            if cnt > 1:
                board[idx][jdx] = False
    
    print(*board, sep='\n')
    
    visited = [[False] * len(words) for _ in range(len(words))]
    answer = bfs(words.index(begin), words.index(target), board, visited)
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))