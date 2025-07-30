print("Hi! Welcome to our quiz.")
score = 0

ques_1 = input("What is PC stands for?")
if ques_1 == "Personal Computer":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")


ques_2 = input("What is CPU stands for?")
if ques_2 == "Central Processing Unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

ques_3 = input("What is RAM stands for?")
if ques_3 == "Random Access Memory":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

ques_4 = input("What is GPU stands for?")
if ques_4 == "Graphics Processing Unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

ques_5 = input("What is PSU stands for?")
if ques_5 == "Power Supply Unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

ques_6 = input("What is ROM stands for?")
if ques_6 == "Read Only Memory":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

print("You got " + str(score) + " questions correct!")
print("Congratulations!! You got " + str((score / 6) * 100) + "%.")
