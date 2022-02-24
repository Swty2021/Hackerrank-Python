#Find a string
S1 = input("Enter original string:")
S2 = input("Enter substring:")
res = sum(1 for i in range(len(S1))if S1.startswith(S2, i))
print(res)
       
