# module import
import random

import pickle

from time import sleep

from random import choices


# player class
class player:
    def __init__(self, n="name", g=0, mnd=0, mxd=0, h=0, d=0):
        self.name = n
        self.gold = g
        self.mindamage = mnd
        self.maxdamage = mxd
        self.health = h
        self.defense = d


# inventory class
class inventory:
    def __init__(self, n="name", n1="name", n2="name",n3="name", n4="name" ):
        self.item1 = n
        self.item2 = n2
        self.item3 = n3
        self.item4 = n4


# item class
class item:
    def __init__(self, n="name", d="description", a1=0, a2=0, a3=0, u=1):
        self.name = n
        self.description = d
        self.damage = a1
        self.health = a2
        self.defense = a3
        self.uses = u


# enemie class
class enemie:
    def __init__(self, n="name", i="item", g=0, mnd=0, mxd=0, h=0, d=0):
        self.name = n
        self.item = i
        self.gold = g
        self.mindamage = mnd
        self.maxdamage = mxd
        self.health = h
        self.defense = d


sleep(1.0)

print("\n")

# name option(string)
namep = input('Enter your name: ')

# player stats generator
player1 = player(namep, 1, 1, random.randint(5, 30), 100)

action = -2

sleep(1.0)

print("\n")

# save ask
yOrN = input('load save?(only if you already played) y/n: ')


# save function
def save():
    pickle.dump([action, player1.maxdamage, player1.mindamage, player1.gold, player1.health, player1.defense],
    open("save.pi", "wb"))


# save load
if yOrN == "y":
    action, player1.maxdamage, player1.mindamage, player1.gold, player1.health, player1.defense = pickle.load(
    open("save.pi", "rb"))

# debug starter
if namep == "debug":
    action = int(input('actionValue: '))
    player1.maxdamage = int(input('maxDamage: '))
    player1.mindamage = int(input('minDamage: '))
    player1.gold = int(input('goldValue: '))
    player1.health = int(input('healthValue(100 recomended): '))
    player1.defense = int(input('defenseValue: '))


# functions
def playerStats():
    print("name        =", player1.name)
    print("gold        =", player1.gold)
    print("min damage  =", player1.mindamage)
    print("max damage  =", player1.maxdamage)
    print("health      =", player1.health)
    print("defense     =", player1.defense)


def randEneStat():
    print("name        =", enemieFight.name)
    print("gold        =", enemieFight.gold)
    print("min damage  =", enemieFight.mindamage)
    print("max damage  =", enemieFight.maxdamage)
    print("health      =", enemieFight.health)
    print("defense     =", enemieFight.defense)


