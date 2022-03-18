import copy

# backtracking
def dfs(parent, candidate, animal_cnt, data, graph):
    
    # 노드의 동물 편입
    animal_cnt[data[parent]] += 1
    
    if animal_cnt[1] >= animal_cnt[0]:
        animal_cnt[data[parent]] -= 1
        return 0
    
    # 자식 노드들을 이동 가능 노드에 편입 시키고 백트래킹
    for child in graph[parent]:
        candidate.add(child)
        
    # print(parent, candidate, animal_cnt)
    
    max_ = animal_cnt[0]
    for can in candidate:
        tmp = copy.deepcopy(candidate)
        tmp.remove(can)
        max_ = max(max_, dfs(can, tmp, animal_cnt, data, graph))
    
    animal_cnt[data[parent]] -= 1
    return max_

def solution(data, edges):
    # 그래프 생성
    graph = [[] for _ in range(len(data))]
    for parent, child in edges:
        graph[parent].append(child)
    
    animal_cnt = {0: 0, 1: 0}
    candidate = set()
    
    answer = dfs(0, candidate, animal_cnt, data, graph)

    return answer

print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))