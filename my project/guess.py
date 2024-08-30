import random 


secret_number = random.randint(1,200)
guess_count = 0
guess_limit = 2
while guess_count<guess_limit:
    guess=int(input("guess: "))
    guess_count+=1
    if guess==secret_number:
        print("you won move to the next level")
    elif guess<secret_number:
        print(f"too low! the correct number was {secret_number} try again")
    elif guess>secret_number:
        print(f"too high! the correct number was {secret_number} try again with faith")
        break
    else:

        print("you failed try ")