def shop():
    # custom vars = actionChoose itemStat(1 to 4) itemPrice(1 to 4) and statsType(1 to 4)
    global action
    global actionChoose

    global itemName1
    global itemStat1
    global statType1
    global itemPrice1
    global statPlayer1

    global itemName2
    global itemStat2
    global statType2
    global itemPrice2
    global statPlayer2

    global itemName3
    global itemStat3
    global statType3
    global itemPrice3
    global statPlayer3

    global itemName4
    global itemStat4
    global statType4
    global itemPrice4
    global statPlayer4

    # shop loop
    while action > 4 and action < 6:
        sleep(1.0)

        print("\n")
        # action list(shop)
        print("1: Items")
        print("2: Equipment")
        print("3: Stats")
        print("4: Sell")
        print("5: Leave")

        sleep(1.0)

        print("\n")

        action = int(input("What do? : "))

        # item action
        if action == 1:
            sleep(1.0)

            print("")

        # equipament action
        while action > 1 and action < 3:
            sleep(1.0)

            print("\n")

            print("1:", itemName1, " (+", itemPlus1, "", statType1, ") --", itemPrice1, "gold")
            print("2:", itemName2, " (+", itemPlus2, "", statType2, ") --", itemPrice2, "gold")
            print("3:", itemName3, " (+", itemPlus3, "", statType3, ") --", itemPrice3, "gold")
            print("4:", itemName4, " (+", itemPlus4, "", statType4, ") --", itemPrice4, "gold")
            print("5: back")

            sleep(1.0)

            print("\n")

            action = int(input("What do? : "))

            if action == 1:
                sleep(1.0)

                print("\n")

                yOrN = input('sure y/n: ')

                if yOrN == "y":
                    if player1.gold >= itemPrice1:
                        setattr(player1, statPlayer1, itemStat1)

                        player1.gold = player1.gold - 5

                        action = actionChoose

                    else:
                        sleep(1.0)

                        print("\n")

                        print("not enough gold")

                        action = 2

                    sleep(1.0)

                    print("\n")

                    playerStats()

                else:
                    action = 2

            if action == 2:
                sleep(1.0)

                print("\n")

                yOrN = input('sure y/n: ')

                if yOrN == "y":

                    if player1.gold >= itemPrice2:
                        setattr(player1, statPlayer2, itemStat2)

                        player1.gold = player1.gold - itemPrice2

                        action = actionChoose

                    else:
                        sleep(1.0)

                        print("\n")

                        print("not enough gold")

                        action = 2

                    sleep(1.0)

                    print("\n")

                    playerStats()

                else:
                    action = 2

            if action == 3:
                sleep(1.0)

                print("\n")

                yOrN = input('sure y/n: ')

                if yOrN == "y":
                    if player1.gold >= itemPrice3:
                        setattr(player1, statPlayer3, itemStat3)

                        player1.gold = player1.gold - itemPrice3

                        action = actionChoose

                    else:
                        sleep(1.0)

                        print("\n")

                        print("not enough gold")

                        action = 2

                    sleep(1.0)

                    print("\n")

                    playerStats()

                else:
                    action = 2

            if action == 4:
                sleep(1.0)

                print("\n")

                yOrN = input('sure y/n: ')

                if yOrN == "y":

                    if player1.gold >= itemPrice4:
                        setattr(player1, statPlayer4, itemStat4)

                        player1.gold = player1.gold - itemPrice3

                        action = actionChoose

                    else:
                        sleep(1.0)

                        print("\n")

                        print("not enough gold")

                        action = 2

                    sleep(1.0)

                    print("\n")

                    playerStats()

                else:
                    action = 2

            if action == 5:
                action = actionChoose

        # sell stats action
        while action > 2 and action < 4:
            sleep(1.0)

            print("\n")

            print("1: Sell health")
            print("2: Sell Min damage")
            print("3: Sell Max damage")
            print("4: sell Defense")
            print("5: back")

            sleep(1.0)

            print("\n")

            action = int(input("What do? : "))
            # sell health
            if action == 1:
                sleep(1.0)

                print("\n")

                healthCheck = 0

                howMucHealth = int(input("How much health : "))

                # check if player not dead
                healthCheck = player1.health - howMucHealth

                if healthCheck > 1:

                    howMuchGold = 0

                    howMuchGold = howMucHealth * 30

                    player1.gold = player1.gold + howMuchGold

                    player1.health = player1.health - howMucHealth

                    action = 3

                    break

                else:
                    print("\n")

                    print("Thats not how you commit suicide")

                    action = 3

                break
            # sell min dmg
            if action == 2:
                sleep(1.0)

                print("\n")

                howMuchMiDamage = int(input("How much min damage : "))

                mindmgCheck = player1.health - howMuchMiDamage

                if mindmgCheck > 0:

                    howMuchGold = howMuchMiDamage * 50

                    player1.gold = player1.gold + howMuchGold

                    player1.mindamage = player1.mindamage - howMuchMiDamage

                    action = 3

                else:
                    sleep(1.0)

                    print("\n")

                    print("...")

                    action = 3

            # sell max dmg
            if action == 3:
                sleep(1.0)

                print("\n")

                howMuchMaDamage = int(input("How much max damage : "))

                maxdmgCheck = player1.health - howMuchMaDamage

                if maxdmgCheck > 1:

                    howMuchGold = howMuchMaDamage * 30

                    player1.gold = player1.gold + howMuchGold

                    player1.maxdamage = player1.maxdamage - howMuchMaDamage

                    action = 3 

                else:
                    sleep(1.0)

                    print("\n")

                    print("...")

                    action = 3

            # sell defense
            if action == 4:
                sleep(1.0)

                print("\n")

                howMuchDefense = int(input("How much defense : "))

                mindmgCheck = player1.health - howMuchDefense

                if mindmgCheck > 0:

                    howMuchGold = howMuchDefense * 30

                    player1.gold = player1.gold + howMuchGold

                    player1.defense = player1.defense - howMuchDefense

                    action = 3

                else:
                    sleep(1.0)

                    print("\n")

                    print("Baidu Antivirus.")

                    action = 3

            # back action
            if action == 5:
                action = 3

        if action == 4:
            print("")

        if action == 5:
            sleep(1.0)

            print("\n")

            print("You leave walmart™")

            action = actionChoose

            break

