import random
playing = True
while playing:
    user_choice = (input("enter a choice between rock,paper,sisscors:"))
    possible_actions = ["rock","paper","sisscors"]
    computer_choice = random.choice(possible_actions)
    print(f"comuter chose{computer_choice}\n")
    print(f"you chose {user_choice}\n")
    if user_choice==computer_choice:
        print("tie")
        
    elif user_choice=="rock":
        if computer_choice=="sisscors":
            print("you win")
        else:
            print('you lose')
    elif user_choice=="paper":
            if computer_choice=="rock":
                print("you win")
            else:
                print('you lose')
    elif user_choice=="sisscors":
            if computer_choice=="paper":
                print("you win")
            else:
                print('you lose')