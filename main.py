import pokemonData
import random

listloop = True
guessloop = True


def decaps(capitalized):
    caps = {
"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,"K":11,"L":12,"M":13,
"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,
 }
    lowcase = {
"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,"k":11,"l":12,"m":13,
"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,
 } 
    approved_letters = [
    ]
    list_capitalized = list(capitalized)
    for letter in list_capitalized:
        list_caps = list(caps) 
        if letter in list_caps:            
            cap_key = caps[letter]#turns A to 1           
            for key, value in lowcase.items():
                if cap_key == value:
                    lowcaseletter = key   # turn 1 to a
                    approved_letters.append(lowcaseletter)
                    break
        else: 
            approved_letters.append(letter)
    decapitalized = ''.join(approved_letters)
    return decapitalized


def guess():
    guess = input("What's your guess? ")
    print("")
    if guess in  random_type_pokemon:
                print("Correct!")
                random_type_pokemon.remove(guess)
                print(random_type_pokemon)
                if len(random_type_pokemon) == 0:
                    print("You got all the pokemon!") 
                    break #finished list
                else: 
                    print(f"You have {len(random_type_pokemon)} {random_type_combo} type pokemon left")
                    continue #still guessing
            else: 
                print(f"That is not a {random_type_combo} type pokemon!")
                continue


def hint(random_type_pokemon): 
    hint_type = decaps(input("What type of hint do you want (Gen, Legendary, Form) "))
    Gen_hints = []
    Legendary_hints = []
    form_hints = []
    for pokemon in random_type_pokemon:
        pokemon_hints_list = pokemonData.pokemondic[pokemon]
        Gen_hints.append(pokemon_hints_list[0])
        Legendary_hints.append(pokemon_hints_list[1])
        form_hints.append(pokemon_hints_list[2])
    if hint_type == "gen":
        for index, gen in enumerate(Gen_hints, start=1):
            print(f"Pokemon {index} is in gen {gen}")

    elif hint_type == "Legendary":
        for index, legendary in enumerate(Gen_hints, start=1):
            print(f"Pokemon {index} is in gen {legendary}")

    elif hint_type == "form":
        for index, legendary in enumerate(Gen_hints, start=1):
            print(f"Pokemon {index} is in gen {legendary}")
    
    
            

while listloop: 
    print("")
    random_type_combo = random.choice(list(pokemonData.dualtypedic.keys()))
    random_type_pokemon = list(pokemonData.dualtypedic[random_type_combo])
    
    
    print(f"name all {len(random_type_pokemon)} {random_type_combo} type pokemon!")
    
    while guessloop: 
       
        action = decaps(input("Guess or Hint? "))
        print("")
        if action == "guess":
            guess()
        elif action == "hint":
            hint(random_type_pokemon)
        else:
            print("Oops, That's not a possible answer")

        
            