#item list
playerInv = inventory("none", "none", "none", "none")

def itemstats():

    Healthpotion = item(
    "Health Potion",
    "Gives you 10 points of health", 
    0,
    10,
    0,
    1)

    StackHealthpotion = item(
    "Health Potion Stack",
    "Gives you 10 points of health", 
    0,
    10,
    0,
    5)

    BigHealthpotion = item(
    "Big Health Potion",
    "Gives you 60 points of health", 
    0,
    10,
    0,
    1)

    StackBigHealthpotion = item(
    "Big Health Potion Stack",
    "Gives you 60 points of health", 
    0,
    60,
    0,
    5)

    StackBigHealthpotion = item(
    "Big Health Potion Stack",
    "Gives you 60 points of health", 
    0,
    60,
    0,
    5)

    RedPilled = item(
    "You're red pilled take this",
    "Gives you 10 points of defense", 
    0,
    0,
    10,
    1)

    Greanade = item(
    "Greanade",
    "Does 40 damage to the enemy", 
    0,
    40,
    0,
    1)

    HolyGreanade = item(
    "Greanade",
    "Does 1000 damage to the enemy", 
    0,
    1000,
    0,
    1)

    TrowingDagger = item(
    "Trowing Dagger",
    "Does 25 damage to the enemy", 
    0,
    25,
    0,
    1)

    TrowingDaggerStack = item(
    "Trowing Dagger Stack",
    "Does 25 damage to the enemy", 
    0,
    25,
    0,
    5)

    DildoGolden = item(
    "Dildo Gold(dom)",
    "Fucks everything up. Just like the usa",
    100000000000000,
    100000000000000,
    100000000000000,
    999999999999969
    )

# item shop
def itemshop():
    sleep(1.0)

    print("\n")

    print(playerInv.item1)
    print(playerInv.item2)
    print(playerInv.item3)
    print(playerInv.item4)

    selectinv = "item1"
    if playerInv.item1  == "none" or playerInv.item2  == "none" or playerInv.item3  == "none" or playerInv.item4  == "none":
        sleep(1.0)

        print("\n")

        print("Welcome to Walmart™ sir, I can see you got no items, what would you wnat?")
        
    if playerInv.item1  == "none" or playerInv.item2  == "none" or playerInv.item3  == "none" or playerInv.item4  == "none":
        sleep(1.0)

        print("\n")

        print("Welcome to Walmart™ sir, what would you want?") 

    sleep(1.0)

    print("\n")

    print("1: buy item slot 1")
    print("2: buy item slot 2")
    print("3: buy item slot 3")
    print("4: buy item slot 4")
    print("5: leave")

    action = int(input("What do? : "))
    
    if action == 1:
        sleep(1.0)

        print("\n")

    if action == 2:
        sleep(1.0)

        print("\n")

    if action == 3:
        sleep(1.0)

        print("\n")

    if action == 4:
        sleep(1.0)

        print("\n")

    if action == 5:
        sleep(1.0)

        print("\n")

        print("You leave Walmart™")

        action = actionChoose

# All the game choices are a especific action from 1 to 5
# All the game levels are a especific action from -... to 0 and 6 to ...

