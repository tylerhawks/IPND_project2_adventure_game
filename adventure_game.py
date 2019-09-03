import time
import random


def play_game():
    inventory = []
    intro(inventory)


def print_pause(message):
    print(message)
    time.sleep(1.5)


# Set the scene
def intro(inventory):
    print_pause("It is the early 18th century and you are a poor fisherman "
                "struggling to get by in a bustling Mediterranean port city")
    print_pause("Tired of the struggles of trying to keep up with the "
                "increasing costs of the ever-growing city.")
    print_pause("You decide to seek a spot on a crew of enterprising young "
                "sailors of rather ill repute.")
    print_pause("Okay yes; they're pirates. But they're wealthy pirates.")
    print_pause("In order to join them you must prove your value.")
    print_pause("They tell you that you must steal a crate of rum from a "
                "shipment that has just come into port")
    select_item(inventory)
    docks(inventory)


# Check for valid input
def validate(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response


# Ask player to make a choice
def choose():
    response = validate("Please enter 1 or 2\n",
                        ["1", "2"])
    return response


# Have the player chosse an item to use in the game
def select_item(inventory):
    print_pause("You can take one piece of equipment with you")
    print_pause("Do you take \n1) A dagger\n2) A length of rope")
    response = choose()
    if response == "1":
        print_pause("You take the dagger with you on your mission.")
        inventory.append("dagger")
    else:
        print_pause("You take the rope with you on your mission.")
        inventory.append("rope")


# playout the scenarios at the dock area
def docks(inventory):
    # randomize the number of guards
    gaurds = random.choice(["a single gaurd", "two guards"])
    print_pause("You wait for nightfall and approach the docks")
    print_pause(f"The ship is being watched by {gaurds}")
    # single gaurd scenarios
    if "single" in gaurds:
        print_pause("Do you \n1) Sneak past the gaurd\n2) Fight the guard")
        response = choose()
        if response == "1":
            if "rope" in inventory:
                print_pause("You successfully sneak past the guard.")
                print_pause("You use the rope to lower the crate into the "
                            "water, and float it to the priates ship.")
                victory()
            else:
                print_pause("You drop the crate into the water, but the "
                            "gaurd hears you.")
                print_pause("You try to fight him off, but he is well "
                            "trained, and better armed.")
                print_pause("You are quickly defeated and thrown in prison. "
                            "You are to be hanged in the morning")
                play_again()
        else:
            print_pause("You approach the lone sentry while he is looking "
                        "the other direction")
            if "dagger" in inventory:
                print_pause("You quickly take him down with your dagger "
                            "before he knows what is happening")
                print_pause("You load the crate into the life raft and row "
                            "it to the pirates ship")
                victory()
            else:
                print_pause("You attack with all your might, but he is well "
                            "trained, and better armed.")
                print_pause("You are quickly defeated and thrown in prison. "
                            "You are to be hanged in the morning")
                play_again()
    # two gaurd scenarios
    else:
        print_pause("You cannot sneak past both gaurds without being spotted.")
        print_pause("Do you\n"
                    "1) Take them on in a fight\n"
                    "2) Attemp to create a diversion")
        response = choose()
        if response == "1":
            if "dagger" in inventory:
                print_pause("You rush the gaurds and manage to take the first "
                            "one down quickly, but with the element of "
                            "surprise no longer on your side, you are easily "
                            "defeated by the second gaurd")
                print_pause("You have been mortally wounded and have only "
                            "moments to reflect on your poor choices before "
                            "passing away")
                play_again()
            else:
                print_pause("You attack with all your might, but they are "
                            "well trained, and better armed.")
                print_pause("You are quickly defeated and thrown in prison. "
                            "You are to be hanged in the morning")
                play_again()
        else:
            if "dagger" in inventory:
                print_pause("You spot a carraige coming down the road.")
                print_pause("As it's passing by you attemp to jam the wheel "
                            "with you dagger.")
                print_pause("Instead the horse veers unexpectedly; crushing "
                            "your leg.")
                print_pause("You are crippled and unable to work. You starve "
                            "to death that winter.")
                play_again()
            else:
                print_pause("You use the rope to set up a trip wire on the "
                            "road.")
                print_pause("When a horse-drawn carraige stumbles into your "
                            "trap and topples over, the guards run to "
                            "investigate.")
                print_pause("You use this opportunity to sneak aboard the "
                            "ship and quickly escape with the crate")
                victory()


# display victory message and ask player if they want to play again
def victory():
    print_pause("Congratulatons! You are victorious")
    play_again()


# present player with option to play again
def play_again():
    response = validate("Would you like to play again? (y/n)\n",
                        ["y", "n"])
    if "y" in response:
        play_game()
    else:
        print_pause("Goodbye")


play_game()
