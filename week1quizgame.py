print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay!Lets play the game:)")
score = 0
answer = input("Which continent is known as the Dark Continent? ")
if answer.lower()=="africa":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What gas do we  breath in to stay alive? ")
if answer.lower() == "oxygen":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("How many players are there in cricket team? ")
if answer.lower() == "11":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("Which month has 28 days? ")
if answer.lower() == "all the months":
    print('Correct!')
    score += 1
else:
    print("Incorrect")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")