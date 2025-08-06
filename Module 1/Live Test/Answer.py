user_score = int(input("Please Enter the user score: "))

if user_score >=90 and user_score <= 100:
    print("Student's Grade is: A")
elif user_score >=80 and user_score <= 89:
    print("Student's Grade is: B")
elif user_score >=70 and user_score <= 79:
    print("Student's Grade is: C")
elif user_score >=60 and user_score <= 69:
    print("Student's Grade is: D")
elif user_score >=50 and user_score <= 59:
    print("Student's Grade is: E")
elif user_score >=40 and user_score <= 49:
    print("Student's Grade is: E-")
elif user_score <40:
    print("Student's Grade is: F")
else:
    print("Invalid Score!\nPlease Enter a valid score.")

