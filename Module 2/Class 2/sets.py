# thisset = {"Apple", "Banana", "Apple","Grape", True,1,2} #True Means 1, False Means 0. So only True will be showd 1 won't as set returns only single time a item
# print(thisset) #Sets does not return duplicate value.

# #Adding New value in Set

# thisset.add("orange")
# print(thisset)

# topical = {"Pinaple","Mango","Papaya"}

# #Marging 2 sets:
# thisset.update(topical)
# print(thisset) #Marged Set
# print(topical) #This one will be unchanged

# thisset.remove("Papaya") #removing pinaple
# print(thisset)

set1 = {"a","b","c"}
set2={1,2,3,"a","c"}
set3= set1.union(set2)
print(set3)
set3=set1.intersection(set2)
print(set3)

set4=set1.difference(set2) #Difference discards the common ones.
print(set4)
set5=set2.difference(set1)
print(set5)