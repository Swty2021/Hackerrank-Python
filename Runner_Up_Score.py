#RunnerUp Score
run = int(input("Enter number of elements:"))
Li1 = []
for i in range(1,run+1):
    score = int(input("Enter runs:"))
    Li1.append(score)
S1 = set(Li1)
S1.remove(max(S1))
print(max(S1))

