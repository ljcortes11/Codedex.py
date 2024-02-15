import random

class Player:
    def __init__(self, ID, health, attack, block):
        self.ID = ID
        self.health = health
        self.attack = attack
        self.block = block

def pvp(player_1, player_2):
    random_number = random.randint(1, 10)
    if random_number == 4:
        print(f"Luis lost HP {player_1.health} - You lost 50%")
        player_1.health -= 50
             
        print(f"random number: {random_number}")
   
    elif random_number == 5:
        print(f"Mat has Health bar {player_2.health} - You lost 50%")
        player_2.health -= 50
        print(f"random number: {random_number}")

    elif random_number == 6:
        print(f"Mat has Health bar {player_2.health} - You lost 50%")
        print(f"random number: {random_number}")
    
    elif random_number == 7:
        print(f"Luis has block with a shield pressing bottom {player_1.block} from and attack from Mat")
        print(f"random number: {random_number}")
    
    elif random_number == 8:
        print(f"Mat has attack Luis with a spear pressing the bottom {player_2.attack}  Mat shielded him self")
        print(f"random number: {random_number}")
    
    elif random_number == 9:
        print(f"Luis has HP went down {player_1.health} Mat killed him")
        player_1.health -= 100
        print(f"random number: {random_number}")
    
    elif random_number == 10:
        print(f"Mat has HP went Down {player_2.health} Mat has died Luis killed him ")
        player_2.health -= 100
        print(f"random number: {random_number}")

    else:
        print("Try again")
        print(f"random number: {random_number}")
    

Luis = Player(1, 100, 'A', 'B')
Mat = Player(2, 100, 'a', 'b')

pvp(Luis,Mat)

print(f"Initial status:")
print(f"Luis: {vars(Luis)}")
print(f"Mat: {vars(Mat)}")





print(f"Updated status:")
print(f"Luis: {vars(Luis)}")
print(f"Mat: {vars(Mat)}")
