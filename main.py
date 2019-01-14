from lib.CheapSlime import CheapSlime

slime_types = ["Cheap slime", "Mediocre slime (Unavaliable)", "Epic slime (Unavaliable)"]

def intro():
    print("Welcome the official AvinoamCo's Slime store!")
    print("We have a very large variety of slimes:", end=" ")
    
    for i, slime_type in enumerate(slime_types):
        print(slime_type, end="")
        if i < len(slime_types) - 1:
            print(end=", ")

    print()
    choose_slime()
    
def choose_slime():
    did_choose = False
    slime = None
    
    while did_choose == False:
        slime_type = input("Which one would you like? ")
        if slime_type.lower() == "cheap slime":
            print("Great choice!")
            print("* Cheap slime is given *")
            print("Have fun!")
            slime = CheapSlime()
            did_choose = True
        else:
            print("We don't have this kind of slime, please choose another one")
    print("* Leaving store *")

    to_try = input("Would you like to try your slime? ")
    if to_try.lower() == "yes" or to_try.lower() == "y":
        print("Great!")
    elif to_try.lower() == "no" or to_try.lower() == "n":
        print("That wasn't a question, you *will* play with your slime and you *will* enjoy.")
        print("Anyways", end=", ")
    else:
        print("I didn't understand your answer so I'll take it as a yes.")
    use_slime(slime)

def use_slime(slime):
    while True:
        activity = input("what would you like to do with your slime? ")

        slime.do(activity.lower())

intro()