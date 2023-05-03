import ninjas
import pets
# implement __init__( first_name , last_name , treats , pet_food , pet )

reggie_pet_info = {
    "name": "Sir Reginald the Third",
    "type": "dog",
    "tricks": ['Sit', 'Stay for 2 seconds', 'Lay Down but really just sit again'],
    'sound' : 'rrrrwooof'
}

kitty_the_cat = {
    "name": "kitty_the_cat",
    "type": "cat",
    "tricks": ["Sorry the only trick I know is pooping in the litter box."],
    'sound' : 'meooow'
}

luke_ninja_info = {
    "first_name": "Luke",
    "last_name": "Jech",
    "treats": "peanut butter",
    "pet_food": "aligator bites",
    "pets": {
        "reggie": reggie_pet_info,
        "kitty": kitty_the_cat
        }
}


luke = ninjas.Ninja(luke_ninja_info)


luke.feed()
luke.walk()
luke.bathe()

print(luke.cat.lives)
luke.cat.noise()
luke.cat.sleep()
