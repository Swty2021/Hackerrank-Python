#Symmetric Difference
N = int(input())
S1 = set(map(int,input().split()))
M = int(input())
S2 = set(map(int,input().split()))
S3 = S1.symmetric_difference(S2)
S4 = S2.symmetric_difference(S1)
for i in sorted(S3.union(S4)):
    print(i)
