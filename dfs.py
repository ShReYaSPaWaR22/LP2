visited = []
def dfs(visited,graph,node):
    if node not in visited :
        visited.append(node)
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited :
               dfs(visited,graph,neighbour)

graph = {'3':['1','2'],'2':['4'],'1':['5'],'4':[],'5':[]}
print("THE DFS FOR GIVEN GRAPH IS : ")
dfs(visited,graph,'3')