import random
def datetime():
    import datetime
    return datetime.datetime.now()
time=str(datetime())
def history(a,b):
    h = open("Game_History.txt", "a")
    h.write(time)
    h.write("\n")
    h.write(a)
    h.write("\n")
    h.write(b)
    h.write("\n")
    h.close()
print("This is a text based Player V/S Computer Stone_Paper_Scissor game\n"
      "How to play :\n"
      "Select any one (Stone/Paper/Scissor)\n"
      "If user selects Stone and computer Paper the later wins\n"
      "If user selects Paper and computer Scissor the later wins\n"
      "If user selects Scissor and computer Stone the former wins\n")
choices=["Stone","Paper","Scissor"]
comp_score=0
user_score=0
for i in range(0,10):
    user_choice=input("Enter your choice : ")
    comp_choice=random.choice(choices)
    if user_choice in choices:
        if user_choice=="Stone" and comp_choice=="Paper":
            comp_score+=1
            print(f"Computer : {comp_choice}")
            print(f"Computer earned {comp_score} point\n")
        if user_choice == "Stone" and comp_choice == "Scissor":
            user_score += 1
            print(f"Computer : {comp_choice}")
            print(f"You earned {user_score} point\n")
        if user_choice=="Stone" and comp_choice=="Stone":
            print(f"Computer : {comp_choice}\n")
            print("Draw")
        if user_choice=="Paper" and comp_choice=="Stone":
            user_score+=1
            print(f"Computer : {comp_choice}")
            print(f"You earned {user_score} point\n")
        if user_choice=="Paper" and comp_choice=="Scissor":
            comp_score+=1
            print(f"Computer : {comp_choice}")
            print(f"Computer earned {comp_score} point\n")
        if user_choice=="Paper" and comp_choice=="Paper":
            print(f"Computer : {comp_choice}\n")
            print("Draw")
        if user_choice=="Scissor" and comp_choice=="Stone":
            comp_score+=1
            print(f"Computer : {comp_choice}")
            print(f"Computer earned {comp_score} point\n")
        if user_choice=="Scissor" and comp_choice=="Paper":
            user_score+=1
            print(f"Computer : {comp_choice}")
            print(f"You earned {user_score} point\n")
        if user_choice=="Scissor" and comp_choice=="Scissor":
            print(f"Computer : {comp_choice}\n")
            print("Draw")
if comp_score>user_score:
    print("Computer Won!!")
elif user_score>comp_score:
    print("You Won!!")
else:
    print("Draw")

print("***********************************************************************************************************************")
print("\t\t\tSCOREBOARD")
a=f"Computer : {comp_score}"
b=f"You : {user_score}"
print(a)
print(b)
history(a,b)