M, N = list(map(int, input().split()))
maze = []
for i in range(M):
    maze.append(input().split())
b = [[-1] * N for _ in range(M)]
print(maze)
