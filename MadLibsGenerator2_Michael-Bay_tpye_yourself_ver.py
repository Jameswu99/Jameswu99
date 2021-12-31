""" Mad Libs Generator 2 Michael Bay
----------------------------------------
"""
while True:
    man_name = input("Name a man's name: ")
    occupation = input("Choose a occupation: ")
    noun = input("Choose a noun: ")
    noun2 = input("Choose a noun: ")
    noun3 = input("Choose a noun: ")
    shape = input("Choose a shape: ")
    verb = input("Choose a verb: ")
    woman_name = input("Choose a woman's name: ")
    body_part = input("Choose a body part: ")
    verb2 = input("Choose a verb: ")
    noun4 = input("Choose a noun: ")
    noun5 = input("Choose a noun: ")
    restaurant_name = input("Choose a restaurant's name: ")
    historic_monument = input("Choose a historic monument: ")
    verb3 = input("Choose a verb: ")
    noun6 = input("Choose a noun: ")
    noun7 = input("Choose a noun: ")
    verb4 = input("Choose a verb: ")
    noun8 = input("Choose a noun: ")
    adjective = input("Choose an adjective (Describing word): ")
    adjective2 = input("Choose an adjective (Describing word): ")
    emotion = input("Choose an emotion: ")
    ving = input("Choose a present tense verb: ")
    noun9 = input("Choose a noun: ")
    noun10 = input("Choose a noun: ")
    verb5 = input("Choose a verb: ")
    print("------------------------------------------")
    print(man_name, "is a normal", occupation, ".")
    print("Then one day, a", noun, "explodes, causing a", noun2, "to blow up, and a nearby", noun3, "erupts into a",
          shape, "of flames.")
    print(man_name, "realizes that he's being chased by the government, who's trying to", verb, "him.")
    print("While on the run , he teams up with an incredibly attractive woman named", woman_name,
          ", who has an incredible", body_part, ".")
    print("She may be from the streets, but she can", verb2, "like nobody's business.")
    print("The duo decide to turn the tables on their pursuers by blowing up a", noun4,
          ", which triggers a chain reaction, causing the local " + noun5 + ", " + restaurant_name, ", and the",
          historic_monument, "to explode.")
    print("Then, the bad guys' helicopter gets", verb3, "by a piece of", noun6, "from when the", noun5,
          "exploded, and the helicopter explodes and falls onto a", noun7 + ", causing it to",
          verb4 + ", which shoots a fireball straight into the heart of", noun8, "and destroys the bad guy leader.")
    print("Everything is", adjective, "and the two decide that such a", adjective2, "ordeal has caused them to fall in",
          emotion, "with each other.")
    print("They decide to celebrate by", ving, "on the", noun9 + "and they even managed to use a", noun10,
          "from the beginning of the movie, to", verb5, "the whole story together.")
    print("------------------------------------------")
    attitude = input('Do you want to do it again(y for yes and n for no):')
    if attitude == 'n':
        break
