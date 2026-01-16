import random

low_limit=1
high_limit=100
random_number=random.randint(low_limit,high_limit)
print(random_number)
guess_count=0

guess=int(input("Enter a guess between 1 and 100:"))

while True:
    guess_count+=1
    if guess != random_number:
        print("wrong!Please try again.")
        guess=int(input("Enter the number again:"))
    if guess==random_number:
        print(f"You are correct! {guess} is the random number.")
        break
