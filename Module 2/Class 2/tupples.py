mytuple= ("apple", "banana","cherry")
print(mytuple)
print(len(mytuple))
print(mytuple[1])
print(mytuple[2:5])
"""
টাপলে সরাসরি কাজ করা যায়না, কোন কিছু চেঞ্জ করা যায়না তাই চেঞ্জ করা লাগলে টাপল কে লিস্ট বানায়ে লিস্টের
সাথে সব অপারেশান করে সেই লিস্ট কে আবার টাপল বানাইতে হবে । 
"""
convert_to_list= list(mytuple)
print(convert_to_list)
convert_to_list[1]="Kiwi"
mytuple=tuple(convert_to_list)
print(mytuple)