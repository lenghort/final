import random

def question_problem():
    questions = {
    "A mammal that has an ancute od smell and a barking.": "dog",
    "a small mammal with soft fur and retracttable claws.It is widely kept as a pet or for catching mice.": "cat",
    "a very large cat with a yellow-brown coat striped with black.\n"
      "When angry it's say roar.": "tiger",
    "a colorful bird feeding on fruits and seeds Many are popular as able to mimic the human voice.": "parrot",
    "a large bird of prey with a massive hooked bill and long broad wings, known for its keen sight and powerful soaring flight.": "eagle",
    "a mammal which lives in the sea and looks like a large fish with a pointed mouth. It's like to stay near human": "dolphin"
    }
    print(questions.keys())

    print("Welcome to the Guessing Game!\n")

    question, answer = random.choice(list(questions.items()))

    user_guess = input(f"Question: {question}\nYour Guess: ").lower()
        
    if user_guess == answer:
        print("Correct! You win!")
    else:
        print(f"Wrong! The correct answer was: {answer}")

def game():
    option = ("rock", "paper", "scissors")
    playing = True

    while playing:
        player = None
        computer = random.choice(option)

        while player not in option:
            player = input("Enter a choice (rock, paper, scissors)")


        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!!!")
            question_problem()

# question_problem()
# player_try_again = input("Do you want to keep going? (y/n): ").lower()
# if player_try_again == "y":
#     print("hello")
# elif player_try_again == "n":
#     print("hi")
# else:
#     print("I don't get it!\n"
#           "You supposed to type (y/n)\n"
#           "BYE!!!")
#     exit() # hello

print("You lose!!! (-_-)\n"
      "You have to solve one problem to continue Rock, Paper, Scissors\n"
      "I have two problem for you to chose\n"
      ">1< Math Problem\n"
      ">2< Guess The Animal"
)
player_problem = input("Which problem would you like to solve? (1/2)")
if player_problem == "1":
    print("hi")
elif player_problem == "2":
    question_problem()