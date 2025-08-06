# tweet = "Hello earth! sunny here reporting from sector 9"
# print(tweet[:5]) #string slicing : er age ja thakbe sekhan theke suru. : er porer ta porzonto hobe.

# print(tweet [-8:]) #Reverse. - 1 theke start.

# print(tweet[6:11])

# #How to replace something inside String

# messy = "visitEarth!! It is so # # green !!!."

# cleaned= messy.replace("#", " ") .replace("!", " ") .replace("e", "M") #Replace case sensitive

# print(cleaned)

# text="Sunny the Alien"
# upper_text= text.upper()
# lower_text=text.lower()
# Capatilize_text=text.capitalize
# print(upper_text)
# print(lower_text)
# print(Capatilize_text)
# text= "the sunny the alien"
# splitText= text.split("the")
# print(splitText)

planet="Earth"
temperature = 22.5678
weather="rainy"
report ="Planet: {} , Temp: {}, Weather: {}" .format(planet,temperature,weather)
print(report)

print("Count of a", report.count("a"))

mass = 73.4587
print(f"My mass {mass: .2f} Kg") #:.2f used to see 2 spcace after point