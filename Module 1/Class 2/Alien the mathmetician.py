import math


# distance_to_home = 38440
# gravity= 9.8

# thrust_needed= math.sqrt(gravity * distance_to_home)
# print("Thrust Needed: ", thrust_needed)

height=15
base_length= 10
angle_radius= math.atan(height/base_length)  #.atan is used for tan^-1
print(angle_radius)

angle_radius =math.degrees(angle_radius) #.degrees is used for viewing degree 
print(angle_radius)

print("Rounded Angle: ", round(angle_radius)) #point er por 5 er beshi thakle 1 increment

print("Ceilling: ", math.ceil(angle_radius))

print("Floor: ", math.floor(angle_radius))

