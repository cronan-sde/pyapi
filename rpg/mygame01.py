#!/usr/bin/python3

import random as rand

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]

Win by making it to the Garden with key and potion in hand,
but beware of monsters lurking in the shadows...
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#function for combat
#user battles monster
def combat():
    user_health = 100
    monster_health = 100

    while True:
        #allow user to attack or defend
        if choose_atk_def() == 'a':
            user_dmg = user_atk()
            monster_health -= user_dmg
            print(f"You swing your mighty fist and caused {user_dmg} damage to the monster")
            if monster_health <= 0:
                break
            monst_dmg = monster_atk()
            user_health -= monst_dmg
            print(f"The monster strikes back causing {monst_dmg} damage to you\n")
            if user_health <= 0:
                break
        #user blocked    
        else:
            monst_dmg = user_blk() 
            user_health -= monst_dmg
            print(f"You have chosen to block, monster takes a swipe at you and caused {monst_dmg} damage")
            if user_health <= 0:
                break
            #blocking deals 50% of damage dealt by monster
            dmgToMonst = monst_dmg * 0.5
            monster_health -= dmgToMonst
            print(f"You're block has casued {dmgToMonst} damage to the monster\n")
            if monster_health <= 0:
                break
        print(f"user health {user_health}, monster {monster_health}")

    #check who lived
    survivor = "user" if user_health > 0 else "monster"
    return survivor


#allow user to choose wheter to block or atck
def choose_atk_def():
    atkOrDef = ''
    while True:
        print("Would you like to attack or block? type (a or b)")
        choice = input(">> ").strip().lower()
        if choice == 'a':
            atkOrDef = choice
            break
        elif choice == 'b':
            atkOrDef = choice
            break
        else:
            print(f"{choice} is not a valid option")

    return atkOrDef

#user attack function
def user_atk():
    dmg = 0
    dmg = rand.randint(1, 35)
    return dmg

#monster attack function
def monster_atk():
    dmg = rand.randint(5, 35)
    return dmg

#blocked attack
#when user blocks they avoid 50% of attack damage
def user_blk():
    dmg = monster_atk()
    dmg /= 2
    return dmg

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
             },
            'Garden' : {
                  'north': 'Dining Room'
             }
          }


#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  ## If a player enters a room with a monster
  if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'monster':
    print("Oh no a monster! You must fight for your life")  
    survivor = combat()
    if survivor == 'monster':
        print("The monster has devoured you!\nGame Over...")
        break
    else:
        rooms[currentRoom]['item'] = 'dead monster'
    print("You have vanquished the monster! Continue on your quest to escape")
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