# action -2
while action > -3 and action < -1:
    # save
    save()

    sleep(1.0)

    print("\n")

    # stat list(player greeting)
    print("Hello", player1.name, "! You have", player1.gold, "gold, do", player1.mindamage, "min damage and",
          player1.maxdamage, "max damage.")

    sleep(1.0)

    print("\n")

    # stat list(again)
    playerStats()

    sleep(1.0)

    print("\n")

    print("The city of Homo Duro, isn't known for its life quality or safety,")
    print("but its sure as hell is known for being a shit hole full of")
    print("appreciator of 'soap droping boys' (young, dumb and have less ")
    print("experience with life, than politicians have with their wife's.)")
    print("They appreciate people like you")
    print(player1.name, "!")

    sleep(1.0)

    print("\n")

    # y/n action(select)
    yOrN = input('Continue? y/n: ')

    sleep(1.0)

    print("\n")

    # if yes (action 0 starter)
    if yOrN == "y":
        print("Finally someone want to play!")
        sleep(1.0)
        action = 0
    # if not yes
    else:
        # if no(end program)
        if yOrN == "n":
            sleep(1.0)

            print("\n")

            print("Fuck you, :(")

            sleep(1.0)

        # if not "no"
        else:
            yOrN = input('Wtf?! I just want to known y/n: ')
            sleep(1.0)

            # if yes(action 0 starter)
            if yOrN == "y":
                print("\n")
                print("Finally someone want to play!")
                sleep(1.0)
                action = 0
            # if not yes
            else:
                # if no(end program)
                if yOrN == "n":
                    sleep(1.0)

                    print("\n")

                    print("Fuck you then, :(")
                    sleep(1.0)
                # if not "no"(end program)
                else:
                    print("\n")
                    print("...")
                    sleep(1.0)

# action 0 loop
while action > -1 and action < 1:
    # save
    save()

    print("\n")

    print("You arrive in a tavern full of suspicious looking 'Rupers'")

    sleep(1.0)

    print("\n")

    # action list
    print("1: Walk away")
    print("2: Talk to the bartender")
    print("3: Say a racial slur(very bad)")

    sleep(1.0)

    print("\n")

    # action select
    action = int(input("What do? : "))

    # stop palyer form going above 3 actions
    if action > 3:
        action = 1

    sleep(1.0)

    # walk away action
    if action == 1:
        print("\n")

        print("You walk away. Wtf where you expecting?")

        sleep(1.0)

        print("\n")

        print("You go inside without knowing what were you doing")

        action = 0

    # bartender action(action -1 starter)
    if action == 2:
        print("\n")

        print("You walk to the bartender")

        sleep(1.0)

        action = -1

    # racial action
    if action == 3:

        print("\n")

        print("A bunch of Rupers got mad at you")
        print("(i warned your fucking racist ass).")
        print("Wtf were you thinking?")

        sleep(1.0)

        print("\n")

        print("You enter combat")

        sleep(1.0)

        print("\n")

        # stats
        playerStats()

        sleep(1.0)

        print("\n")

        print("name =        Bunch Of Mad Rupers", )
        print("min damage = ", 1.00)
        print("max damage = ", 999999999999999999)
        print("health =     ", 10000)

        sleep(1.0)

        print("\n")

        # action list
        print("1: Attack")
        print("2: Run away")
        print("3: Say sorry(very nice :) )")

        sleep(1.0)

        print("\n")

        # action select
        action = int(input("What do? : "))

        if action > 3:
            action = 1

        if action > 5:
            action = 1

        # attack action(incomplete)
        if action == 1:

            sleep(1.0)

            print("\n")

            print("You attack!")

            sleep(1.0)

            print("\n")

            damagesad = random.randint(player1.mindamage, player1.maxdamage)

            print("you deal", damagesad, "damage", "leaving the enemy with", 10000 - damagesad, "hp")

            sleep(1.0)

            print("\n")

            print("I gonna save you the trouble...")

            sleep(1.0)

            print("\n")

            deaths = ["You got annaly raped by a sjw and died",
                      "You got sued for racism and died of aids",
                      "You got imaginary banned from twitter and got sentenced to death(and aids)"]
            randomDeath = random.choice(deaths)
            print(randomDeath)

            sleep(1.0)

            print("\n")

            # restart action
            yOrN = input('Restart? y/n: ')

            if yOrN == "y":
                action = 0

        # try to run action
        if action == 2:
            sleep(1.0)

            print("\n")

            print("You failed and fall")

            sleep(1.0)

            print("\n")

            print("You are in a position called 'Soap boy'...")

            sleep(1.0)

            print("\n")

            print("Well...")

            sleep(1.0)

            print("\n")

            deaths = ["You got anally raped by a sjw and died",
                      "You got sued for racism and died of aids",
                      "You got imaginary banned from twitter and got sentenced to death(and aids)"]
            randomDeath = random.choice(deaths)
            print(randomDeath)

            sleep(1.0)

            print("\n")

            # restart action
            yOrN = input('Restart? y/n: ')

            if yOrN == "y":
                action = 0
        # sorrya action
        if action == 3:
            sleep(1.0)

            print("\n")

            print("You say sorry and...")

            sleep(3)

            print("\n")

            print("Dont work")

            sleep(1.0)

            print("\n")

            print("Last words?")

            sleep(1.0)

            print("\n")

            # y/n option(select)
            yOrN = input('Say racial slur? y/n: ')

            sleep(1.0)

            print("\n")

            # if yes
            if yOrN == "y":
                deaths = ["You got analy raped by a sjw and died. But you're based",
                          "You got sued for racism and died of aids. But you're based",
                          "You got imaginary banned from twitter and got sentenced to death(and aids). But you're based"]
                randomDeath = random.choice(deaths)
                print(randomDeath)

                sleep(1.0)

                print("\n")

                yOrN = input('Restart? y/n: ')

                if yOrN == "y":
                    action = 0
            # if not yes
            else:
                deaths = ["You got anally raped by a sjw and died. But you're not based",
                          "You got sued for racism and died of aids. But you're not based",
                          "You got imaginary banned from twitter and got sentenced to death(and aids). But you're not based"]
                randomDeath = random.choice(deaths)
                print(randomDeath)

                sleep(1.0)

                print("\n")

                # y/n action(select)
                yOrN = input('Restart? y/n: ')

                # if yes
                if yOrN == "y":
                    action = 0

