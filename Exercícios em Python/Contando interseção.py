n1 = int(input())
v1 = set(map(int, input().split()))

n2 = int(input())
v2 = set(map(int, input().split()))

comum = v1 & v2

print(len(comum))