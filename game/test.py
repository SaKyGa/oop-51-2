
# import time

# import random

# def play_game():
#     number_to_guess = random.randint(1, 100)
#     attempts = 0
#     print("Welcome to the Number Guessing Game!")
#     print("I have selected a number between 1 and 100. Can you guess what it is?")

#     while True:
#         try:
#             guess = int(input("Enter your guess: "))
#             attempts += 1

#             if guess < number_to_guess:
#                 print("Too low! Try again.")
#             elif guess > number_to_guess:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

# if __name__ == "__main__":
#     play_game()


# def track_time():
#     start_time = time.time()
#     input("Press Enter to stop the timer...")
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"You spent {elapsed_time:.2f} seconds.")

# if __name__ == "__main__":
#     track_time()

