#Mutation
S1 = input("Enter a string:")
L1 = list(S1)
P1 = int(input("Enter position:"))
C1 = input("Enter new character:")
L1[P1]= str(C1)
S1 = ''.join(L1)
print(S1)
