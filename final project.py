import random

def player_choice():
    player_input = input("Which one you would love to pick <rock, paper or scissors>: ").lower()
    while player_input not in ["rock", "paper", "scissors"]:
        player_input = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return player_input

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def question_problem():
    questions = {
    "A mammal that has an ancute od smell and a barking.": "dog",
    "It is widely kept as a pet or for catching mice.": "cat",
    "a very large cat. When angry it's say roar.": "tiger",
    "a colorful bird feeding on fruits and seeds.\n"
    "Many are popular as able to mimic the human voice.": "parrot",
    "a large bird of prey with a massive hooked bill and long broad wings,\n"
    "known for its keen sight and powerful soaring flight.": "eagle",
    "a mammal which lives in the sea and looks like a large fish with a pointed mouth.\n"
    "It's like to stay near human": "dolphin"
    }
    print("What animal is it?")
    question, answer = random.choice(list(questions.items()))
    player_guess = input(f"{question}\nYour Guess: ").lower()  
    if player_guess == answer:
        print("Correct! You win!")
        try_again()
    else:
        print(f"Wrong! The correct answer was: {answer}")
        try_again()

def math_problem():
    math_symbols = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    random_math_symbol = random.choice(math_symbols)
    if random_math_symbol == '+':
        total = num1 + num2
    elif random_math_symbol == '-':
        total = num1 - num2
    elif random_math_symbol == '*':
        total = num1 * num2
    elif random_math_symbol == '/':
        total = num1 // num2
    print(f"Please solve this math problem {num1} {random_math_symbol} {num2}")
    player_math = int(input("Enter your answer here!!!"))
    if player_math == total:
        print("You pass ;D")
        try_again()
    else:
        print(f"Wrong answer -,- The answer is {total}")
        try_again()

def try_again():
    player_try_again = input("Do you want to keep going? (y/n): ").lower()
    if player_try_again == "y":
        game_running()
    elif player_try_again == "n":
        print("Bye Bye! see you next time")
        exit()
    else:
        print("I don't get it!\n"
            "You supposed to type (y/n)\n"
            "BYE!!!")
        exit()

def chose_problem():
    print("You have to solve one problem to continue Rock, Paper, Scissors\n"
          "I have two problem for you to chose\n"
          ">1< Math Problem\n"
          ">2< Guess The Animal"
    )
    player_problem = input("Which problem would you like to solve? (1/2)")
    if player_problem == "1":
        math_problem()
    elif player_problem == "2":
        question_problem()

def indentify_winner(get_player_choice, get_computer_choice):
    if get_player_choice == get_computer_choice:
        print("It's a tie!")
    elif get_player_choice == "rock" and get_computer_choice == "scissors":
        print("You win!")
    elif get_player_choice == "paper" and get_computer_choice == "rock":
        print("You win!")
    elif get_player_choice == "scissors" and get_computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!!! (-_-)")
        chose_problem()
    return " "

def game_running():
    playing = True
    while playing:
        get_player_choice = player_choice()
        get_computer_choice = computer_choice()
        print(f"You chose: {get_player_choice}")
        print(f"Computer chose: {get_computer_choice}")
        result = indentify_winner(get_player_choice, get_computer_choice)
        print(result)

print("Hello! Welcome to Rock, Paper, Scissors!")
game_running()