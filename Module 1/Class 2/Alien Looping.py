# donuts= ["glazed", "chocolate", "galactic sprinkle", "nut"]
# print(donuts)

# for x in donuts: #donut er shob value x e one by one dhukbe  
#     print(x) 

# angle = 0
# while angle <90:
#     print("Angle:" , angle)
#     angle=angle+30

# i=1
# while i<11:
#     print(i)
#     i=i+2

# for i in range (1,11,2): #1 theke start 11 er ag porzonto print 2 kore increment
#     print(i)
    
# for i in range (10,0,-1): #1 theke start 11 er ag porzonto print 2 kore increment
#     print(i)
    
protocols= ["ok","ok","bad","ok""bad"]
for i, protocol in enumerate(protocols): # i diye index asche protocol diye value
    print(i, protocol)
    if protocol == "bad":
        break