# action -1 loop
while action > -2 and action < 0:
    # save
    save()

    # y/n option (select)
    print("\n")

    yOrN = input('He ask if you want to take a drink (- 1 gold) y/n: ')

    # if yes
    if yOrN == "y":
        sleep(1.0)

        print("\n")

        print("The bartender says with rage 'What is this?")
        print("Do you think a drink is that cheap? Are you")
        print("fucking retarded? This is such a disrespect")
        print("that i will keep your gold'")

        player1.gold = player1.gold - 1

        sleep(1.0)

        print("\n")

        print("-1 gold")

        sleep(1.0)

        print("\n")

        # stats
        playerStats()

        action = 6

        # if not yes
    else:
        sleep(1.0)

        print("\n")

        print("The bartender look at you and say 'That dude")
        print("just stole your gold'")

        sleep(1.0)

        print("\n")

        player1.gold = player1.gold - 1

        print("-1 gold")

        sleep(1.0)

        print("\n")

        # stats
        playerStats()

        action = 6

# action 6 loop
while action > 5 and action < 7:
    # save
    save()

    sleep(1.0)

    print("\n")

    print("Bartender ask 'something else'")

    sleep(1.0)

    print("\n")

    # action list
    print("1: Info")
    print("2: Fuck you")
    print("3: Leave")

    sleep(1.0)

    print("\n")

    # action select
    action = int(input("What do? : "))

    # stop palyer form going above 3 actions
    if action > 3:
        action = 1

    # info action
    if action == 1:
        sleep(1.0)

        print("\n")

        print("Bartender says You look like a 'soap boy'.")
        print("What such a young and retarded boy is doing")
        print("here in Homo Duro?'")

        sleep(1.0)

        print("\n")

        # action list
        print("1: Prostitution")
        print("2: You're fucking weird")
        print("3: Idk")

        sleep(1.0)

        print("\n")

        # action select
        action = int(input("What do? : "))

        # stop player from going above 3 actions
        if action > 3:
            action = 1

        # prostitution action
        if action == 1:
            sleep(1.0)

            print("\n")

            print("Bartender ask 'Would you tell my wife?'")

            sleep(1.0)

            print("\n")

            print("You have increased your combat level")

            sleep(1.0)

            print("\n")

            gainDMG = random.randint(1, 10)

            print("+", gainDMG, "max damage")

            player1.maxdamage = player1.maxdamage + gainDMG

            sleep(1.0)

            print("\n")

            # stats
            playerStats()

            sleep(1.0)

            print("\n")

            print("You leave")

            action = 7

        # weird action
        if action == 2:
            sleep(1.0)

            print("\n")

            print("Bartender says 'this city is weird'")

            action = 4

        # idk action(player is lazy)
        if action == 3:
            sleep(1.0)

            print("\n")

            print("You are the reason most RPG games sucks. Make a real decision you gormless minger")

            sleep(1.0)

            print("\n")

            print("Bartender says 'you're beyond than just a retard'")

            action = 6

        # action 4(neutral action)
        if action == 4:
            print("You say 'ok'")
            action = 6

    # being a dick action
    if action == 2:
        sleep(1.0)

        print("\n")

        # he really does
        print('#The player deserves this for being such a buffoon')

        sleep(1.0)

        print("\n")

        print("Fuck you too")

        action = 6

    # action leave (action 7 starter)
    if action == 3:
        sleep(1.0)

        print("\n")

        print("You say goodbye to the bartender and leave")

        action = 7

