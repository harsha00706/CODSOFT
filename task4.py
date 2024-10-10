import random
def user_choice():
    choice=input("Enter your choice (rock, paper, scissors):").lower()
    while choice not in ["rock","paper","scissors"]:
        choice = input("Invaild input. Please choose either Rock, Paper or Scissors:").lower()
    return choice
def computer_choice():
    return random.choice(["rock","paper","scissors"])
def winner(user,comp):
    if user==comp:
        return "Its a tie!"
    elif (user=="rock" and comp=="scissors")or(user=="paper"and comp=="rock")or(user=="scissors"and comp=="paper"):
        return "You Win!"
    else:
        return "Computer Wins!"
def play_game():
    user_sc=0
    comp_sc=0
    round_no=1
    while True:
        print(f"Round {round_no}")
        user= user_choice()
        comp=computer_choice()
        print(f"You choose: {user}\n")
        print(f"Computer chooses: {comp}")
        result= winner(user,comp)
        print(result)
        if result == "You Win!":
            user_sc+=1
        elif result=="Computer Wins!":
            comp_sc+=1
        print(f"Current Scores: You-{user_sc}, Computer-{comp_sc}")
        again=input("\nDo you want to play again? (yes/no): ").lower()
        if again!="yes":
            print("End of the game!")
            break
        round_no+=1
if __name__=="__main__":
    print("Welcome to Rock, Paper and Scissors Game")
    print("The Instructions are: Type 'rock', 'paper' or 'scissor' To make your choice")
    play_game()