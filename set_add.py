#Set.add()
S = set()
n = int(input("How many elements you want to add:"))
for i in range(1,n+1):
    country_name= input("Enter country name:")
    S.add(country_name)
print(len(S))

