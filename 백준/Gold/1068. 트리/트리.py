# dfs함수
def dfs(target):

    # 타겟 안에 자식 노드가 있다면!
    
    if graph[target]:
        while graph[target]:

            dfs(graph[target][0])
            graph[target].remove(graph[target][0])

    # 타겟 안에 왼쪽 노드가 없다면!!
    elif not graph[target]:
        return
    
# dfs2함수
def dfs2(root):

    global answer

    if graph[root]:
        for i in range(len(graph[root])):
            dfs2(graph[root][i])
    
    elif not graph[root]:
        answer += 1
        




root = 0

# N은 노드의 개수
N = int(input())

# 노드 정보
information = list(map(int, input().split()))

# 지울 노드
target = int(input())

# 그래프 만들기

graph = [[] for _ in range(len(information))]

# count = 1
for i in range(len(information)):
    # # 루트 이므로 건너뛰자
    if information[i] == -1:
        root = i
        continue
    graph[information[i]].append(i)

dfs(target)

answer = 0

for i in range(len(graph)):
    if target in graph[i]:
        graph[i].remove(target)

dfs2(root)
if target == root:
    print(0)
else:
    print(answer)
# print(answer)