# action 7

# action 7 "counter variables"
enemiesLeft = 5
worksLeft = 5
begsLeft = 5

# loop start here
while action > 6 and action < 8:
    # save
    save()

    # action menu
    sleep(1.0)

    print("\n")

    print("You go to the tavern front door")

    sleep(1.0)

    print("\n")

    print("1: Talk to the weird dude on the tavern door")
    print("2: Fight a beggar")
    print("3: Sell your body")
    print("4: Beg")
    print("5: Go to walmart™")

    sleep(1.0)

    print("\n")

    # action select
    action = int(input("What do? : "))

    # stop player from going above 5 actions
    if action > 5:
        action = 1

    # boss fight action
    if action == 1:
        # boss stats
        boss1 = enemie("Utilmate Upper Class Non Beggar", "", 100, 1, 20, 50, 0)

        sleep(1.0)

        print("\n")

        print("The weird dude ask you to fill a form and before you say")
        print("anythinhg he push you into a comporation room.")

        sleep(1.0)

        print("\n")

        print("A wild corporate appear")

        action = 4

        # fight loop
        while action > 3 and action < 5:
            # boss health checker(action 8 starter)
            if boss1.health <= 0:
                sleep(1.0)

                print("\n")

                print("You killed the", boss1.name, "for money.", )

                # enemie gold reward
                player1.gold = player1.gold + boss1.gold

                sleep(1.0)

                print("\n")

                print("+", boss1.gold, "gold")

                action = 8

                break

            # player health checker
            if player1.health <= 0:
                sleep(1.0)

                print("\n")

                deaths = ["You should have begged for your recommendation",
                          "You met Jeffrey Epstein, faggot",
                          "You got sued for denying cookies(how could you?!"]
                randomDeath = random.choice(deaths)
                print(randomDeath)

                # gold lost on death
                deathLost = player1.gold * 0.15

                player1.gold = player1.gold - deathLost

                sleep(1.0)

                print("\n")

                print("You lost", deathLost, "Gold")

                sleep(1.0)

                print("\n")

                # stats
                playerStats()

                action = 7

                break

            sleep(1.0)

            print("\n")

            # stats board
            # stats
            playerStats()

            sleep(1.0)

            print("\n")

            print("name =       ", boss1.name)
            print("gold =       ", boss1.gold)
            print("min damage = ", boss1.mindamage)
            print("max damage = ", boss1.maxdamage)
            print("health =     ", boss1.health)

            sleep(1.0)

            print("\n")

            # action list
            print("1: Attack")
            print("2: Use item")
            print("3: Run away")

            sleep(1.0)

            print("\n")

            action = int(input("What do? : "))

            # stop player from going above 3 actions
            if action > 3:
                action = 1

            # attack action
            if action == 1:
                sleep(1.0)

                print("\n")

                attacks = ["You call him a bigot",
                           "You jizz in his logo",
                           "You show him the most sacred book 'James Charles wet dream'"]

                randomAttack = random.choice(attacks)

                print(randomAttack)

                pdamage = random.randint(player1.mindamage, player1.maxdamage)

                boss1.health = boss1.health - pdamage

                sleep(1.0)

                print("\n")

                print("That dealt", pdamage, "damage to him")

                edamage = random.randint(boss1.mindamage, boss1.maxdamage)

                player1.health = player1.health - edamage

                sleep(1.0)

                print("\n")

                attacks = ["The enemie ask for your opnion",
                           "The enemie ask for you to fill out a form",
                           "The enemie try to steal your data"]
                randomAttack = random.choice(attacks)
                print(randomAttack)

                sleep(1.0)

                print("\n")

                print("That dealt", edamage, "damage to you")

                action = 4

            # item action (icomplete)
            if action == 2:
                sleep(1.0)

                print("\n")

                print("You have no items")

                action = 4

            # escape action
            if action == 3:
                sleep(1.0)

                print("\n")

                print("You escaped this captalist Non Beggar")

                action = 7

    # fight action
    if action == 2:
        # enemies list
        enemie1 = enemie("Poor Beggar", "", random.randint(1, 2), 1,
                         random.randint(player1.maxdamage - 3, player1.maxdamage - 1), 30)
        enemie2 = enemie("Medium Class Beggar", "", random.randint(1, 4), 1,
                         random.randint(player1.maxdamage - 3, player1.maxdamage - 1), 30)
        enemie3 = enemie("Rich Beggar", "", random.randint(1, 7), 1,
                         random.randint(player1.maxdamage - 3, player1.maxdamage - 1), 30)
        enemie4 = enemie("Non Beggar", "", random.randint(1, 10), 1,
                         random.randint(player1.maxdamage - 3, player1.maxdamage - 1), 30)

        # enemie type choose random
        enemies = (enemie1, enemie2, enemie3, enemie4)
        enemieFight = random.choice(enemies)

        sleep(1.0)

        print("\n")

        print("A wild Beggar appears")

        action = 4

        # combat action loop
        while action > 3 and action < 5:
            # player health checker
            if player1.health <= 0:
                sleep(1.0)

                print("\n")

                deaths = ["You should have begged for your gold",
                          "You met Ellen DeGeneres and killed yourself(she is fucking mean)",
                          "You got sued for spanking a beggar(wtf are doing with your life)"]
                randomDeath = random.choice(deaths)
                print(randomDeath)

                deathLost = player1.gold * 0.15

                player1.gold = player1.gold - deathLost

                sleep(1.0)

                print("\n")

                print("You lost", deathLost, "Gold")

                sleep(1.0)

                print("\n")

                # stats
                playerStats()

                print("\n")

                yOrN = input('Restart? y/n:')

                # restart action

                # restart
                if yOrN == "y":
                    print("\n")

                    print("You got revived by the ROBLOX © mod (he thinks you're a pedophile)")

                    player1.health = 100

                # not restart
                else:
                    print("\n")

                    print("ok")

                    action = 999999999

                    break

                action = 7

                break
            
            # enemie health checker
            if enemieFight.health <= 0:
                sleep(1.0)

                print("\n")

                enemiesLeft = enemiesLeft - 1

                print("You killed a random", enemieFight.name, "for money.", )

                sleep(1.0)

                print("\n")

                print(enemiesLeft, "beggars left")

                # enemie gold reward
                player1.gold = player1.gold + enemieFight.gold

                sleep(1.0)

                print("\n")

                print("+", enemieFight.gold, "gold")

                action = 7

                break

            

                # enemie limit checker
            if enemiesLeft == 0:
                sleep(1.0)

                print("\n")

                print("No beggars left. You killed the entire population like damn")

                action = 7

                break

            sleep(1.0)

            print("\n")

            # stats board
            playerStats()

            sleep(1.0)

            print("\n")

            # enemie stats
            randEneStat()

            sleep(1.0)

            print("\n")

            # action list
            print("1: Attack")
            print("2: Use item")
            print("3: Run away")

            sleep(1.0)

            print("\n")

            action = int(input("What do? : "))

            # stop player from going above 3 actions
            if action > 3:
                action = 1

            # attack action
            if action == 1:
                sleep(1.0)

                print("\n")

                attacks = ["You call him a faggot", "You jizz in his face",
                           "You show him the most sacred book 'Zabiba and the King'"]
                randomAttack = random.choice(attacks)
                print(randomAttack)

                pdamage = random.randint(player1.mindamage, player1.maxdamage)

                enemieFight.health = enemieFight.health - pdamage

                sleep(1.0)

                print("\n")

                print("That dealt", pdamage, "damage to him")

                edamage = random.randint(enemieFight.mindamage, enemieFight.maxdamage)

                player1.health = player1.health - edamage

                sleep(1.0)

                print("\n")

                attacks = ["The enemie ask for money", "The enemie ask for you to jizz on his face",
                           "The enemie try to steal your gold"]
                randomAttack = random.choice(attacks)
                print(randomAttack)

                sleep(1.0)

                print("\n")

                print("That dealt", edamage, "damage to you")

                action = 4

            # item action (icomplete)
            if action == 2:
                sleep(1.0)

                print("\n")

                print("You have no items")

                action = 4

            # escape action
            if action == 3:
                sleep(1.0)

                print("\n")

                print("You escaped")

                action = 7

    # work loop
    while action > 2 and action < 4:
        # work limit checker
        if worksLeft == 0:
            sleep(1.0)

            print("\n")

            print("No works left. You're a fucking 'WorkCuck'")

            action = 7

            break

        # work action
        sleep(1.0)

        print("\n")

        works = ["A random ruper lick your awful toe. Do you even clean it?",
                 "A random ruper ask you to clean his house and try to calm his wife",
                 "A random ruper ask you to kill a debtor (very sexy)",
                 "A random ruper ask you to do an abortion",
                 "A random ruper ask you to eat a weird package and cross the border",
                 "A random ruper ask you to call someone a rupla (U got beat up bad)"]

        randomWork = random.choice(works)
        print(randomWork)

        gotGold = random.randint(1, 10)

        player1.gold = player1.gold + gotGold

        sleep(1.0)

        print("\n")

        print("+", gotGold, "gold")

        worksLeft = worksLeft - 1

        sleep(1.0)

        print("\n")

        print(worksLeft, "works left")

        action = 7

    # beg loop
    while action > 3 and action < 5:
        # beg limit checker
        if begsLeft == 0:
            sleep(1.0)

            print("\n")

            print("No begs left. Stop being a leech, your not even THAT poor")

            action = 7

            break

        # beg action
        sleep(1.0)

        print("\n")

        begs = ["You asked David Baszucki for child money",
                "You asked a beggar for money",
                "You asked a ruper to give you good time",
                "You gave up and stole a drunk illegal immigrant",
                "You searched a hospital trash can(it hurst when you pee)",
                "You found a pendrive with a image and a code(Worth money i guess?)"]
        randomBeg = random.choice(begs)
        print(randomBeg)

        gotGold = random.randint(0, 2)

        # Got gold? checker
        if gotGold == 0:
            sleep(1.0)

            print("\n")

            print("Nothing :(")

            action = 7

            break

        # beg action continuation
        player1.gold = player1.gold + gotGold

        sleep(1.0)

        print("\n")

        print("+", gotGold, "gold")

        begsLeft = begsLeft - 1

        sleep(1.0)

        print("\n")

        print(begsLeft, "begs left")

        action = 7

    # shop action
    while action > 4 and action < 6:
        # shop equipament list
        actionChoose = 7

        itemName1 = "used condom"
        itemStat1 = player1.defense + 3
        itemPlus1 = 3
        statType1 = "defense"
        statPlayer1 = "defense"
        itemPrice1 = 5

        itemName2 = "medieval glock 18"
        itemStat2 = player1.maxdamage + 3
        itemPlus2 = 3
        statType2 = "max dmg"
        statPlayer2 = "maxdamage"
        itemPrice2 = 3

        itemName3 = "insurance scam"
        itemStat3 = player1.mindamage + 3
        itemPlus3 = 3
        statType3 = "min dmg"
        statPlayer3 = "mindamage"
        itemPrice3 = 5

        itemName4 = "tail boner pad"
        itemStat4 = player1.defense + 3
        itemPlus4 = 3
        statType4 = "defense"
        statPlayer4 = "defense"
        itemPrice4 = 5

        # start shop
        shop()
