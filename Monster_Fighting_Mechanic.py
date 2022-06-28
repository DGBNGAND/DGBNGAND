import random
import time
c=0
starter=[]
class poke_attack:
    def __init__(self,att_name,att_power):
        self.att_name=att_name
        self.att_power=att_power
tackle=poke_attack('Tackle',(1,2,3))
scratch=poke_attack('Scratch',(1,2,3))
ember=poke_attack('Ember',(5,6,7))
razor_leaf=poke_attack('Razor Leaf',(5,6,7))
aqua_tail=poke_attack('Aqua Tail',(3,4,5))
class pokemon:
    def __init__(self,name,attack,health,description):
        self.name = name
        self.attack = attack
        self.health = health
        self.description=description
def fight(target,attack):
    target.health=target.health-attack
    return target   
charmander=pokemon('Charmander',5.2,39,'The flame that burns at the tip of its tail is an indication of its emotions.')
bulbasaur=pokemon('Bulbasaur',4.9,45,'Bulbasaur is a cute Pokémon born with a large seed firmly affixed to its back;\
the seed grows in size as the Pokémon does')
squirtle=pokemon('Squirtle',4.8,44,'Squirtles shell is not merely used for protection.\
The shells rounded shape and the grooves on its surface help minimize\n\
resistance in water,\
enabling this Pokémon to swim at high speeds.')
starter.append(charmander)
starter.append(bulbasaur)
starter.append(squirtle)
def game():
    print('Please choose from one of these pokemon:\n')
    print('[1] Charmander\n{}'.format(charmander.description))
    print('[2] Bulbasaur\n{}'.format(bulbasaur.description))
    print('[3] Squirtle\n{}\n'.format(squirtle.description))
    poke_choice=int(input('->'))
    valid=False
    while not valid:
        if poke_choice == 1:
            my_pokemon=pokemon('Charmander',5.2,39,'The flame that burns at the tip of its tail is an indication of its emotions.')
            valid=True
        elif poke_choice == 2:
            my_pokemon=bulbasaur
            valid=True
        elif poke_choice == 3:
            my_pokemon=squirtle
            valid=True
        else:
            continue
    enemy=random.choice(starter)
    battle(my_pokemon,enemy)
def battle(my_pokemon,enemy):
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
