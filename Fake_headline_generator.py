# Import random module
import random

# Create subjects

subjects = [
    "Amir khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "Prime Minister Modi",
    "A Group Of Munkey",
    "A Mumbai Cat",
    "Auto Driver from Delhi",
    "Osho Rajnish",
    "Aman",
]

actions =[
    "Lunches",
    "cancels",
    "dances with",
    "eats",
    "declares wars on",
    "hugs",
    "yoga teacher",
    "run the way",
    "frustation for work",
    "mind is very intaligent",
    "celebrates",
]

place_or_things = [
    "at Red Fort",
    "Mumbai local Train",
    "a plate of samosa",
    "during IPL match",
    "is beautfull girl",
    "on Mars mission",
    "inside a washing machine",
    "with a dancing robot",
    "at Parliament canteen",
    "in a Zoom call glitch",
    "wearing pajama suit",
    "behind the tea stall",
    "under mysterious UFO",
]

# start the headline generation  loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/no)").strip()
    if user_input == "no":
        break

# print Good bye messege
print("\nThanks for using the fake headline news generator.Have a fun day")    