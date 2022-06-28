import random
import time
c=0
starter=[]
class monster_attack:
    def __init__(self,att_name,att_power):
        self.att_name=att_name
        self.att_power=att_power
bodyslam=monster_attack('Body Slam',(1,2,3))
scratch=monster_attack('Scratch',(1,2,3))
burn=monster_attack('Burn',(5,6,7))
bloom=monster_attack('Bloom',(5,6,7))
water_slap=poke_attack('Water Slap',(3,4,5))
class monster:
    def __init__(self,name,attack,health,description):
        self.name = name
        self.attack = attack
        self.health = health
        self.description=description
def fight(target,attack):
    target.health=target.health-attack
    return target   
FlameBoy=monster('Flame Boy',5.2,39,'Fire Type Monster')
LeafGuy=monster('Leaf Guy',4.9,45,'Leaf Type Monster')
WaterDude=monster('Water Dude',4.8,44,'Water Type Monster')
starter.append(FlameBoy)
starter.append(LeafGuy)
starter.append(WaterDude)
def game():
    print('Please choose from one of these pokemon:\n')
    print('[1] Charmander\n{}'.format(FlameBoy.description))
    print('[2] Bulbasaur\n{}'.format(LeafGuy.description))
    print('[3] Squirtle\n{}\n'.format(WaterDude.description))
    monster_choice=int(input('->'))
    valid=False
    while not valid:
        if monster_choice == 1:
            my_monster=FlameBoy
            valid=True
        elif poke_choice == 2:
            my_pokemon=LeafGuy
            valid=True
        elif poke_choice == 3:
            my_pokemon= WaterDude
            valid=True
        else:
            continue
    enemy=random.choice(starter)
    battle(my_monster,enemy)
def battle(my_monster,enemy):
    dead=False
    print('A wild {0} appeared!'.format(enemy.name))
    print('What do you choose to do :')
    while not dead:
        print('\n{}(Enemy)      HP:{}\n'.format(enemy.name,enemy.health))
        print('{}               HP:{}\n\n'.format(my_pokemon.name,my_pokemon.health))
        if my_pokemon.name=='Charmander':
            print('[1] Scratch\n[2] Ember')
            move_choice=int(input('->'))
            if move_choice==1:
                print('\n{} used {}!'.format(my_pokemon.name,scratch.att_name))
                time.sleep(1)
                fight(enemy,random.choice(scratch.att_power))
            elif move_choice==2:
                print('\n{} used {}!'.format(my_pokemon.name,ember.att_name))
                time.sleep(1)
                fight(enemy,random.choice(ember.att_power))
        elif my_pokemon.name=='Bulbasaur':
            print('[1] Tackle\n[2] Razor Leaf')
            move_choice=int(input())
            if move_choice==1:
                print('\n{} used {}!'.format(my_pokemon.name,tackle.att_name))
                time.sleep(1)
                fight(enemy,random.choice(tackle.att_power))
            elif move_choice==2:
                print('\n{} used {}!'.format(my_pokemon.name,razor_leaf.att_name))
                time.sleep(1)
                fight(enemy,random.choice(razor_leaf.att_power))
        elif my_pokemon.name=='Squirtle':
            print('[1] Tackle\n[2] Aqua Tail')
            move_choice=int(input())
            if move_choice==1:
                print('\n{} used {}!'.format(my_pokemon.name,tackle.att_name))
                time.sleep(1)
                fight(enemy,random.choice(tackle.att_power))
            elif move_choice==2:
                print('\n{} used {}!'.format(my_pokemon.name,aqua_tail.att_name))
                time.sleep(1)
                fight(enemy,random.choice(aqua_tail.att_power))
        time.sleep(1)
        c=random.randint(1,2)
        if c == 1:
            fight(my_pokemon,random.choice(tackle.att_power))
        elif c==2:
            fight(my_pokemon,6)
        time.sleep(1)
        if enemy.health<=0 or my_pokemon.health<=0:
            dead=True
            time.sleep(1)
            print('It was a critical hit!')
            print('Foe {} was defeated!'.format(enemy.name))
game()
