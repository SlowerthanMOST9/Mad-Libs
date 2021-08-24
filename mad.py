plural_noun = input("Enter a plural noun: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
color = input("Enter a color: ")
noun2 = input("Enter a noun: ")
plant = input("input a plant: ")
name = input("Enter a name: ")
name2 = input("Enter a name: ")
adjective3 = input("Enter an adjective: ")


def story_one():
    print("There once were " + plural_noun)
    print("They were hit by a " + noun)
    print("Now they are " + adjective)
    print("But will always " + adjective2 + "on")

def story_two():
    print(noun2 + "are" + color)
    print(plant + "are blue")
    print("my name is" + name + "How are you?")

def story_three():
    print(name2 + "is really cool")
    print("they will never " + adjective3)

import random

my_list = [story_one, story_two, story_three]
random.choice(my_list)()