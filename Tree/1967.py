import sys

class Node:
    def __init__(self, data, w):
        self.data = data
        self.left = None
        self.right = None
        self.dp = (0,0)    # (자식 중 큰 것, 자식의 합)
        self.w = w
        
tree = dict()
tree[1] = Node(1, 0)
N = int(sys.stdin.readline().strip())
for _ in range(N-1):
    p, c, w = map(int, sys.stdin.readline().strip().split())
    # 부모와의 거리가 자식 노드에 저장됨
    tree[c] = Node(c, w)
    if tree[p].left is not None:
        tree[p].right = c
    else:
        tree[p].left = c

def solution(p):
    if tree[p].left == None and tree[p].right ==None: return
    idx_left = tree[p].left
    if tree[p].right != None:
        idx_right = tree[p].right
        max_ = max(tree[idx_left].dp[0] + tree[idx_left].w, tree[idx_right].dp[0] + tree[idx_right].w)
        sum_ = tree[idx_left].dp[0] + tree[idx_left].w + tree[idx_right].dp[0] + tree[idx_right].w
    
    else:
        max_ = tree[idx_left].dp[0] + tree[idx_left].w
        sum_ = tree[idx_left].dp[0] + tree[idx_left].w
    
    # idx가 None을 반환 받은 경우도 고려해야함
    
    tree[p].dp = (max_, sum_)

result = 0
for i in range(N, 0, -1):
    solution(i)
    result = max(result, tree[i].dp[1])

print(result)

''' [review]
이진 트리를 전제로 풀었더니 테케는 맞으나
이진트리가 아닌 테케를 넣으면 틀림
=> 문제 조건 파악에 신경쓰자. 이진트리라는 말 없음.
위 코드는
5
1 2 3
1 3 4
1 4 5
1 5 6
을 입력하면 9가 나옴. 답은 11
'''
