'''A program to randomly generate knight info including name, house, weapon and coat of arms'''

import random
def knight_info():
    firstnames = ["Lancelot","Charles","Henry","William","James","Richard","Edward", 'John', 'Dranerys', 'Dickson', 'Jamie', 'Cersei']
    lastnames = ['Snow', 'Lannister', 'Targerion', 'Tarly', 'Greyjoy', 'Baylish', 'Frey', 'Baratheon', 'Stark', 'Tyrell', 'Greyjon', 'Strong', 'Velaryon']
    colours = ["Red","Golden","Blue","Purple","White","Silver", 'Black', 'Green', 'Yellow']
    animals = ["Lion","Dragon","Unicorn","Horse","Tiger", "Wolf", 'Cat', 'Fox', 'Hyenna']
    weapons = ['iron mace', 'golden flail', 'silver axe', 'silver sword', 'wooden shield', 'silver spade', 'metal shield']
    attributes = ['courageous', 'merciful', 'judicial', 'peaceful', 'generous', 'noble', 'faithful', 'Hopeful','loyal', 'combative', "Brave","Horrific","Terrific","Fair","Conqueror","Victorious","Glorious","Invicible"]
    houses = ['Haunted castle', 'Hidden mansion', 'Fortified tower', 'Castle rock', 'Dragon stone', 'Winter fell', 'Hightower', 'Black water']

    firstname = random.choice(firstnames)
    lastname =  random.choice(lastnames)
    colour = random.choices(colours, k=2)
    color = colour[0] if colour[0]==colour[1] else ' '.join(colour)
    animal = random.choice(animals)
    weapon = random.choice(weapons)
    attribute = ' And '.join(random.sample(attributes, k=2))
    house = random.choice(houses)

    return f'Your name is {firstname}, {lastname}. \nYour coat of arm is {color} {animal}. \nYour weapon is {weapon}. \nYou\'re {attribute}. \nYou live in {house}'
info = knight_info()
print('Player 1: ', info,)
print('\n') 
print('Player 2: ', info)





















