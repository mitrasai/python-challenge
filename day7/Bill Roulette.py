"""
Program which asks for names and select random name from the list of names. 
The person selected will have to pay for everbody's food bill.
"""

import random


def billRoulette():
    namesList = []
    num_people = int(input("How many people are participating? "))

    for i in range(num_people):
        name = input(f"Please enter person {i+1}'s name: ")
        namesList.append(name)

    print("Participants: ", namesList)

    chosen_one = random.choice(namesList)
    print(f"{chosen_one} is going to pay for the meal today!")


# billRoulette()


def billRoulette2():
    names_input = input("Please enter the names, separated by commas: ")
    namesList = names_input.split(",")
    
    num_items = len(namesList)
    random_index = random.randint(0, num_items-1)
    person_name = namesList[random_index]
    # chosen_one = random.choice(namesList)
    print(f"{person_name} is going to pay for the meal today!")


billRoulette2()
