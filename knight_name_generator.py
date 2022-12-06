#Knight Name Generator
import random

def knightNameGenerator():
  firstnames = ["Lancelot","Charles","Henry","William","James","Richard","Edward"]
  nicknames = ["Brave","Horrific","Courageous","Terrific","Fair","Conqueror","Victorious","Glorious","Invicible"]

  firstname = random.choice(firstnames)
  nickname =  random.choice(nicknames)

  return f'{firstname} The {nickname}'

def generatecoatofarm():
  colours = ["Red","Golden","Blue","Purple","White","Silver"]
  animals = ["Lion","Dragon","Unicorn","Horse","Tiger"]

  colour = (random.choices(colours, k=2))
  animal = random.choice(animals)

  colo_2 = colour[0] if colour[0] == colour[1] else ' '.join(colour)
  return f'Your coat of arm is {colo_2} {animal}'

def generateweapon():
  weapons = ['iron mace', 'golden flail', 'silver axe', 'silver sword', 'wooden shield', 'silver spade', 'metal shield']

  weapon = random.choice(weapons)
  return f'your favourite weapon is {weapon}'

def generatequality():
  qualities = ['courageous', 'merciful', 'judicial', 'peaceful', 'generous', 'noble', 'faithful', 'Hopeful','loyal', 'combative']

  quality = ' And '.join(random.sample(qualities, k=2))
  return f'You\'re {quality}'

def generatehouse():
  houses = ['haunted castle', 'hidden mansion', 'fortified tower', 'castle rock', 'dragon stone', 'winter fell']
  
  house = random.choice(houses)
  return f'You live in {house}'

player1 = knightNameGenerator()
print("Player 1: Your name is: " + player1)

player1 = generatecoatofarm()
print(player1)

player1 = generateweapon()
print(player1)

player1 = generatequality()
print(player1)

player1 = generatehouse()
print(player1)

print('\n')

player2 = knightNameGenerator()
print("Player 2: Your name is: " + player2)

player2 = generatecoatofarm()
print(player2)

player2 = generateweapon()
print(player2)

player2 = generatequality()
print(player2)

player2 = generatehouse()
print(player2)


