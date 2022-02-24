#Set Intersection
N = int(input())
S1 = set(map(int,input().split()))
M = int(input())
S2 = set(map(int,input().split()))
S3 = S1.intersection(S2)
print(len(S3))
