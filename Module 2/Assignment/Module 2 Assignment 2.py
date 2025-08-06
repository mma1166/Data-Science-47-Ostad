A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
AunionB = A.union(B)
BunionA= B.union(A)
print(f'A Union B : {AunionB}')
print(f'B Union A : {AunionB}')
AintersectionB = A.intersection(B)
BintersectionA= B.intersection(A)
print(f'A Intersection B : {AintersectionB}')
print(f'B Intersection A : {BintersectionA}')
differenceBetweenAandB= A.difference(B)
differenceBetweenBandA=B.difference(A)
print(f'Difference Between Set A and Set B is : {differenceBetweenAandB}')
print(f'Difference Between Set B and Set A is : {differenceBetweenBandA}')